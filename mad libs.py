import sys
import re

# Choosing a number to show a sentence
number = input('Please pick a number from 1 to 10: ')
number = number + ' '

# Cheking if input is valid
try:
    num = int(number)
    print("So, you choosed", num)
except:
    print("That's not a number!")
if num > 10 or num < 1:
    sys.exit("Sorry, not in range!")

# Searching and printing the choosed sentence
fh = open('F:\py4e\hh\mad_libz\senteces.txt')
for line in fh:
    if number in line:
        sentence = line[2:]

print("Complete the missing words:")
print(sentence)

# Searching for the missing spaces
blanks = re.findall("_+",sentence)

# Entering your words in the sentence
for i in blanks:
    word = input('Enter your word: ')
    s1 = re.sub("_+", word, sentence, 1)
    sentence = s1

# printing the final result
print(s1)
