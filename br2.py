import sys
import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = r"C:\Users\9 MAN\projects\automate project\chromedriver.exe"

repository = str(sys.argv[1])
print(repository)

driver = webdriver.Chrome(path)
driver.get("https://github.com/login")
Username = "UserName"
Password = "*******"

Uname_xpath = 'login_field'
Uname_element = driver.find_element_by_id(Uname_xpath)
Uname_element.send_keys(Username)

Password_xpath = 'password'
Password_element = driver.find_element_by_id(Password_xpath)
Password_element.send_keys(Password)
Password_element.send_keys(Keys.RETURN)

driver.get('https://github.com/new')
repository_xpath = 'repository_name'
repository_element = driver.find_element_by_id(repository_xpath)
repository_element.send_keys(repository)
time.sleep(5)
repository_element.send_keys(Keys.RETURN)
os.chdir(repository)
command = f'git remote add origin https://github.com/{Username}/{repository}.git'
push = 'git push -u origin master'

os.system(command)
os.system(push)
time.sleep(30)
print("All set to go ")
