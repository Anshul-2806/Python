a = int(input('Enter one side'))
b = int(input('Enter one side'))
c = int(input('Enter one side'))

if(a==b or b==c):
    print('An Equilateral traingle')
elif(a==b or b==c or c==a):
    print('An Isoscles traingle')
else:
    print('A Scalane traingle')