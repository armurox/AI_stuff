# NLTK Parser
A command line tool to parse sentences using the Natural Language Toolkit (NLTK). This allows one to identify the syntax tree of a sentence, using a context-free grammer as a base.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisities
NLTK is the only library required for this parser:

* nltk

You can install the prerequisite libraries with the following command:

`pip3 install -r requirements.txt`

Or separately:

`pip3 install nltk`

### Usage

To use this parser, provide it with a sentence.

#### From the command line

Run `python3 nltk_parser.py` followed by the sentence you wish to parse.

## Summary
This parser uses the NLTK library to tokenize a sentence, and parse it into a tree. It then returns a list of noun phrase chunks in the sentence.

## Features
This parser: 

* breaks a sentence down into individual words
* uses NLTK to parse the sentence into a tree structure
* returns a list of all noun phrase chunks in the sentence

## Acknowledgements
Thank you to NLTK for providing a useful library for handling natural language processing tasks.