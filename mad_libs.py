#import nltk
#import random
#nltk.download('wordnet')
#from nltk.corpus import wordnet
x = input("list adj words")
words = []
sentence = ["walking", "across", "swim", "San Francisco", "California", "Bay Area", "Riding", "bike", "run", "house", "pick", "change", "unlock", "love", "girlfriend"]
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
        elif(l[j] == "|"):
            words.append(word)
            word = ""
    words.append(word)
clense(x)

print(words)
userWords = len(words)
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
if(userWords >= 3):
    for x in range(0, 3):
        value.append(words[x])
else:
    mark = len(words)
    for x in range(mark, 3):
        words.append(None)
    for x in words:
        value.append(x)
for x in value:
    if(x is None):
        x = "NULL"
val = value[0]
val2 = value[1]
val3 = value[2]

sentence_choice = f""" Today we will talk about {val} who is currently living with {val2}.\n Being together has been a positive impact on their {val3}"""
# for x in range(0,random.randint(0,greater)):
# sentence_choice += sentence[random.randint(0,len#(sentence) - 1)] + " " +  words[random.randint(0,len(words)# - 1)].upper() + " "

print(sentence_choice)
#if not wordnet.synsets("patrick"):
#    print("not a word")
#else:
#    print("word")
