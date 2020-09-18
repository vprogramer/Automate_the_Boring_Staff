import os
import sys


# my directory
print(os.getcwd())
# path from parts for all systems
print(os.path.join('usr','bin','span'))
# change directory
os.chdir('/home/acervlad/PycharmProjects/Automate_the_Boring_Staff')
# create new directory
os.makedirs('/home/acervlad/PycharmProjects/Automate_the_Boring_Staff/new')
