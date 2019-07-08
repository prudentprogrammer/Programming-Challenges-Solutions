# importing the requests library
import requests
import pprint
import os
import shutil

# api-endpoint
URL = "https://uhunt.onlinejudge.org/api/p"

# sending get request and saving the response as response object
r = requests.get(URL)

# extracting data in json format
problem_objs = r.json()
res = []
for problem in problem_objs:
    res.append('{} - {}.py'.format(problem[1], problem[2]))

parent_dir = os.getcwd()
folder_name = os.path.join(parent_dir, 'UVA Problems')
if os.path.exists(folder_name):
  shutil.rmtree(folder_name)
else:
  os.mkdir(folder_name)

os.chdir(folder_name)

for filename in res:
    filename = filename.replace('!','').replace(r'/','')
    f = open(filename, 'w+')  # open file in append mode
    source_code = '# Link: \n# Solution is yet to be filled and updated\nfor _ in range(int(input())):\n  pass'
    f.write(source_code)
    f.close()
os.chdir(parent_dir)
