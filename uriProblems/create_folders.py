import sys
import os
import pickle
import string
import shutil

parent_dir = r'/Users/arjunbharadwaj/Documents/Programming-Challenges-Solutions/uriProblems'
with open('meta_data', 'rb') as handle:
  file_categories = pickle.load(handle)
  for category, problems in file_categories.items():
    print(category)
    problems = [s.replace('!','').replace(r'/','') for s in problems]
    if os.path.exists(category):
      shutil.rmtree(category)
    else:
      os.mkdir(category)
      os.chdir(category)
      for problem in problems:
        f = open(problem, 'w+')  # open file in append mode
        source_code = 'info = [int(x) for x in input().split()]\nprint(info)'
        f.write(source_code)
        f.close()
    os.chdir(parent_dir)


    