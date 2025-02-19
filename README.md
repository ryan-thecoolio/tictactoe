# tictactoe
the game impossible to win
I was SO close to entirely writing all my code from scratch, NO AI HELP THIS TIME.
I realized I was so dependent on my friend chat that I struggled to write logical ideas. For example, checking to see if a horizontal or vertical row was all the same number (indicating a player had won). In fact, I thought creating the game would take at most a few hours. It took a couple of hours...which required a layover because I was confused on how to display Xs and Os while storing numerical values as the logical functions in my code are based on simple arithmetic. 

As you may or may not know, most of the code I write is purely brute force, so if it does not work, then I simply find an alternative, or keeping going at it until VS Code decides to stop prompting me error messages. Although that may not necessarily indicate the portion of my code is working, and something sneakily hiding in my code is interfering with the rest of the somewhat function code ;) So, because I did not have my good trusty pal, the guy who basically writes all my code when I give up after 1 minute, I ended up suffering hours, in fact, I was going on and off during the last bit when I implemented my logical code to the aesthetic portion of my code and for some reason, the math was not adding up! Even though I changed a couple of things, I was confused why it was not adding correctly. After a day of writing the code, I have already forgotten the error, but one thing that I did not forgot, which was after every time I solved a bug was a feeling of relief, joy, and also an increase in my "resilience," if I possess any at all, since I did give up on attempting to display the X and O board. But you know how it is, sometimes, you got to do what you got to do, plus I relied on a new friend, *Google.* While it is not any better, at least it took some effort, and I also just quickly glanced at the code.

As a matter of fact, let me explain the visual display. First, I create a dictionary 
``self.pos = {1: ' ',2: ' ',3: ' ',...,9: ' '}`` which hold the 9 possible values of the graph. In my code, I model the points like a cartesian graph, only that the top-left is ``(1,1)`` and the bottom-right is ``(3,3)`` which may be confusing, as one normally would just select where they go, and typing coordinates may feel odd, but hey at least it is not based on index, as ``(0,0)`` and ending at ``(2,2)`` is weirder.  Then I create a print statement that constantly is called in a function as it is placed in a while True loop in another function. Inside the display function the print is divided into three parts ``1-3``,``4-6``,``7-9`` and since the user's input is not based on index, I do not have to add 1 to accommodate the initial start value of 1. Moreover, to change the value of an index in the dictionary it is the same as a list where ``self.pos[index] = value`` will change the current value in the index which are all simply empty strings ``' '`` to become either: ``X`` or ``O``. I think I overcomplicated the process, since I initially create the display using a for loop with lines:

```
width = 3
height = 3
for i in range(height):
	print(' --- '*width)
	print(' |  '*(height+1))
print(' --- '*width)
```

However, the obvious thing that stumped me was how could I input values, since this function is just a loop printing out loops, and holds no values that could be changed. Naturally or unnaturally, since nobody googles things anymore and just uses AI, I required assistance, if you may and that is the end of explanation and rant on why AI is probably bad if you want to improve on anything and simply just ask someone who is not you for help. It is the like asking the teacher for help on a test, clearly, you do not know something. (Which is why I brute force my solutions)

Now, moving onto how I actually made the Tic-Tac-Toe game. It was obvious that the only possible methods for a player to win is by getting three in a row in three possible ways: horizontal, vertical, or diagonally. So, I would not consider this help, but I did create my tic tac toe based on a guide on how to make it. In other words, the building blocks for the game. Although as I mentioned above, the string I printed was the first task to create the game, which I scraped entirely because if you compare the final solution of the game, you would notice that it looks nowhere near the same as it did in the initial step. However, the second task for creating a matrix which is a list inside a list like this: ``[['0','1','2'],['1','0','2'],['2','1','0']]``. So in the sub lists, 0 represents a "free" spot, 1 represents player 1 and 2 represents player 2. What I noticed was, if you add the sum when a row is taken up by 1 or 2 (horizontal), player 1 and player 2 respectively equal to 3 and 6. 

Although, what problem that I later found an intuitive solution to overcome, is that since there are free spots, while a number that contains at least 1 0 or 1 can never become a 6, if there is one 0 and one 2, it is possible to get a sum of 3. However, I solved this issue on my own, by looping through the rows and columns and if there was a zero, it would be skipped, i.e., the loop breaks since there is no point of looping any further into the remaining numbers. In order to indicate whether it is 1 or 2, i.e., player 1 or player 2 has won, if it is a sum of 6, it adds 2 to the variable count, while if it is a sum of 3, it adds 1. As a result, when the function is returned and there is a winner, if the function calling this function receives a 3, it prints out that player 1 has won and vice verse if it is a 6.

Also, to find the sum, for the row, I could simply just use the ``sum(row)`` list method, but for the column, I had to create a loop that would iterate through the second index i.e., ``self.board[col][i]`` where i is the current column and it should actually be named row instead of col, as the for loop goes down one by own until add values have been added and then returned. 

Interestingly, for the diagonal, where there are two possibilities, I later realized a different approach, which probably would be more difficult and require more brute force would be simply switching the first and second index since this is how the diagonal is mapped.
```
[0][0] [0][1] [0][2]
[1][0] [1][1] [2][2]
[2][0] [2][1] [2][2]
```

So you will notice that the middle will always be ``[1,1]`` regardless which side the diagonal is coming from, but my approach was to iterate from top-left to bottom-right and bottom-left to top-right:

 *Top-Left to Bottom-Right*
```
for j in range(self.length):
	self.board[j][j]
```

Although there are restrictions like above, to break the function as soon as there is a 0.

*Top-Right to Bottom-Left*
```
for j in range(self.length):
	self.board[j][(self.length-j)-1]
```
The first index starts at 0 and second index starts at 2 which go all the way to
``[2][0]``.

The loops are nearly identical to the column and rows function as the premise of finding a sum of 3 and 6 are the same. 

Furthermore, I create another class, ``class Interactive()`` where the two players are able to chose their location and where the display is located.

There is a function that starts the round, alternating between ``self.p1_turn()`` and ``self.p2_turn()``, where in between it will display the board as well as check if player 1 or 2 has won yet.

**What I learned** 
One thing I learned was matrixes, which are lists of list and the index can be called by creating a double index if you will. If I explore this concept further, I may use this in my connection game, otherwise, I am considering using another new concept of dictionaries into my game as I am able to change the values into string and display it on the terminal which I was trying to learn and find while making Tic Tac Toe. Furthermore, I learned the hardships of being self-reliant and not depending on someone else to help you when you are struggling and getting easily angered a lot...
