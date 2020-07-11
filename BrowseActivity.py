import sys
import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
pat = os.getcwd()
path = f' {pat}\chromedriver.exe'
repository = str(sys.argv[1])
print(path)