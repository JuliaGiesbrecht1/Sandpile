#!/usr/bin/env python
# coding: utf-8




"""
Sandpile - Julia Giesbrecht

"""



def printPile(pile):
    
    """
    prints the sandpile, a, nicely
    
        >>> printPile([[2,0,2],[0,3,0],[2,0,2]])
    [2, 0, 2]
    [0, 3, 0]
    [2, 0, 2]
    
    """
    
    for i in pile:
        print(i)


# In[49]:


def isStablePile(pile):
    """
    isStablePile(a): returns True if a is stable, i.e., all cells have values between 0 and 3, False otherwise
    
    >>> isStablePile([[0,1,2],[2,3,2],[0,0,1]])
    True
    >>> isStablePile([[0,4,0],[3,5,3],[1,2,3]])
    False
    
    """
    for row in pile:
        
        for x in row:
            if x>3:
                return False 
        
    return True
    
            


# In[53]:


def topplePile(pile):
    """
        for a stable pile, just returns a, for an unstable pile it goes
        through and topples any cells that are 4 or more and continues doing this 
        until the pile is stable (naturally, you must call isStablePile to see when you're done)
        
     >>> topplePile([[0,0,0],[0,4,0],[0,0,0]])
    [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
    >>> topplePile([[4,0,0],[0,4,0],[0,0,0]])
    [[0, 2, 0], [2, 0, 1], [0, 1, 0]]
    >>> topplePile([[4,0,0],[0,10,0],[0,0,0]])
    [[0, 3, 0], [3, 2, 2], [0, 2, 0]]
    """
   
    
  
    while isStablePile(pile) == False:
        for row in range(3):
            for column in range(3):
                if pile[row][column] >=4:
                    value = pile[row][column] -4 
                    pile[row][column] = value
                    if row+1 < 3: # checking row below
                        pile[row+1][column] +=1
                    if row-1 >= 0: # checking row above
                        pile[row-1][column] +=1
                    if column+1 < 3: # checking column right
                        pile[row][column +1] +=1
                    if column-1 >= 0: # checking column left
                        pile[row][column-1] +=1
    return pile
        
                


# In[56]:


def addPiles(pile1,pile2):  
    """addPiles(a,b): returns the resulting sandpile of adding sandpile a to sandpile b and toppling
     >>> addPiles([[0,0,0],[0,2,0],[0,0,0]], [[0,0,0],[0,2,0],[0,0,0]])
    [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
    >>> addPiles([[1,2,0],[2,1,1],[0,1,3]], [[2,1,3],[1,0,1],[0,1,0]])
    [[3, 3, 3], [3, 1, 2], [0, 2, 3]]
    """
    newpile = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    for row in range(3):
        for column in range(3):
            newpile[row][column] = pile1[row][column] + pile2[row][column]
            
    return topplePile(newpile)

            


# In[57]:


def zeroPile():

    return [[2, 1, 2], [1, 0, 1], [2, 1, 2]]
    


# In[62]:


def isInGroup(a):
    """
        returns True if the sandpile a is in Dr. Garcia-Puente's S group. 
        The way to tell if a is in S is by adding a to the zero sandpile. 
        If 𝑎+0=𝑎 then a is in S, and if it doesn't equal itself when added to 
        the zero sandpile, then a is not in S.
        
     >>> isInGroup([[3,2,2],[2,1,1],[3,3,3]])
    True
    >>> isInGroup([[1,1,1],[1,1,1],[1,1,1]])
    False
    
    """
    if addPiles(a,zeroPile()) == a:
        return True
    else:
        return False
    
 







