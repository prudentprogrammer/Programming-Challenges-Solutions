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
python_stub_code = '''
# Link: 
# Solution to be filled out and attempted.
test_cases = int(input())
for _ in range(test_cases):
  pass
'''.strip()

java_source_code = '''
import java.io.*;
import java.util.*;
import java.util.stream.*;

class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());
    // Code to be filled out here.
  }
}
'''.strip()

res = {'Python': [], 'Java': [] }

for problem in problem_objs:
  file_name = '{} - {}'.format(problem[1], problem[2])
  res['Python'].append( { 'name' : file_name + '.py', 'source_code': python_stub_code} )
  res['Java'].append( { 'name' : file_name + '.java', 'source_code': java_source_code} )

#pprint.pprint(res)

parent_dir = os.getcwd()
for ind, sol_type in enumerate(['Python Solutions', 'Java Solutions']):
  folder_name = os.path.join(parent_dir, 'UVA Problems/{}'.format(sol_type))
  if os.path.exists(folder_name):
    shutil.rmtree(folder_name)
  
  os.mkdir(folder_name)
  os.chdir(folder_name)

  curr_key_folder_type = 'Python' if ind == 0 else 'Java'
  for problem_obj in res[curr_key_folder_type]:
      file_name = problem_obj['name'].replace('!','').replace(r'/','')
      f = open(file_name, 'w+')  # open file in append mode
      f.write(problem_obj['source_code'])
      f.close()
  os.chdir(parent_dir)
