#!/usr/bin/env python
# coding: utf-8

# # Q11:-Write a python program to find the factorial of a number

# In[10]:


#here I have used inside lib of python which is imported from math and got the factorial of a no.(n!=n*(n-1)*(n-2).....)

import math 

number = int(input(" Enter a number to find factorial : "))
if number < 0:    
   print(" Factorial does not exist for negative numbers") 
elif number == 0:    
   print("The factorial of 0 is 1")   
else: 
    fact = math.factorial(number)
    print("The factorial of %d  = %d" %(number, fact))


# # Q12. Write a python program to find whether a number is prime or composite.

# In[15]:


#if no. is greater the 1 then we can find prime no. by dividing "a no.".If after dividing we get reminder as 0 
#           then its not a prime.If reminder is not 0 then its prime.And to find reminder we use "modulus=%"

number = int(input("Enter a number: ")) 
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")
else:
    print(number, "is not a prime number")


# # Q13. Write a python program to check whether a given string is palindrome or not.

# In[19]:


#Enter any string and do opposite of it using[::-1]..example:-Madam=Madam.So its a palindrome

strName = input('Enter the String :')
oppName = strName[::-1]
if strName == oppName:
    print(strName,'is a palindromic')
else:
    print(strName,'is not palindromic')


# # Q14. Write a Python program to get the third side of right-angled triangle from two given sides.

# In[27]:


#here i have used formula hypo=sqrt((a**2 +b**2))
#and i have used float bcz we can have floating value also and converted that to 2 digit only

from math import sqrt
firstNum=float(input("Enter a first number:"))
secNum=float(input("Enter a second number:"))
hypotenuse  =sqrt(firstNum**2 + secNum**2)
thirdSide=round(hypotenuse, 2)
print("the third side of",firstNum ,"and",secNum,"is",thirdSide)


# # Q15. Write a python program to print the frequency of each of the characters present in a given string.

# In[34]:


#First we initialize string and then we count the string using object
#     of each element in string 

freqChar =  input('Enter the String :')
all_freq = {}
for i in freqChar:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
print ("The frequency of each of the characters in", freqChar,"is :\n "
                                        +  str(all_freq))


# In[ ]:




