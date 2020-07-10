import sys
import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = r"C:\Users\9 MAN\projects\automate project\chromedriver.exe"
dirpath = os.getcwd()
path = f' {dirpath}\chromedriver.exe'
print(path)

repository = str(sys.argv[1])
print(repository)
