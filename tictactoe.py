#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output


# In[2]:


inpboard=[' ']*10
def disp_table(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])


# In[3]:


def player_inp():
    marker=' '
    marker=input('choose X or O ')
    player1=marker
    if player1=='X'or player1=='x':
        player2='o'
        player1='x'
    else:
        player2='x'
        player1='o'
    return player1,player2


# In[4]:


def placing(inpboard,pos,marker):
    if inpboard[pos] not in range(1,9):
        inpboard[pos]=marker
        return 1
    else:
        return 0


# In[5]:


def check(a,b,c,inpboard):
        if inpboard[a]==inpboard[b] and inpboard[a]!=' ' and inpboard[b]!=' ' and inpboard[c]!=' ':
            if inpboard[b]==inpboard[c]:
                return 1
            else:
                return 0


# In[6]:


def winner(w):
    if w!='abc':
        print(w + ' is the winner')
        a=input("enter Y to try again, else enter N ")
        if a=='Y':
            player_inp()
            func(inpboard)
        else:
            exit()
    else:
        print("Draw match")
        a=input("enter Y to try again, else enter N ")
        if a=='Y':
            player_inp()
            func(inpboard)
        else:
            exit()


# In[7]:


def func(inpboard):
    z=0
    n=1
    q=0
    p1,p2=player_inp()
    while n<=9:
        if n%2!=0:
            m=p1
            while q==0:
                p=int(input("player 1 enter your position "))
                q=placing(inpboard,p,m)
                disp_table(inpboard)
            q=0
        else:
            m=p2
            while q==0:
                p=int(input("player 2 enter your position "))
                q=placing(inpboard,p,m)
                disp_table(inpboard)
            q=0
        if check(1,2,3,inpboard)==1:
            w=inpboard[1]
            winner(w)
        elif check(4,5,6,inpboard)==1:
            w=inpboard[4]
            winner(w)
        elif check(7,8,9,inpboard)==1:
            w=inpboard[7]
            winner(w)
        elif check(1,4,7,inpboard)==1:
            w=inpboard[1]
            winner(w)
        elif check(2,5,8,inpboard)==1:
            w=inpboard[2]
            winner(w)
        elif check(3,6,9,inpboard)==1:
            w=inpboard[3]
            winner(w)
        elif check(1,5,9,inpboard)==1:
            w=inpboard[1]
            winner(w)
        elif check(3,5,7,inpboard)==1:
            w=inpboard[3]
            winner(w)
        n+=1
    w='abc'
    winner(w)


# In[ ]:


func(inpboard)


# In[ ]:




