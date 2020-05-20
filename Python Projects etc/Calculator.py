import os
import subprocess

# Initialize first number variable
cur_num = 0

def clear():
    os.system('cls')
    subprocess.call("cls", shell=True)
    
def menu():
    print('0: Set First Value')
    print('1: Addition')
    print('2: subtraction')
    print('3: Multiplication')
    print('4: Division')
    

def add(x,y):
    global cur_num
    cur_num = x+y
    return cur_num

def subtract(x,y):
    global cur_num
    cur_num = x-y
    return cur_num

def multiply(x,y):
    global cur_num
    cur_num = x*y
    return cur_num

def divide(x,y):
    global cur_num
    cur_num = x/y
    return cur_num

class switch(object):
        def calc(object,i):
                proc_name='proc'+str(i)
                x=getattr(object,proc_name,lambda:'Invalid')
                return x()
        def proc0(self):
                print('Choose a starting number for calculation.')
                global cur_num 
                cur_num = float(input('#: '))
        def proc1(self):
                print('Choose a number for the addition process:')
                var1 = cur_num
                var2 = float(input('#: '))
                print(add(var1,var2))
        def proc2(self):
                print('Choose a number for the subtraction process:')
                var1 = cur_num
                var2 = float(input('#: '))
                print(subtract(var1,var2))
                
        def proc3(self):
                print('Choose a number for the multiplication process:')
                var1 = cur_num
                var2 = float(input('#: '))
                print(multiply(var1,var2))
                
        def proc4(self):
                print('Choose a number for the division process:')
                var1 = cur_num
                var2 = float(input('#: '))
                print(divide(var1,var2))

s=switch()

def main():

    print('What type of calculation will you be doing? (Choose by number)')
    print('Current Number: ' + str(cur_num))
    menu()
    c = input("Choice: ")
    clear()
    
    s.calc(c);

    clear()
    main()


if __name__=="__main__":
    main()
