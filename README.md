# kioku

## description
a vocabulary building game for Japanese language speakers/ learners. players are given 9 unique character sounds, moras (モーラ), and are given the task to create as many words as possible. The only caveat is that only the last 7 words created are displayed.

## rules
* submitted words have to exist in Japanese dictionary sourced from [jamdict](https://github.com/neocl/jamdict)
* users can utilize the same mora as often as they like
* in addition the mora can be modified depending upon the relationship. i.e. if the character か is listed then が is also an acceptable mora selection
* users can shuffle the list of moras whenever they like
* repeat a word or create a word will result in one life lost
* the game is over when all lives remaining reaches 0

## live version of the game
[kioku game](https://kioku-game.herokuapp.com/)

## installation
1. clone down the repo and cd into the parent directory
2. on one terminal run python3 app.py
3. from the parent directory cd into client/
4. run npm i
5. run npm serve
