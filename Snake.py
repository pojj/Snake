import pygame
import time
import sys
import random

def move(board,length,grow):
    if direction=="up":
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]==1:
                    if board[i-1][j]>0 or i-1==-1:
                        return "die"
                    if board[i-1][j]==-1:
                        grow=True
                    board[i-1][j]="new"
                    
    if direction=="down":
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]==1:
                    if board[i+1][j]>0:
                        return "die"
                    if board[i+1][j]==-1:
                        grow=True
                    board[i+1][j]="new"
                    
    if direction=="left":
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]==1:
                    if board[i][j-1]>0 or j-1==-1:
                        return "die"
                    if board[i][j-1]==-1:
                        grow=True
                    board[i][j-1]="new"
                    
    if direction=="right":
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]==1:
                    if board[i][j+1]>0:
                        return "die"
                    if board[i][j+1]==-1:
                        grow=True
                    board[i][j+1]="new"
                
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]!=0 and board[i][j]!="new" and board[i][j]!=-1:
                board[i][j]=(board[i][j]+1)

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]=="new":
                 board[i][j]=1
    if grow==False:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]==int(length+1):
                    board[i][j]=0
    if grow==True:
        return grow
    
 
        
def food(board):
    while True:
        x=random.randint(0,24)
        y=random.randint(0,24)
        if board[x][y]==0:
            board[x][y]=-1
            break
            
            
    

pygame.init()
screen=pygame.display.set_mode(size=(805,805))
pygame.display.set_caption("Snake")

clock=pygame.time.Clock()

board=[]
for i in range(25):
    temp=[]
    for j in range(25):
        temp.append(0)
    board.append(temp)

board[11][12]=1
board[12][12]=2
board[13][12]=3
board[14][12]=4
board[15][12]=5

direction="up"
length=5
tick=0
turned=False
dead=False
food(board)


while True:
    tick+=1
    grow=False
    #how many frames per move
    if tick%5==0 and dead==False:
        try:
            grow=move(board,length,grow)
        except:
            grow="die"
        if grow=="die":
            dead=True
            print("you dead")
        turned=False
    if grow==True:
        length+=1
        food(board)
    
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_BACKSPACE:
                pygame.quit()
                sys.exit()
            if event.key==pygame.K_w:
                if direction!="down"and turned==False:
                    direction="up"
                    turned=True
            if event.key==pygame.K_s:
                if direction!="up"and turned==False:
                    direction="down"
                    turned=True
            if event.key==pygame.K_a:
                if direction!="right"and turned==False:
                    direction="left"
                    turned=True
            if event.key==pygame.K_d:
                if direction!="left"and turned==False:
                    direction="right"
                    turned=True
            if event.key==pygame.K_ESCAPE:
                board=[]
                for i in range(25):
                    temp=[]
                    for j in range(25):
                        temp.append(0)
                    board.append(temp)

                board[11][12]=1
                board[12][12]=2
                board[13][12]=3
                board[14][12]=4
                board[15][12]=5

                direction="up"
                length=5
                tick=0
                turned=False
                dead=False
                food(board)
                    
                
    #fps
    clock.tick(30)
    
    screen.fill((0,0,0))
    
    for i in range(25):
        for j in range(25):
            if board[i][j]>0:       
                pygame.draw.rect(screen,(0,255,0),[5+(32*j),5+(32*i),27,27],0)
            if board[i][j]==-1:       
                pygame.draw.rect(screen,(255,0,0),[5+(32*j),5+(32*i),27,27],0)

    pygame.display.flip()

