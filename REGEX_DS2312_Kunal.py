#!/usr/bin/env python
# coding: utf-8

# # Question 1- Write a Python program to replace all occurrences of a space, comma, or dot with a colon.
# Sample Text- 'Python Exercises, PHP exercises.'
# Expected Output: Python:Exercises::PHP:exercises:
# 

# In[12]:


import pandas as pd
import re
import regex as re
string1 = input ('Enter your text -')
x = re.sub('\W', ':', string1)
print(x)


# # Question 2-  Create a dataframe using the dictionary below and remove everything (commas (,), !, XXXX, ;, etc.) from the columns except words.
# Dictionary- {'SUMMARY' : ['hello, world!', 'XXXXX test', '123four, five:; six...']}
# Expected output-
# 0      hello world
# 1             test
# 2    four five six

# In[23]:


import pandas as pd
import re
import regex as re
patern = '\W'
Dictionary = {'SUMMARY' : ['hello, world!', 'XXXXX test', '123four', 'five :; six...']}
x = re.split ('\W', '\n', Dictionary)
print(x)


# # Question 3- Create a function in python to find all words that are at least 4 characters long in a string. The use of the re.compile() method is mandatory.
# 

# In[97]:


import pandas as pd
import re
import regex as re


Str_pattern = r'\b\w{4,}\b'
Str = input ('enter your text here - ')
regex_pattern = re.compile(Str_pattern)
print(type(regex_pattern))

result = regex_pattern.findall(Str)
print(result)


# In[ ]:





# # Question 4- Create a function in python to find all three, four, and five character words in a string. The use of the re.compile() method is mandatory

# In[100]:


import pandas as pd
import re
import regex as re

Str1 = input ('enter your text here - ')

Str1_pattern = r'\b\w{3,5}\b'
        
regex_pattern = re.compile(Str1_pattern)
print(type(regex_pattern))
    
result = regex_pattern.findall(Str1)
print(result)


# # Question 5- Create a function in Python to remove the parenthesis in a list of strings. The use of the re.compile() method is mandatory.
# Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
# 

# In[124]:


import pandas as pd
import re
import regex as re

Str2 = input ('Enter your text - ')
Str2_pattern = re.sub(r'\([^)]*\)', '',Str2) 
reg_pat = re.compile(Str2_pattern)
#print(type(reg_pat))
result = reg_pat.findall(Str2)
print(result)



# In[ ]:


# need to redo Q5


# # Question 6- Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression.
# Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]

# In[140]:


import regex as re

def no_parenth(string):
    pattern = (r'\([^)]*\)')
    strng =[re.sub(pattern, '',s) for s in string]
    return strng
string =  ['example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)']
strng = no_parenth(string)
for non_parenth in strng:
    print(non_parenth)
 


# In[ ]:





# # Question 7- Write a regular expression in Python to split a string into uppercase letters.
# Sample text: “ImportanceOfRegularExpressionsInPython”
# 

# In[146]:


import regex as re
Sample_text = 'ImportanceOfRegularExpressionsInPython'
x= re.split(r'(?=[A-Z])', Sample_text)
print(x)


# In[ ]:





# # Question 8- Create a function in python to insert spaces between words starting with numbers.
# Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
# 

# In[149]:


import regex as re
def insert_space(txt):
    output_txt = re.sub(r'(?=\d)',' ',txt)
    return output_txt
sample_text = 'RegularExpression1IsAn2ImportantTopic3InPython'
output_txt = insert_space(sample_text)
print(output_txt)


# In[ ]:





# # Question 9- Create a function in python to insert spaces between words starting with capital letters or with numbers.
# Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"

# In[151]:


import regex as re
def insert_space(txt):
    output_txt = re.sub(r'(?=\d)|(?=[A-Z])',' ',txt)
    return output_txt
sample_text = 'RegularExpression1IsAn2ImportantTopic3InPython'
output_txt = insert_space(sample_text)
print(output_txt)


# In[ ]:





# # Question 10- Use the github link below to read the data and create a dataframe. After creating the dataframe extract the first 6 letters of each country and store in the dataframe under a new column called first_five_letters.
# Github Link-  https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv

# In[ ]:


sorry


# In[ ]:





# # Question 11- Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.
# 

# In[ ]:


sorry


# # Question 12- Write a Python program where a string will start with a specific number. 
# 

# In[ ]:


sorry


# In[ ]:





# # Question 13- Write a Python program to remove leading zeros from an IP address
# 

# In[168]:


import regex as re
def remove_zeros(ip_address):
    components =ip_address.split('.')
    new_ip_address = [str(int(component)) for component in components]
    no_zero_ip_address = '.'.join(new_ip_address)
    return no_zero_ip_address

ip_addresses = ['192.168.000.101', '194.168.004.100', '001.002.003.004', '120.09.020.009', '005.006.007.008']

for ip_address in ip_addresses:
    cleaned = remove_zeros(ip_address)
    print (f'Original IP - {ip_address} After removing leading Zero -> {cleaned}')
    


# # Question 14- Write a regular expression in python to match a date string in the form of Month name followed by day number and year stored in a text file.
# 
# #Sample text :  ' On August 15th 1947 that India was declared independent from British colonialism, 
#                 #and the reins of control were handed over to the leaders of the Country’.
# #Expected Output- August 15th 1947
# #Note- Store given sample text in the text file and then extract the date string asked format.
# 

# In[ ]:





# # Question 15- Write a Python program to search some literals strings in a string. 
# #Sample text : 'The quick brown fox jumps over the lazy dog.'
# #Searched words : 'fox', 'dog', 'horse'
# 

# In[162]:


def search(text, searched):
    found = [word for word in searched if word in text]
    return found

sample_text = 'The quick brown fox jumps over the lazy dog.'
searched = ['fox', 'dog', 'horse']

found = search(sample_text, searched)

for word in found:
    print(f"'{word}' found in the given text.")


# # Question 16- Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs
# #Sample text : 'The quick brown fox jumps over the lazy dog.'
# #Searched words : 'fox'

# In[161]:


def literals_strng (sample_txt,finding):
    location = sample_txt.find(finding)
    return location
sample_txt = 'The quick brown fox jumps over the lazy dog'
finding = 'fox'

location =literals_strng(sample_txt,finding)

if location !=-1:
    print(f' "{finding}" found in the main string @ index {location}')
else: 
    print(f' "{finding}" not found in the main string')


# # Question 17- Write a Python program to find the substrings within a string.
# #Sample text : 'Python exercises, PHP exercises, C# exercises'
# #Pattern : 'exercises

# In[169]:


import regex as re
def find_substrng(text, pattern):
    found_index = []
    start = 0
    while True:
        index = text.find(pattern, start)
        if index == -1:
            break
        found_index.append(index)
        start = index + len(pattern)

    return found_index

sample_text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'

found_index = find_substrng(sample_text, pattern)

if found_index:
    print(f"'{pattern}' found in sample_teaxt at below positions:")
    for index in found_index:
        print(f"Position {index}")
else:
    print(f"'{pattern}' not found in the sample_text.")


# # Question 18- Write a Python program to find the occurrence and position of the substrings within a string.

# In[ ]:





# # Question 19- Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

# In[ ]:





# # Question 20- Create a function in python to find all decimal numbers with a precision of 1 or 2 in a string. The use of the re.compile() method is mandatory.
# Sample Text: "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
# Expected Output: ['01.12', '145.8', '3.01', '27.25', '0.25'] 

# In[ ]:





# # Question 21- Write a Python program to separate and print the numbers and their position of a given string.

# In[ ]:





# # Question 22- Write a regular expression in python program to extract maximum/largest numeric value from a string.
# Sample Text:  'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
# Expected Output: 950

# In[170]:


def top_mark(result):
    marks= re.findall(r'\b\d+\b', result)
    if marks:
        higher_mark = max(map(int, marks))
        return higher_mark
    else:
        return None
    
sample_text = 'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
higher_mark = top_mark(sample_text)

if higher_mark is not None:
    print(f'Highest mark is - {higher_mark}')


# # Question 23- Create a function in python to insert spaces between words starting with capital letters.
# #Sample Text: “RegularExpressionIsAnImportantTopicInPython"
# #Expected Output: Regular Expression Is An Important Topic In Python
# 

# In[159]:


import regex as re
def insert_space(txt):
    output_txt = re.sub(r'(?=[A-Z])',' ',txt)
    return output_txt
sample_text = 'RegularExpressionIsAnImportantTopicInPython'
output_txt = insert_space(sample_text)
print(output_txt)


# In[ ]:





# # Question 24- Python regex to find sequences of one upper case letter followed by lower case letters
# 

# In[177]:


import regex as re
def word_with_Capital(text):
    pattern = r'[A-Z][a-z]+'
    lower_case = re.findall(pattern, text)
    return lower_case

input_text = "I HaVe noT Tried hard Enough"

outcomes = word_with_Capital(input_text)
print("sequences of one upper case letter followed by lower case letters:")
print(outcomes)


# # Question 25- Write a Python program to remove continuous duplicate words from Sentence using Regular Expression.
# Sample Text: "Hello hello world world"
# Expected Output: Hello hello world
# 

# In[ ]:





# # Question 26-  Write a python program using RegEx to accept string ending with alphanumeric character.

# In[ ]:






# # Question 27-Write a python program using RegEx to extract the hashtags.
# Sample Text:  """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
# Expected Output: ['#Doltiwal', '#xyzabc', '#Demonetization']

# In[ ]:


import regex as re
def tagged_string{sample_text}
    result= re.findall(r'


# # Question 28- Write a python program using RegEx to remove <U+..> like symbols
# Check the below sample text, there are strange symbols something of the sort <U+..> all over the place. You need to come up with a general Regex expression that will cover all such symbols.
# Sample Text: "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
# 

# In[ ]:





# # Question 29- Write a python program to extract dates from the text stored in the text file.
# Sample Text: Ron was born on 12-09-1992 and he was admitted to school 15-12-1999.
# Note- Store this sample text in the file and then extract dates.

# In[ ]:





# # Question 30- Create a function in python to remove all words from a string of length between 2 and 4.
# #The use of the re.compile() method is mandatory.
# #Sample Text: "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
# #Expected Output:  following example creates ArrayList a capacity elements.

# In[ ]:




