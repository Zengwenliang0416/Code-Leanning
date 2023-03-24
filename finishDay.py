import os
import sys

a,b,n=map(int,input().split())
sum=5*a+2*b
week=n//sum
day=week*7
n=n-week*sum
for i in range(5):
    if n>0:
        n=n-a
        day += 1
for j in range(2):
    if n>0:
        n=n-b
        day += 1
print(day)
