import random as rand
print('Stone-----Paper-----Sissor')
n1=input('Enter the name of the player1: ')
n2=input('Enter the name of the player2: ')
p1=0
p2=0
t=0
n=int(input('Enter number of chances: '))
A=['stone','paper','scissor']
for i in range(n):
    x=rand.randint(0,2)
    y=rand.randint(0,2)
    print('P1: ',A[x],' P2: ',A[y])
    if(((A[x]=='stone') and (A[y]=='scissor')) or ((A[x]=='scissor') and (A[y]=='paper')) or((A[x]=='paper') and (A[y]=='stone'))):
       p1=p1+1
       print('P1 got point')
    elif(((A[y]=='stone') and (A[x]=='scissor')) or ((A[y]=='scissor') and (A[x]=='paper')) or ((A[y]=='paper') and (A[x]=='stone'))):
        p2=p2+1
        print('P2 got point')
    else:
        t=t+1
if(p1>p2):
    print(n1,' won')
elif(p2>p1):
    print(n2,' won')
else:
    print('Tie')
print('Points: P1:',p1,' P2: ',p2,' Tie: ',t)
print('Game End')
