# -*- coding: utf-8 -*-
"""
@author: Ritesh Rajput | riteshrajput381@gmail.com
This script is used to structur the text obtained from voter id, it is saved in result.json file 
"""

# Libraries
import json
import re

# Open and reading the textfile containing result
filename = open('TextExtract.txt', 'r')
text = filename.read()

text1 = []

# Splitting the lines to sort the text paragraph wise
lines = text.split('\n')
for lin in lines:
    s = lin.strip()
    s = s.rstrip()
    s = s.lstrip()
    text1.append(s)

# Using regex to find the neceesary information
def findword(textlist, wordstring):
    lineno = -1
    for wordline in textlist:
        xx = wordline.split()
        if ([w for w in xx if re.search(wordstring, w)]):
            lineno = textlist.index(wordline)
            textlist = textlist[lineno+1:]
            return textlist
    return textlist

# Finding the electors number 
voter_no = findword(text1, '(ELECTION COMMISSION OF INDIA IDENTITY CARD|CARD|IDENTITY CARD)$')
voter_no = voter_no[0]
epic_no = voter_no.replace(" ", "")
print('\n')
print('Epic No:',epic_no)

# Some voter id's last name is printed on next line hence, it will extract from next line
find_word = "(Elector's Name|NAME|Name)$"
name_end = findword(text1, find_word)
endname = name_end[0]

lines = text
for x in lines.split('\n'):
    _ = x.split()
    if ([w for w in _ if re.search("(Elector's Name|ELECTOR'S NAME|NAME|Name|name)$", w)]):
        person_name = x
        person_name = person_name.split(':')[1].strip()
        
        # If voter id's endname is on next line it will join it
        if endname:
            print("Elector's Name:",person_name + ' ' + endname)
            full_name = person_name + ' ' + endname
        else:
            print(person_name)
            full_name = person_name

    # Finding the father/husband/mother name        
    if ([w for w in _ if re.search("(Father's|Mother's|Husband's)$", w)]):
        elder_name = x
        elder_name = elder_name.split(':')[1].strip()
        print("Father's Name:",elder_name)
        
    # Finding the gender of the electoral candidate    
    if ([w for w in _ if re.search('(sex|SEX|Sex)$', w)]):
        gender = x
        gender = gender.split('/')
        sex = ''.join(gender[2]).strip()
        print('Sex:',sex)
    
    # Finding the Date of Birth 
    if ([w for w in _ if re.search('(Year|Birth|Date of Birth|DATE OF BIRTH|DOB)$', w)]):
        year = x
        year = year.split(':')
        dob = ''.join(year[1:]).strip()
        print('Date of Birth:',dob)

# Converting the extracted informaton into json
di = {'Epic No':epic_no,
      'Elector Name':full_name,
      'Father Name':elder_name,
      'Sex':sex,
      'Date of Birth':dob}

# Saving the json file
print('\n',di)
with open('Result.json', 'w') as fp:
    json.dump(di, fp, sort_keys=True, indent=4)