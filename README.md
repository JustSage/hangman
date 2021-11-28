
### CLI Hangman implementation in Python 3

To initiate the game run `python src/main.py` in the commandline.<br>
The goal of hangman is to guess a hidden word within **6 guesses**, otherwise you'll get hanged!

#### Steps:
-> Guess a letter.<br>
-> If the letter is in the word, it will replace the "_" (resembles a hidden letter) wherever it's located.<br>
-> If the letter is not in the word, an ascii image of a man being hanged will be printed to the terminal.<br>

Indicators such as used letters and letters remaining will be printed in each round.

#### Credits:

* [ASCII Hangman](https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c) for the ascii images. <br>
* [Hangmanwords.com](https://www.hangmanwords.com/) for providing data.<br>

<b><br>Any feedback will be appreciated.</b><br>
