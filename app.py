from collections import Counter
import re

correct = "COMPLETE"
wrong = "NOT COMPLETE"
frequenciesList = []


def mahjong(hand):
    if validateChars(hand):
        if len(hand)==2 or ((len(hand)-2)%3==0):
            if len(hand)==2:
                return lenIsTwo(hand)
            else:
                return handleFrequencies(hand)
        else:
            frequenciesList.clear()
            return wrong
    frequenciesList.clear()
    return wrong


# accept only characters [0-9]
def validateChars(hand):
    pattern = re.compile(r'[0-9]+')
    if re.fullmatch(pattern, hand): #only works in Python3
        return True
    else:
        print("invalid characters")
        return False

#if there's a possibility of a pair with 0 triples, make sure the 2 characters are the same
def lenIsTwo(hand):
    if hand[0]==hand[1]:
        frequenciesList.clear()
        return correct
    else:
        frequenciesList.clear()
        return wrong

#check frequency of each character, store the frequencies in a global List
def handleFrequencies(hand):
    frequencies = Counter(hand) # Counter method of the collections class records number of occurences of each character. They're stored in a dict
    for i,j in frequencies.items():
        frequenciesList.append(j) #append only the 'values' of the dict to a list
    return final()

#check if 
def final():
    if 2 in frequenciesList: #there has to be a "PAIR" search for a frequency of 2
        freq = Counter(frequenciesList)
        if freq[2]==1: #if a "PAIR" occurs only once
            for i in range (len(frequenciesList)):
                if (frequenciesList[i]!=2 and frequenciesList[i]!=3): #if there's a frequency other than 2 or 3 
                    frequenciesList.clear()
                    return wrong
            frequenciesList.clear()
            return correct
        else:
            frequenciesList.clear()
            return wrong
    else:
        frequenciesList.clear()
        return wrong

print(mahjong('11222666999444777888'))