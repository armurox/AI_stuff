# PageRank Algorithm

This Python code implements the PageRank algorithm, which is used to evaluate the importance or ranking of web pages based on their links and connections. PageRank was originally developed by Larry Page and Sergey Brin, the founders of Google, and is a fundamental component of Google's search engine.

## Overview

The PageRank algorithm works by assigning each web page a numerical score (PageRank value) that reflects its importance within a network of linked web pages. The algorithm is based on the idea that important pages are linked to by other important pages. PageRank values are computed iteratively and eventually converge to a stable value for each page.

## Usage

To use this code, follow these steps:

1. Ensure you have Python installed on your system.

2. Save the code to a Python file, e.g., `pagerank.py`.

3. Create a directory containing HTML pages that you want to analyze. These pages should be linked to each other using anchor tags (`<a>`).

4. Open a terminal or command prompt and run the code with the following command, providing the path to the directory containing your HTML pages as an argument:

   ```
   python pagerank.py <directory_path>
   ```

   Replace `<directory_path>` with the actual path to your HTML files.

## Code Structure

The code consists of several functions and a `main()` function that orchestrates the execution of the PageRank algorithm. Here's an overview of the key functions:

1. `crawl(directory)`: This function parses a directory of HTML pages and identifies links between pages. It returns a dictionary where each page is a key, and the corresponding value is a set of pages linked to by the current page.

2. `transition_model(corpus, page, damping_factor)`: This function calculates the probability distribution for transitioning from the current page to other pages. It considers both the links on the current page (with a probability of `damping_factor`) and random transitions to any page in the corpus (with a probability of `1 - damping_factor`).

3. `sample_pagerank(corpus, damping_factor, n)`: This function estimates PageRank values by sampling `n` pages according to the transition model. It starts with a random page and keeps sampling pages based on the model. The result is a dictionary of PageRank values for each page.

4. `iterate_pagerank(corpus, damping_factor)`: This function iteratively computes PageRank values until convergence. It initializes PageRank values, updates them based on the links between pages, and continues until the values stabilize.

## Constants

- `DAMPING`: The damping factor, which determines the likelihood of following links versus jumping to a random page. The default value is 0.85.

- `SAMPLES`: The number of samples to use when estimating PageRank through sampling. The default value is 10,000.

## Output

The code will generate two sets of PageRank results:

1. PageRank Results from Sampling: These are estimated PageRank values based on random sampling.

2. PageRank Results from Iteration: These are PageRank values computed through iterative calculation.

The results will be printed to the console, showing the PageRank values for each page in the corpus.

## Note

- Ensure that your HTML files in the provided directory are properly formatted with anchor tags (`<a>`) for accurate link extraction.

- The PageRank algorithm is iterative and may take some time to converge, especially on large datasets.

- You can adjust the `DAMPING` and `SAMPLES` constants in the code to fine-tune the algorithm's behavior.

- This code is designed for educational purposes and may require modifications or optimizations for production use.