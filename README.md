# Sandpile

- One of the seminal papers in chaos theory is about self-organized criticality by Per Bak, Chao Tang and Kurt Wiesenfeld  written in 1987. In this paper they introduce a simple cellular automaton model called the sandpile model.

- One of the features of the sandpile model is that if you choose a certain subset of all possible sand pile states you have what's known in math as an abelian group, i.e., a set that behaves like integers under addition.


- Creating functions that creates a 3x3 sandpiles which topple on 4 grains in each cell. Sandpiles are represented by a simple 3x3 list, e.g., pile = [[2,0,2],[0,3,0],[2,0,2]] represents the sandpile with 2 on the corners, 3 in the middle, and zero in the other cells. Our ultimate goal is to (a) have a function that tells us if a given sandpile is part of Dr. Garcia-Puente's set S, and (b) count the number of possible sandpiles exactly that are in S (Dr. Garcia-Puente said there were approximately 100,000).

- Our sandpile representation is a list that has three elements, the rows. Each row is also a list that has three elements, the contents of each cell for that row. For accessing, the first index is the row number. So, if pile = [[0,1,2],[1,2,3],[2,3,0]], then pile[0] is the top row [0,1,2], pile[1] is the middle row [1,2,3], and pile[2] is the bottom row [2,3,0]. Once you have accessed the row you can then look at the individual column's cell contents by indexing again. So, for instance, pile[0][0] is the top-left corner, pile[0][2] is the top-right corner, pile[1][1] is the center cell, and pile[2][0] is the bottom-left corner. You can also assign a variable to the row and access from it, so, for instance you could get to the center cell with centerRow = pile[1]; center = centerRow[1]. Usually to look at all the cells you'd use a nested loop, where the outside loop iterates over the rows and the inside loop over the columns within the current row. 
