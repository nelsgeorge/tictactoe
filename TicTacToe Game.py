import random

print("welcome to tictactoe")
print("---------------------")
print()

row1 = [1,2,3,4,5,6,7,8,9]


def board():
    print("+---+---+---+")
    print("|", row1[0],"|", row1[1],"|", row1[2],"|")
    print("+---+---+---+")
    print("|", row1[3], "|", row1[4], "|", row1[5], "|")
    print("+---+---+---+")
    print("|", row1[6], "|", row1[7], "|", row1[8], "|")
    print("+---+---+---+")
     
board()




def gamewinx():
    if row1[0] =="X" and row1[1] =="X" and row1[2] =="X":
        print("X wins")
        exit()
    elif row1[3] =="X" and row1[4] =="X" and row1[5] =="X":
        print("X wins")
        exit()
    elif row1[6] =="X" and row1[7] =="X" and row1[8] =="X":
        print("X wins")
        exit()
    elif row1[0] =="X" and row1[3] =="X" and row1[6] =="X":
        print("X wins")
        exit()
    elif row1[1] =="X" and row1[4] =="X" and row1[7] =="X":
        print("X wins")
        exit()
    elif row1[2] =="X" and row1[5] =="X" and row1[8] =="X":
        print("X wins")
        exit()
    elif row1[0] =="X" and row1[4] =="X" and row1[8] =="X":
        print("X wins")
        exit()
    elif row1[2] == "X" and row1[4] == "X" and row1[6] == "X":
        print("X wins")
        exit()

def gamewiny():
    if row1[0] =="o" and row1[1] =="o" and row1[2] =="o":
        print("o wins")
        exit()
    elif row1[3] =="o" and row1[4] =="o" and row1[5] =="o":
        print("o wins")
        exit()
    elif row1[6] =="o" and row1[7] =="o" and row1[8] =="o":
        print("o wins")
        exit()
    elif row1[0] =="o" and row1[3] =="o" and row1[6] =="o":
        print("o wins")
        exit()
    elif row1[1] =="o" and row1[4] =="o" and row1[7] =="o":
        print("o wins")
        exit()
    elif row1[2] =="o" and row1[5] =="o" and row1[8] =="o":
        print("o wins")
        exit()
    elif row1[0] =="o" and row1[4] =="o" and row1[8] =="o":
        print("o wins")
        exit()
    elif row1[2] == "o" and row1[4] == "o" and row1[6] == "o":
        print("o wins")
        exit()

def turnx():
    num = input("Where do you place x: ")
    check = num.isnumeric()
    if num == "1" or num == "2" or num == "3" or num == "4" or num == "5" or num == "6" or num == "7" or num == "8" or num == "9":
        check1=True
    else:
        check1=False
    while check == False or check1 == False:
        num = input("Please eneter a number from 1-9: ")
        check = num.isnumeric()
        if num == "1" or num == "2" or num == "3" or num == "4" or num == "5" or num == "6" or num == "7" or num == "8" or num == "9":
            check1=True
        else:
            check1=False
    num = int(num)
    return num




def change():
    num = turnx()
    if row1[num-1] == "o" or row1[num-1] == "X":
        print("o is already there")
        change()
    else:
        row1[num-1] = "X"






def ran():
  num3 = random.randint(0,9)
  return num3


def turny():
  num6 = ran()
  return num6



def change1():
    num3 = turny()
    if row1[num3-1] == "X" or row1[num3-1] == "o":
        change1()
    else:
        row1[num3-1] = "o"
   

num_turn=0
while num_turn <4:
    change()
    board()
    gamewinx()
    gamewiny()

    print("AI's turn")
    print("")
            
    change1()
    board()
    gamewinx()
    gamewiny()

    num_turn = num_turn + 1


change()
board()
gamewinx()
gamewiny()

print("tie")
exit()
