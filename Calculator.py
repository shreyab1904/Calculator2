def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mult(x,y):
    return x*y

def divide(x,y):
    return x/y

if __name__=="__main__":
    num1=float(input("enter number 1:  "));
    num2=float(input("enter number 2:  " ));
    result=add(num1,num2)
    print(result)
    result=sub(num1,num2)
    print(result)
    result=mult(num1,num2)
    print(result)
    result=divide(num1,num2)
    print(result)