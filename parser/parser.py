import nltk
import sys

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> NP VP | S Conj S | VP NP
AP -> Adj | Adj AP | Det Adj
NP -> N | Det N | Det N PP | AP NP | N PP | N Conj NP | Det N Adv | N Adv
PP -> P NP
VP -> V | V NP | V PP | V Conj VP | Adv V NP | V Adv | V Adv NP
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():
    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    # Seperate all whitespaced parts of sentences
    words = nltk.tokenize.word_tokenize(sentence)
    final_words = []
    for word in words:
        # Add any words that contain at least one alphabetic character to the word list (and convert to lowercase)
        if word.isalpha():
            final_words.append(word.lower())
    return final_words


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    # Initialize noun phrase chunks list
    chunks = []
    # Loop through all subtrees that contain the "NP" label
    for t in tree.subtrees(lambda t: t.label() == "NP"):
        add = True
        # Loop through all the subtrees of the "NP" subtrees, and only add the subtree to the chunks list if it does not contain "NP" itself
        for i in range(len(t)):
            for element in t[i].subtrees():
                if element.label() == "NP":
                    add = False
        if add:
            chunks.append(t)
    return chunks


if __name__ == "__main__":
    main()
