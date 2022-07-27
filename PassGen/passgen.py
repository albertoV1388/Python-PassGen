# Python Password Generator
# PassGen V0.0.1 Alpha
from pkgutil import ImpImporter
from traceback import print_tb
from turtle import position
from termcolor import colored
from colorama import init, Fore, Back, Style
import variables
import time
import string
import random
def warning():
    print(Fore.RED + "This tool has been created for educational purposes,\n I am not responsible for any damage caused by it.\nUse it at your own risk \nYou agree to make good use of this tool")
    risk = input("Are You agree? (y/n):")
    print(risk)
    if risk == "y":{
    print(Fore.WHITE + "Password Generation Options:\n\t1) Birth Dates\t2) Bruteforce!!\t3) More... ")
    }
    else:
        if risk == "n":
            print("Closing")
            quit()
        
def choose():
    opcion = int(input("Enter Option: "))
    print(opcion)
    if opcion == 1:
        print("Birth Dates \nEnter Icon of Date, (Leave Blank if not use)");
        datepass()
        
    else:
        if opcion == 2:
            print("Bruteforce!!")
            bruteforce()
        else:
            if opcion == 3:{
                print("Created by @albertoV1388\n\t Made as a personal project to improve my Python 3 skills\n\t Github: https://github.com/albertoV1388\n\t Twitter: https://twitter.com/Alberto44631563")
            }
            quit()
        
def datepass():
    icon1 = input("Enter Icon: ")
    print(icon1)
    print("You are selected: " + icon1)
    year = int(input("Enter year: "))
    print("Generating...")
    time.sleep(5)
    for i in range(year+1):
        for u in range(13):
            for e in range(32):
                print(e,icon1,u,icon1,i)
    print("Passwords Generated!!")
    quit()


def bruteforce():
    print(variables.titlebruteforce)
    print("\n\tEnter Option:\n\t1) Numbers\n\t2) Alfanumeric digits")
    bruteforcingoption = int(input("\n\tEnter Option: "))
    print(bruteforcingoption)
    if bruteforcingoption == 1:
            print("\n\tNumbers")
            numberpass()
    else:
        if bruteforcingoption == 2:
            print("\n\tAlfanumeric digits")
            number_of_strings = int(input("Enter quantity of passwords to Gen: "))
            length_of_string = int(input("Enter password length: "))
            generatedpasswords = open("Passwords.txt", "w")
            print(number_of_strings)
            print(length_of_string)
            print("Generating...")
            time.sleep(5)
            for x in range(number_of_strings):
                generatedpasswords.write(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))
                generatedpasswords.write("\n")
            print("Number of passwords generated: ", x+1)
            print("Passwords Generated!!")
            print("The passwords are save on Passwords.txt")
            quit()
            
def numberpass():
    number_of_strings = int(input("Enter quantity of passwords to Gen: "))
    length_of_string = int(input("Enter password length: "))
    generatedpasswords = open("Passwords.txt", "w")
    for x in range(number_of_strings):
            generatedpasswords.write(''.join(random.choice(string.digits) for _ in range(length_of_string)))
            generatedpasswords.write("\n")
    print("Number of passwords generated: ", x+1)
    print("Passwords Generated!!")
    print("The passwords are save on Passwords.txt")
    quit()
    
