# from functools import lru_cache
# import time
# @lru_cache(maxsize=None)
# def enterno(n):
#     time.sleep(5)
#     return n*5


# en=enterno(20)
# print("program run for 20")   
# en1=enterno(5)
# print("program run for 5")   
# en=enterno(20)
# print("program run for 20")   
# en1=enterno(5)
# print("program run for 5")   



import re
srch=r"[A-Z]+nimal"
text='''A cow is a friendly Animal that many people keep on farms.
Cows make a sound called “moo.”
Mnimal and or Cnimal
They have big bodies and are usually black, white, brown, or a mix of these colors.
Cows love to eat grass and hay.
They give us milk, which is used for making cheese and yogurt.
Milk from cows is good for our bones because it has calcium.
Cows also make manure, which helps plants grow better.
Some people make leather from the skin of cows for shoes and jackets.
Cows like to live together as friends in a group.
They are important to us for the many helpful things they provide.'''

founds=re.finditer(srch,text)
for f in founds:
    pass
    #print(f)
    #print(type(f.span()))
    print(text[f.span()[0]:f.span()[1]])
#print(text[f.span()[0]: f.span()[1]])