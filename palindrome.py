# -*- coding: utf-8 -*-
"""
Created on Wed May 12 19:14:18 2021
checking a string is pallindrome or not
@author: Saikat Datta
"""

s=input()
j=len(s)-1
i=0
flag=0
while(i<j):
    if(s[i]!=s[j]):
        flag=1
        break
    else:
        i+=1
        j-=1
if(flag==0):
    print("pallindrome")
else:
    print("not pallindrome")        
© 2021 GitHub, Inc.
