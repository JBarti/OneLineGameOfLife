# OneLineGameOfLife
Conway's Game of Life written as a one liner in Python.

Version of Python used for testing is 3.7.3.

The file `min_game_one_line.py` is the one line of code containing the whole logic of Conway's Game of Life. You can find the code descrambled inside `min_game.py` 

The code contains no:
 - functions that would require creating a separate indentation block
 - standalone if/else blocks (all of the branching is done as a part of comprehensions)
 - for loops (every loop is a comprehension)

A single recursive immedietly invoked lambda function contains the whole logic of the game, the function is then passed into another lambda function as an argument to. The second lambda function is immedietly invoked so that we could avoid making a function call thus adding a new line of code.

To run the game use the command `python3 ./min_game_one_line.py`. Press enter to proceed into the next generation and type `q` to exit the program.
