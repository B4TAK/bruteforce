#!/usr/bin/python
# coding=utf-8
import time
import os,sys
from forceFB import brute
os.system("clear")

def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk)) 
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk)) 

green = '\033[32;1m'

gta = '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
  #//Colors 
white = '\033[1;37m' # White 
red = '\033[31m' # red
orange = '\033[33m' # orange
blue = '\033[34m' # blue
p  = '\033[35m' # purple
C  = '\033[36m' # cyan

idgroup = []


idd = ("100022350489847")
duma = ("===========================================")
savefile = ("id.txt")
banner= C+blue+"""

 +=======================================i==+
 |..........   FACEBOOK BRUTE   ...........|
 +-----------------------------------------+
 |            AUTHOR : JHOSUA DZ           |
 |	       FACEBOOK CRACKER            |
 |          WHATSAPP : 082260032271        |
 +=========================================+
 |..........    FBBRUTE V1.2    ...........|
 +-----------------------------------------+\n\n
"""
print banner
me = (orange+'SELECT NUMBER =>> ')
oh= time.sleep(1)


class fbr:
 def __init__(self):
     oh
     print (red+'[ 1 ]'+green+' Start Attack')
     oh
     print (red+'[ 2 ]'+green+' Exit')
     time.sleep(2)
     print
     print
     self._check()




 def _check(self):
     try:
         inn = raw_input(me+(''))
         if(inn=='1'):
             print
             fbbrute.shit()
         elif(inn=='2'):
                 print
                 exit()
     except Exception as g:
          print          os.system('python2 fbr.py')
     else:
         return self.updown()
     
       
       

       
if __name__ == "__main__":
	fbr()
