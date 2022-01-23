import random
class MyGame:
    boardWidth=4
    boardHeight=4
    target=2048
    
    def __init__(self) -> None:
        self.board=[[0 for i in range(self.boardWidth)]for j in range(self.boardHeight)]
    
    def showBoard(self):
        for i in self.board:
            print(i)
    
    def readInput(self):
        inp=input("enter wasd-")
        if inp.lower()=="w" or inp.lower()=="a" or inp.lower()=="s" or inp.lower()=="d":
            inputMapping={"w":"up","a":"left","s":"down","d":"right"}
            return inputMapping[inp.lower()]
        return None
    
    def getEmptyPositions(self):
        res=[]
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j]==0:
                    res.append([i,j])
        return res
    
    def hasWon(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j]==self.target:
                    return True
    
    def setValue(self,pos,value):
        self.board[pos[0]][pos[1]]=value
    
    def getRandomValueForBoard(self):
        return random.choice([2,4])
    
    def gameOver(self):
        print("Game Over")
    
    def newGame(self):
        gameContinuedAfterWin=False
        while True:
            emptyPositions=self.getEmptyPositions()
            if len(emptyPositions)==0:
                self.gameOver()
                break
            if not gameContinuedAfterWin:
                if self.hasWon():
                    print("\n You Won!! \n")
                    if(input("continue playing? y/n")=="y"):
                        gameContinuedAfterWin=True
                    else:
                        break
            emptyRandomChoice=random.choice(emptyPositions)
            self.setValue(emptyRandomChoice,self.getRandomValueForBoard())
            self.showBoard()
            while True:
                if self.move(self.readInput())==True:
                    break
                else:
                    print("cant perform action")
    
    def move(self,dir):
        if dir=="up" or dir=="down":
            return self.moveVertical(dir)
        elif dir=="left" or dir=="right":
            return self.moveHorizontal(dir)
        print("invalid")
        return False
    
    def moveHorizontal(self,dir):
        moved=False
        if dir=="left":
            j=0
            increment=1
            end=len(self.board[0])-1
        elif dir=="right":
            j=len(self.board[0])-1
            increment=-1
            end=0
        for row in range(len(self.board)):
            if dir=="left":
                j=0
            elif dir=="right":
                j=len(self.board[0])-1
            while j!=end:
                k=j+increment
                while k>=0 and k<len(self.board[row]) and self.board[row][k]==0:
                    k+=increment
                if k>=0 and k<len(self.board[row]):
                    
                    if self.board[row][j]!=0:
                        if self.board[row][k]==self.board[row][j]:
                            self.board[row][j]+=self.board[row][k]
                            self.board[row][k]=0
                            moved=True
                    else:
                        self.board[row][j]=self.board[row][k]
                        self.board[row][k]=0
                        moved=True
                        continue
                j+=increment
        return moved
    
    def moveVertical(self,dir):
        moved=False
        if len(self.board)>0:
            if dir=="up":
                j=0
                increment=1
                end=len(self.board)-1
            elif dir=="down":
                j=len(self.board)-1
                increment=-1
                end=0
            for col in range(len(self.board[0])):
                if dir=="up":
                    j=0
                elif dir=="down":
                    j=len(self.board[0])-1
                while j!=end:
                    k=j+increment
                    while k>=0 and k<len(self.board) and self.board[k][col]==0:
                        k+=increment
                    if k>=0 and k<len(self.board):
                        
                        if self.board[j][col]!=0:
                            if self.board[k][col]==self.board[j][col]:
                                self.board[j][col]+=self.board[k][col]
                                self.board[k][col]=0
                                moved=True
                        else:
                            self.board[j][col]=self.board[k][col]
                            self.board[k][col]=0
                            moved=True
                            continue
                    j+=increment
        return moved

if __name__=="__main__":
    game=MyGame()
    game.newGame()