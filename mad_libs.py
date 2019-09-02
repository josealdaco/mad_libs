#import nltk
#import random
#nltk.download('wordnet')
#from nltk.corpus import wordne
import random
from string import punctuation # link of library name:https://stackoverflow.com/questions/28056843/special-characters-in-string-literals
import webbrowser # Library found from stackOverFlow, link:https://stackoverflow.com/questions/4302027/how-to-open-a-url-in-python user:aaronasterling
from colorama import Fore, Back, Style

check = False
color_choice = []
arr = []
validation = set(punctuation)
print(validation)
validation.discard("'") # this could be used in a name
print(validation)

dic = {"BLACK": Fore.BLACK, "RED": Fore.RED, "GREEN": Fore.GREEN, "YELLOW": Fore.YELLOW, "BLUE": Fore.BLUE, "MAGENTA": Fore.MAGENTA, "CYAN": Fore.CYAN, "WHITE": Fore.WHITE}
key = "WHITE"
list3 = []

file = open("words.txt", "r")
for line in file:
    x = line.split(",")
    b = x[0]
    c = len(b)-1
    b = b[0:c]
    list3.append(b)
print(len(list3)) # file has x amount of usable words
while(check is False):




    if len(color_choice) != 0:
        key = color_choice[len(color_choice) - 1]
        print(key)
        print(dic.get(key, "WHITE") + "Today we will talk about [Noun] who is [Adjective] living with [Noun].\n Being together has been a positive impact on their [Verb]\n")
    print(dic.get(key, "WHITE") + " Today we will talk about [Noun] who is [Adjective] living with [Noun].\n Being together has been a positive impact on their [Verb]\n")
    x = input(dic.get(key, "WHITE") + "If you try adding less words it will be replaced with defaults\n, no more then 4 words will be used:\n If you also wish to fill out the missing parts with random words from our files you may do so by pressing the R button:\n")
    words = []
    new_word = []
    index = []
    sentence = ["walking", "across", "swim", "San Francisco", "California", "Bay Area", "Riding", "bike", "run", "house", "pick", "change", "unlock", "love", "girlfriend"]
    if(x == "r" or x == "R"):
        for n in range(0, 4):
            new_word.append(list3[random.randint(0, len(list3))])
    else:
        def clense(y): #seperates words into individual strings
            word = ""
            l = []
            for x in range(0, len(y)):
                if(y[x] != " "):
                    l.append(y[x])
                elif(y[x] == " " and y[x-1] != "."):
                    l.append("|")
            for j in range(0, len(l)):
                if(l[j] != "|"):
                    word += l[j]
                    print(l[j])
                elif(l[j] == "|"):
                    words.append(word)
                    word = ""
            words.append(word)
            g = 0
            for x in words:   #Second filter until I fix first or use .pop() 8/29/19
                if x == "":
                    print("detected")
                else:
                    new_word.append(x)
                g += 1
            print(new_word)
            return new_word
        def validate(filter, x):
            for y in filter(x):
                for j in range(0, len(y)):
                    for l in validation:
                        if(y[j] == l):
                            print("WORD CANNOT CONTAIN SPECIAL CHARACTERS")
                            print(y)
                            index.append(y)
        def remove():

            for x in index:
                for y in new_word:
                    if(x == y):
                        new_word.pop(new_word.index(x))
                        print("REMOVED")

    validate(clense, x)
    remove()

    print("THE ENTIRE LIST:", new_word)
    userWords = len(new_word)
    pcWords = len(sentence)
    greater = 0
    least = 0
    if(pcWords > userWords):
        greater = pcWords
        least = userWords
    else:
        greater = userWords
        least = pcWords
    value = []
    if(userWords >= 4):
        for x in range(0, 4):
            value.append(new_word[x])
    else:
        mark = len(new_word)
        for x in range(mark, 4):
            new_word.append(None)
        for x in new_word:
            value.append(x)
    for x in value:
        if(x is None):
            x = "NULL"
    val = value[0]
    val2 = value[1] #Adjective
    val3 = value[2]
    val4 = value[3] #Verb
    #Randomising nouns

    for x in range(0, random.randint(1, len(value))):
        rand = random.randint(0, 2)
        rand2 = random.randint(0, 2)
        if(rand != 1 and rand != rand2 and rand2 != 1):
            val = value[rand]
            val3 = value[rand2]

    sentence_choice = dic.get(key, "WHITE") + f""" Today we will talk about {val} who is {val2} living with {val3}.\n Being together has been a positive impact on their {val4}"""
# for x in range(0,random.randint(0,greater)):
# sentence_choice += sentence[random.randint(0,len#(sentence) - 1)] + " " +  words[random.randint(0,len(words)# - 1)].upper() + " "
    print(sentence_choice)
    choose = False
    choose2 = True
    while(choose == False):
        print(dic.get(key, "WHITE") + """ TYPE S TO STOP, TYPE R TO RESTART PROGRAM, TYPE C FOR COLOR TERMINAL, W FOR WEBPAGE OR D FOR DEFAULT SETTINGS,   \n IF YOU CHOOSE D THIS WILL PROMPT AGAIN\n """)
        an = input().upper()
        print(an)
        if an == 'S':
            check = True
            choose = True
        elif an == 'R':
            print(dic.get(key, "WHITE") + "restarting")
            choose = True
        elif an == 'C':
            choose = True
            choose2 = False
        elif an == 'D':
            key = "WHITE"
        elif an == 'W':
            webbrowser.open_new_tab('http://box5377.temp.domains/~shapesur/madlibs/character_resume.html') # Online Custom ad_libs website
        else:
            print("YOU DID NOT TYPE ANYTHING OR ANYTHING RELEVANT, NONE CASE SENSTITIVE")
        while(choose2 is False):
            color = input(dic.get(key, "WHITE") + """Type desired color story text, the list consit of:\n BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE \n""").upper()
            if color == "BLACK":
                color_choice.append(color)
                choose2 = True
            elif color == "RED":
                color_choice.append(color)
                choose2 = True
            elif color == "GREEN":
                color_choice.append(color)
                choose2 = True
            elif color == "YELLOW":
                color_choice.append(color)
                choose2 = True
            elif color == "BLUE":
                color_choice.append(color)
                choose2 = True
            elif color == "MAGENTA":
                color_choice.append(color)
                choose2 = True
            elif color == "CYAN":
                color_choice.append(color)
                choose2 = True
            elif color == "WHITE":
                color_choice.append(color)
                choose2 = True
            else:
                print(dic.get(key, "WHITE") + "YOU DID NOT CHOOOSE!!, \n", """ TYPE S TO STOP, TYPE R TO RESTART PROGRAM, TYPE C FOR COLOR TERMINAL OR D for default settings\n  """)
#if not wordnet.synsets("patrick"):
#    print("not a word")
#else:
#    print("word")
