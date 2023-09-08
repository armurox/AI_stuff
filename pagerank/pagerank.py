import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(link for link in pages[filename] if link in pages)

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    num_links = len(corpus[page])
    num_pages = len(corpus)
    prob_dist = {}
    # Set all pages probabilities to equal selection first
    for link in corpus:
        prob_dist[link] = (1 - damping_factor) / num_pages
    # Add on the appropriate probabilites to the pages linked by the current page
    if num_links != 0:
        for link in corpus[page]:
            prob_dist[link] += damping_factor / num_links
    return prob_dist


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # Choose the first page at random
    page = random.choice(list(corpus.keys()))
    page_rank = {}
    for element in corpus:
        page_rank[element] = 0
    page_rank[page] += 1 / n
    # Keep sampling pages based on the transition model weight from the previous sample
    for _ in range(n - 1):
        page = random.choices(
            list(corpus.keys()),
            weights=transition_model(corpus, page, damping_factor).values(),
            k=1,
        ).pop()
        page_rank[page] += 1 / n
    return page_rank


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # Assume at first the every page is chosen with equal probability
    page_rank = {}
    n = len(corpus)
    for page in corpus:
        page_rank[page] = 1 / n
    prev_page_rank = page_rank.copy()
    # Update the corpus for pages with no outgoing links (interpret them as linking to everything)
    for page in corpus:
        num_links = 0
        if len(corpus[page]) == 0:
            for element in corpus:
                corpus[page].add(element)
    while True:
        for page in corpus:
            page_rank[page] = (1 - damping_factor) / n
            # Identify pages which link back to the current page
            for element in corpus:
                if page in corpus[element]:
                    page_rank[page] += damping_factor * (
                        prev_page_rank[element] / len(corpus[element])
                    )
        end = True
        # Keep repeating until the page rank values are converging appropriately
        for page in page_rank:
            if page_rank[page] - prev_page_rank[page] > 0.001:
                end = False
                break
        if end:
            break
        else:
            prev_page_rank = page_rank.copy()

    return page_rank


if __name__ == "__main__":
    main()
