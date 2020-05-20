import os
import random
import subprocess

def clear():
    os.system('cls')
    subprocess.call("cls", shell=True)

    
print("Do you want to play a game of dice? [yes/no]:")

inp1 = " "

while inp1 != "yes":
    inp1 = input("Your Answer: ")
    
    if inp1 == "yes":
        clear()
        while inp1 == "yes":
            dv = ["1","2","3","4","5","6"]
            x = random.choice(dv)
            print("Choose a number that you think will appear: ")
            bet = input("Your choice: ") 
            print("The number rolled is: " + x)
            inp3 = " "
            
            while inp3 != "yes" and inp3 != "no":
                print("Would you like to try again? [yes/no]:")
                inp3 = input("Your choice: ")
                
                if inp3 == "yes":
                    clear()
                    break
                
                elif inp3 == "no":
                    exit()
                    
                else:
                    clear()
                    print("I'm sorry, I don't understand")
                    continue
            
    elif inp == "no":
        exit()
    else:
        print("I'm sorry, I don't understand")
        continue

