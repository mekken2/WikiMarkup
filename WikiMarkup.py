#! python3
# WikiMarkup.py - Add bullet point before lines in editing Wiki Article

import pyperclip

text = pyperclip.paste()

#Separate lines and add stars
lines = text.split('\n')

#Loop through all indexes in the "lines" list
#Add star to each string in "lines" list
for i in range(len(lines)):
    lines[i] = '* '+lines[i] 

text = '\n'.join(lines)
pyperclip.copy(text)