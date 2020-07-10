import sys
import os
import csv
from github import Github

foldername = str(sys.argv[1])
os.makedirs(foldername) 

os.chdir(foldername)
print("\nCurrent Working Directory " , os.getcwd())

f= open("README.md","w+")
for i in range(1):
     f.write("This is initial readme file with git automated project" )
f.close()
	
f= open("LICENSE.md","w+")
for i in range(1):
     f.write("This is initial LICENCE  file with git automated project")
f.close()


try:
          	# performing git bash actions
    os.system('git init')
    os.system(f'echo "# {foldername}" >> README.md')
    os.system(f'echo "# {foldername}" >> License.md')
    os.system('git add .')
    os.system('git commit -m "first commit"')
	
    print("Directory " , foldername ,  " Created ")
except FileExistsError:
    print("Directory " , foldername ,  " already exists")







