# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 14:30:49 2023

@author: ninae
""" 
'''
numb = 1
while numb <= 5:
    print('hej')
    numb += 1
    
for i in range(5):
    print('hej')
   
    
password = input('Skriv lösenordet ')

if password == 'Nina':
    print('Välkommen')
else:
    print('Fel lösenord')
   

print('Det görs först....')
print('...sen det här...')
print('..och sist det här')
'''
a = int(input('Skriv en siffra mellan 1 och 7 '))
b = int(input('Skriv en siffra mellan 1 och 9 '))
print('')
  

if a < 6 and b > 7:
    print('Nina är bäst')
elif a == b or a<3:
    print('Jag gillar python')
else:
    print('fel')
    


