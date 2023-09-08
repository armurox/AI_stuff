from pagerank import *

def test_transition_model():
    assert(transition_model({"1.html": {"2.html", "3.html"}, "2.html": {"3.html"}, "3.html": {"2.html"}}
                            , "1.html", 0.85) == {"1.html": 0.05, "2.html": 0.475, "3.html": 0.475})