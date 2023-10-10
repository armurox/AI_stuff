# Nim
Nim is a library of code written in Python for playing the game Nim. Nim is a two-player game featuring an initial board of `piles`, each with a certain number of elements, and two players taking turns. The objective of the game is to be the last player to remove one or more objects from a pile. This program allows for the usage of an AI that is trained to play NIM, based on Q-learning (a form of reinforcement learning).

## Libraries
Nim code requires the following libraries:
* `math`: performs mathematical functions and calculations
* `random`: introduces randomness to the game through its functions
* `time`: provides date and time related functions 
Alternatively, install the libraries with `pip3 install -r requirements.txt`

## Code Summary
Nim is a class with a constructor, available actions and other player getters, a switch player method, and a move method. The NimAI class is also included, which allows a player to update game states, get q-values, update q-values, get the best future reward, and choose an action. In addition, there are two methods: train(n) and play, which allow training of an AI player over n games, and playing with an AI or human, respectively.

## Features
Nim is a two-player game featuring a board composed of `piles`. Each pile contains a certain number of objects. Players take turns removing one or more objects from a pile in an attempt to be the last player to remove an object. The AI is updated using Q-Learning, where the AI is able to improve its performance after each game. The AI includes features such as the ability to choose optimal actions for each game state, and exploit its knowledge of optimal move choice.

---
Please note that the starter code for the actual NIM object is not my work, and was provided as starter code for the course CS50AI. Starter code ©2023 Brian Yu/ Harvard 2023
