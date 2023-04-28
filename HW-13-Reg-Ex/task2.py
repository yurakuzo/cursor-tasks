# Task 2 ################################################################
    
# Користувач вводить текст з клавіатури, і якесь слово, 
# треба порахувати скільки разів воно зустрічається в тексті 
# і замінити його на теж саме але з верхнім регістром

from re import subn

def foo(text, word):
    return subn(word, word.upper(), text)

text = "In the park, I saw a squirrel gathering nuts for the winter. \
The squirrel would quickly scurry up the tree, grab a nut,\
and then scurry back down to bury it in the ground.\
It was fascinating to watch the squirrel's quick movements as it\
repeated this process over and over again."
        
word = 'squirrel'

new_text, word_count = foo(text, word)

print(f"""
New text:\n{new_text}

Founded word '{word}' {word_count} times""")
