import sys

from crossword import *


class CrosswordCreator:
    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy() for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont

        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size, self.crossword.height * cell_size),
            "black",
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                rect = [
                    (j * cell_size + cell_border, i * cell_size + cell_border),
                    (
                        (j + 1) * cell_size - cell_border,
                        (i + 1) * cell_size - cell_border,
                    ),
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        _, _, w, h = draw.textbbox((0, 0), letters[i][j], font=font)
                        draw.text(
                            (
                                rect[0][0] + ((interior_size - w) / 2),
                                rect[0][1] + ((interior_size - h) / 2) - 10,
                            ),
                            letters[i][j],
                            fill="black",
                            font=font,
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        for var in self.domains:
            # Initialize set of words in the domain to remove
            to_remove = set()
            for word in self.domains[var]:
                # Add word to the to_remove set if it is not equal to the length of the variable it should be added to
                if len(word) != var.length:
                    to_remove.add(word)
            # Remove the word in to_remove from self.domains at the variable key
            for word in to_remove:
                self.domains[var].remove(word)

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        revised = False
        to_remove = set()
        # If there is an overlap, then we can check if the domain of x should be revised
        if self.crossword.overlaps[x, y] != None:
            for word in self.domains[x]:
                r = True
                for y_word in self.domains[y]:
                    # If there exists a y-word such that it and the x-word share a letter at the appropriate overlap point,
                    # then the x-word does not need to be removed
                    if (
                        word[self.crossword.overlaps[x, y][0]]
                        == y_word[self.crossword.overlaps[x, y][1]]
                        and word != y_word
                    ):
                        r = False
                if r:
                    revised = True
                    to_remove.add(word)
            for word in to_remove:
                self.domains[x].remove(word)

        return revised

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        # Set initial arc list to be all the arcs in the problem if not specified
        if arcs == None:
            arcs = []
            for x in self.domains:
                for y in self.domains:
                    if x == y:
                        continue
                    arcs.append((x, y))
        # Run ac-3, constantly removing elements and making them arc consistent until there are no more left
        while len(arcs) != 0:
            (x, y) = arcs.pop(0)
            # Ignore the case of the same variable
            if x == y:
                continue
            if self.revise(x, y):
                if len(self.domains[x]) == 0:
                    return False
                for z in self.crossword.neighbors(x):
                    arcs.append((z, y))
        return True

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        if len(self.domains) != len(assignment):
            return False
        return True

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        used_words = set()
        for var in assignment:
            # Invalid word size
            if len(assignment[var]) != var.length:
                return False
            # Can't use words again
            if assignment[var] in used_words:
                return False

            # Check if the assignment is consistent with overlap rules
            for overlap in self.crossword.neighbors(var):
                if overlap in assignment:
                    if (
                        assignment[var][self.crossword.overlaps[var, overlap][0]]
                        != assignment[overlap][self.crossword.overlaps[var, overlap][1]]
                    ):
                        return False
            used_words.add(var)
        return True

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        # Initialize dictionary which will contain the words of var as the keys, and the number of ruled out values of neighbors as the values
        ruled_out = {word: 0 for word in self.domains[var]}
        # Loop through the word domain of var
        for word in self.domains[var]:
            # Loop through its neigbors
            for neighbor in self.crossword.neighbors(var):
                # Loop through the words of the neighbors
                for temp_word in self.domains[neighbor]:
                    # Increase the number ruled out by the word by 1 if the word in the neighbor does not have an overlapping character at the appropriate point
                    if (
                        word[self.crossword.overlaps[var, neighbor][0]]
                        != temp_word[self.crossword.overlaps[var, neighbor][1]]
                    ):
                        ruled_out[word] += 1

        # Return a list, sorted in ascending order by the dictionary value
        return sorted([word for word in ruled_out], key=lambda w: ruled_out[w])

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        # Candidate variables
        possible_vars = []
        # Minimum remaining value
        # mrv = len(self.domains[min(self.domains, key = lambda var: len(self.domains[var]))])
        mrv = len(self.crossword.words) + 1
        for var in self.domains:
            if var in assignment:
                continue
            var_len = len(self.domains[var])
            if var_len < mrv:
                mrv = var_len
        for var in self.domains:
            # Consider only unassigned variables
            if var in assignment:
                continue
            var_len = len(self.domains[var])
            # Variable must have minimum number of remaining values in its domain
            if var_len == mrv:
                possible_vars.append(var)
        # Return the variable with the maximum degree
        max_deg = -1
        un_var = possible_vars[0]
        for var in possible_vars:
            deg = len(self.crossword.neighbors(var))
            if deg > max_deg:
                max_deg = deg
                un_var = var
        return un_var

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        if self.assignment_complete(assignment):
            return assignment
        var = self.select_unassigned_variable(assignment)
        for word in self.order_domain_values(var, assignment):
            temp_assignment = assignment.copy()
            temp_assignment[var] = word
            if self.consistent(temp_assignment):
                result = self.backtrack(temp_assignment)
                if result is not None:
                    return result
        return None


def main():
    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
