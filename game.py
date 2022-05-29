


directions = [

[1, 0], #down

[1, 1], #down-right

[0, 1], #right

[-1, 1] #up-right

]
#with the negative direction, 8 directions are compleye





import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

print("Connect Arbitrary")
print("-----------------")
print("Connect Four but not necessarily four any more!")
def prettyprintboard(b):
    return "\n".join(["".join(el) for el in b])


width = int(input("What is the width?"))
height = int(input("What is the height?"))

arb = int(input("Connect how many?"))

howmanyplayers = int(input("How many players?"))

board = [["." for i in range(width)] for j in range(height)]

print(board)
cls()
print(prettyprintboard(board))

gamewon = False

while not gamewon:
    for i in range(howmanyplayers):
        playernumber = str(i+1)
        print("It is player {}'s turn!".format(str(playernumber)))
        
        foundanemptyspot = False
        while not foundanemptyspot:
            colinput = int(input("Which column to play on?"))
            # placing the piece: this will need checking and gravity
            rowcount = 0
            if board[rowcount][colinput-1] == ".":
                # it is unpopulated, found an empty spot
                foundanemptyspot = True
                foundthefinalspot = False
                while not foundthefinalspot and rowcount < height-1:
                    rowcount += 1
                    if board[rowcount][colinput-1] == ".":
                        pass
                    else:
                        rowcount-=1
                        foundthefinalspot = True
                board[rowcount][colinput-1]=playernumber
            else:
                print("Sorry, it is full, try again")
        cls()
        print(prettyprintboard(board))
        # now that the player has made his move, time to check if his piece contributes to a potential line bidirectionally. 
        piecerow = rowcount
        piececolumn = colinput-1
        dirlinkagetotal = [0,0,0,0]
        for i, direction in enumerate(directions):
            linkages = [0, 0]
            #print(direction)
            for i2, factor in enumerate([-1, 1]):
                mpiecerow = piecerow
                mpiececolumn = piececolumn
                didnotmatch = False
                while not didnotmatch:
                    mpiecerow += direction[0]*factor
                    mpiececolumn += direction[1]*factor
                    if mpiecerow < 0 or mpiececolumn < 0 or mpiecerow >= height or mpiececolumn >= width or board[mpiecerow][mpiececolumn] != playernumber:
                        didnotmatch = True
                    else:
                        linkages[i2] += 1
            
            dirlinkagetotal[i]=1+linkages[0]+linkages[1]
        #print(dirlinkagetotal)
        if max(dirlinkagetotal) >= arb:
            print("Player {} won!".format(playernumber))
            gamewon = True

        

