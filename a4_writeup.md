# Assignment 4 - Writeup

In assignment 4 we created a basic tic tac toe game so that we could learn object oriented programming. Respond to the following questions.

## Reflection Questions

### What was the most difficult part to tic-tac-toe? 
The most difficult part of tic-tac toe was figuring out where to begin for each function. I knew what it was asking of me, but I wasn't aways sure how to write my code in the most efficient and concise way. I also wrote some things in Java by accident, so I had to isolate what I wrote in the wrong language and where. 

### Explain how you would add a computer player to the game. 
I would add a computer player to the game by creating another player -- computer_player. At its most basic, the computer would have similar functions as the player, but choose its move randomly. 

### If you add a computer player, explain (doesn't have to be super technical) how you might get the computer player to play the best move every time. *Note - I am not grading this for a correct answer, I just want to know your thoughts on how you might accomplish it. 
I might get the computer player to play the best move every time by having it keep track of all positions on the board: the player's, and its own. The computer would then check where the player's pieces are in relation to its own, and, if there are 2 pieces in a diagonal, horizontal, or vertical line, put its own piece there to block it. Then, the computer would check if there are two of its pieces are together and put a piece in an open spot. This could be achieved using if statements. The computer could use the log of each move to then learn from it and improve for the next game. 