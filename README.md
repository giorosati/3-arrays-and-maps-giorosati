# Project 3: Arrays & Maps
Please complete the following 3 functions. 
You can test by running the `pytest` or `python3` commands:

* To run just the main code for one problem: `python3 frequency.py`
* To run the tests for one problem: `pytest frequency_test.py`
* To run all the tests prior to submission: `pytest`

### Files that should (& shouldn't!) be changed

You **SHOULD** implement your problem solutions in the following files:
* `frequency.py`
* `multiply.py`
* `tic_tac_toe.py`

You **SHOULD NOT** modify the following files:
* anything in the `files` folder
* `frequency_test.py`
* `multiply_test.py`
* `tic_tac_toe_test.py`

Looking for additional practice problems to prepare for the exam? Checkout:
* programs in the `practice` folder

<!--### General Hints
* ???-->

## Problem 1: Word Frequency

Implement a function `word_frequencies` that takes
a string filename as a parameter and returns a
dictionary mapping each word in the text file
to the total number of times it occurs. All
letters should be treated as lower case, and both
punctuation and numbers should be ignored (best practice is to replace with a space).
Letters separated by apostrophes should be left together
(for example, `don't` becomes `dont`).
Your solution may use string & file functions.

**Example call**

`print_map_by_value(word_frequencies("files/turing.txt"))`

**Outputs**
```
    10 the
     4 code
     3 of
     2 turing
     2 and
     2 at
     2 secret
     2 war
     2 enigma
     1 imitation
     1 game
     1 based
     1 on
     1 real
     1 life
     1 story
     1 legendary
     1 cryptanalyst
     1 alan
     1 film
     1 portrays
     1 nail
     1 biting
     1 race
     1 against
     1 time
     1 by
     1 his
     1 brilliant
     1 team
     1 breakers
     1 britains
     1 top
     1 government
     1 cypher
     1 school
     1 bletchley
     1 park
     1 during
     1 darkest
     1 days
     1 world
     1 ii
     1 true
     1 was
     1 man
     1 who
     1 cracked
     1 behind
     1 every
     1 is
     1 an
     1 unlock
     1 win
```

_**Hint**: Looking for how to remove punctuation? 
See https://www.techiedelight.com/remove-punctuations-string-python/_

_**Note**: If you would like an extra challenge with MESSY real world data, you can try the included test_austen() challenge. This is an entire Jane Austen book that you can work on cleaning to find the word frequencies on. It will not display the entire dictionary in the console, you would need to find another way to check the data. This can take a week or more of extra time debugging, researching, and manipulating the data to match the expected output exactly. If you would like to opt into this additional challenge (recommended for those interested in Data Science), uncomment the test_austen() in frequency_test.py and use the austen file as well in frequency.py. Happy Coding!_

## Problem 2: Multiplication Table

Write a function called `multiplication_table` that
takes a width, height, & scaling factor as parameters
and returns a two-dimensional array multiplication
table scaled by the scaling factor.
You should not be using _any_ functions other than `range`, `len`, 
or `append` in implementing your solution.

![multiplication_table(5, 3, 1)](http://emhill.github.io/151/morea/12.arrays//fig1.png)
![multiplication_table(5, 3, 2)](http://emhill.github.io/151/morea/12.arrays//fig2.png)


| **Example calls** | **Returns** |
| -------------- | --------- |
| `print_2D(multiplication_table(5, 3, 1))` | `[1, 2, 3, 4, 5]`<br>`[2, 4, 6, 8, 10]`<br>`[3, 6, 9, 12, 15]` |
| `print_2D(multiplication_table(5, 3, 2))` | `[2, 4, 6, 8, 10]`<br>`[4, 8, 12, 16, 20]`<br>`[6, 12, 18, 24, 30]` |

_**Hint**: Looking to initialize your array? Try a list comprehension:_ `[ [ 0 for i in range(w) ] for i in range(h) ]`. The code `[[0]*w]*h` **WILL NOT work**!

## Problem 3: DID I WIN TIC-TAC-TOE?

Write a function `did_I_win_2D` that takes a string player name
and a 2-dimensional 3 x 3 array as parameters
and returns whether the player won the game.

| **Example calls** | **Returns** |
| -------------- | --------- |
| `b = [["X", "O", "O"]] * 3`<br>`did_I_win_2D("X", b)` | `True` |
| `b = [["X", "O", "O"]] * 3`<br>`did_I_win_2D("O", b)` | `True` |
| `b = [`<br>`['O', 'O', 'X'],`<br>`['O', 'X', 'O'],`<br>`['X', 'O', 'O'] ]`<br>`did_I_win_2D("X", b)` | `True` |
| `b = [`<br>`['O', 'O', 'X'],`<br>`['O', 'X', 'O'],`<br>`['X', 'O', 'O'] ]`<br>`did_I_win_2D("O", b)` | `False` |


_**Hint**: What does a boolean accumulator / aggregator variable look like?_

## Getting started

### Develop in an IDE
 
You will need to install PyCharm (or another IDE),
git, and pytest. PyCharm has some built-in git 
support.

## Testing
Many of the tests are failing right now because the 
functions
aren't outputting the correct information. Fixing this
will make the tests pass & turn green.

### Setup

#### repl.it or command line
To use pytest on repl.it, install it first:

`pip3 install pytest`

To install pytest on the command line for running on a laptop (using a linux or unix based command-line like MacOS):

`sudo -H pip3 install pytest`

#### Pycharm
If using PyCharm, you may need to fix your project setup.
- Open the **Settings/Preferences | Tools | Python Integrated Tools** settings dialog.
- In the Default test runner field select **pytest**.
- Click OK to save the settings.

#### VS Code
If using VS Code, you may need to configure your pytest settings.
- Open a python (.py) file
- In the testing panel, select the **Configure Pytests** button
- Select **.root** directory for the testing route
- Refresh the panel if needed if tests are not discovered

### Run commands
To run just the main code for one problem:

`python3 frequency.py`

To run the tests for one problem:

`pytest frequency_test.py`

To run all the tests prior to submission:

`pytest`
