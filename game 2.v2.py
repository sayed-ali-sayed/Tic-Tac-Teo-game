import sys
board=['a','b','c','d','e','f','g','h','i']
chek=[100,100,100,100,100,100,100,100,100]#array to chek if numbers=15
nums=[]#numbers already taken
def showboard():
    print(board[0],'|',board[1],'|',board[2])
    print('---------')
    print(board[3],'|',board[4],'|',board[5])
    print('---------')
    print(board[6],'|',board[7],'|',board[8])
    print('---------')
showboard()
Rounds=1

def write(a,b):
    board[a]=b
    showboard()
while True:
    if Rounds%2==1:
        print('player 1:')
        a=int(input('Enter The Location'))
        while a<0 or a>8 or board[a]==0 or board[a]==1 or board[a]==2 or board[a]==3 or board[a]==4 or board[a]==5 or board[a]==6 or board[a]==7 or board[a]==8:
            if a<0 or a>8:
                print('Enter a number from 0 to 8')
                a=int(input('Enter The Location'))
            elif board[a]==0 or board[a]==1 or board[a]==2 or board[a]==3 or board[a]==4 or board[a]==5 or board[a]==6 or board[a]==7 or board[a]==8:
                print('This Location is Alerady Occupied')
                a=int(input('Enter The Location'))
        b=int(input('Enter A Number'))
        i=0
        while b<0 or b>9 or b%2==0 or i<Rounds-1:
            if b<0 or b>9 or b%2==0:
                print('Enter an odd number from 0 to 9')
                b=int(input('Enter A Number'))
            elif nums[i]==b:
                print('This Number is Alerady Taken')
                b=int(input('Enter A Number'))
                i=0
            else:
                i+=1
        write(a,b)
        chek[a]=b
        nums.append(b)
        if (chek[0]+chek[1]+chek[2])==15 or(chek[3]+chek[4]+chek[5])==15 or(chek[6]+chek[7]+chek[8])==15 or(chek[0]+chek[3]+chek[6])==15 or(chek[1]+chek[4]+chek[7])==15 or(chek[2]+chek[5]+chek[8])==15 or(chek[2]+chek[4]+chek[6])==15 or(chek[0]+chek[4]+chek[8])==15:
             print('Congratulations Player 1 You Have Won')
             sys.exit()
             break
    else:
        print('player 2:')
        a=int(input('Enter The Location'))
        while a<0 or a>8 or board[a]==0 or board[a]==1 or board[a]==2 or board[a]==3 or board[a]==4 or board[a]==5 or board[a]==6 or board[a]==7 or board[a]==8:
            if a<0 or a>8:
                print('Enter a number from 0 to 8')
                a=int(input('Enter The Location'))
            elif board[a]==0 or board[a]==1 or board[a]==2 or board[a]==3 or board[a]==4 or board[a]==5 or board[a]==6 or board[a]==7 or board[a]==8:
                print('This Location is Alerady Occupied')
                a=int(input('Enter The Location'))
        b=int(input('Enter A Number'))
        i=0
        while b<0 or b>9 or b%2==1 or i<Rounds-1:
            if b<0 or b>9 or b%2==1:
                print('Enter an even number from 0 to 9')
                b=int(input('Enter A Number'))
            elif nums[i]==b:
                print('This Number is Alerady Taken')
                b=int(input('Enter A Number'))
                i=0
            else:
                i+=1
        write(a,b)
        chek[a]=b
        nums.append(b)
        if (chek[0]+chek[1]+chek[2])==15 or(chek[3]+chek[4]+chek[5])==15 or(chek[6]+chek[7]+chek[8])==15 or(chek[0]+chek[3]+chek[6])==15 or(chek[1]+chek[4]+chek[7])==15 or(chek[2]+chek[5]+chek[8])==15 or(chek[2]+chek[4]+chek[6])==15 or(chek[0]+chek[4]+chek[8])==15:
              print('Congratulations Player 2 You Have Won')
              sys.exit()
              break
    Rounds+=1
    if Rounds==10:
        print('Game over')
        sys.exit()
