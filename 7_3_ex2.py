def f1(x,y):
    result = x*y
    if (result%2 ==0 and result%3 != 0):
        return 'two'
    elif(result%3==0 and result%2 != 0):
        return 'three'
    elif(result%2 ==0 and result%3 ==0):
        return 'all'
    else:
        return 'none'

while(1):
    num1 = int(input())
    if(num1 ==0):
        break
    num2 = int(input())
    print(f1(num1, num2))
