import sys
import random

#!/usr/bin/python

def checkInput(length,lowerCase,upperCase,numbers,symbols):
    if length <= 0:
        print("The length argument must be greater than 0");
        return -1;
    if lowerCase not in ["True","False"]:
        print("The lowerCase argument must be True or False");
        return -1;
    if upperCase not in ["True","False"]:
        print("The upperCase argument must be True or False");
        return -1;
    if numbers not in ["True","False"]:
        print("The numbers argument must be True or False");
        return -1;
    if symbols not in ["True","False"]:
        print("The symbols argument must be True or False");
        return -1;

def generate(length,lowerCase,upperCase,numbers,symbols):
    finalList = [];
    password = "";

    if lowerCase == "True":
        for character in range(97,123):
            finalList.append(chr(character));
    if upperCase == "True":
        for character in range(65,91):
            finalList.append(chr(character));
    if numbers == "True":
        for character in range(48,58):
            finalList.append(chr(character));
    if symbols == "True":
        symbolList = ["!","#","$","%","&","'","(",")","*","+",",","-",".","/",":",";","<","=",
                      ">","?","@","[","]","^","_","{","|","}","~"];
        for character in symbolList:
            finalList.append(character);
            
    if not finalList:
        print("Your password must contain something (you inserted False everywhere)")
        return -1

    random.shuffle(finalList);
    
    for i in range(length):
        index = random.randint(0,len(finalList)-1);
        password += finalList[index];

    print("The generated password is :");
    print(password);


if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("The arguments must be excatly 6");
    else:
        if checkInput(int(sys.argv[1]),sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5]) != -1 :
            generate(int(sys.argv[1]),sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5]);
    
