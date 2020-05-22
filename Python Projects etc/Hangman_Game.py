import random
import os
import subprocess

def clear():
    os.system('cls')
    subprocess.call("cls", shell=True)

def main():
        tries = 6
        print("Let's play a game of hangman!")
        words = ["hamster","shoal","radical","crooked","elephant","steamboat","forlorn"]
        word = random.choice(words)
        word_bkp = word
        word = list(word)
        word_blot = ["*" for x in word]

        while word_bkp != "".join(word_blot) and tries != 0:
                print("Tries Left: " + str(tries))
                print("".join(word_blot))
                inp = input("Which letter will you choose: ")
                for x in word:
                        if inp == x:
                                word_blot[word.index(x)] = x
                                word[word.index(x)] = "*"
                                tries += 1
                tries -= 1
                
        if word_bkp == "".join(word_blot):
                print("Congratulations! You found the word!")
                print("".join(word_blot))
        else:
                print("You Lose")
        
main()
