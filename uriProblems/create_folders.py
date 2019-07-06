import sys
import os
import pickle
import string

parent_dir = r'/Users/arjunbharadwaj/Documents/Programming-Challenges-Solutions/uriProblems'
with open('meta_data', 'rb') as handle:
  file_categories = pickle.load(handle)
  for category, problems in file_categories.items():
    problems = [s.replace('!','') for s in problems]
    if not os.path.exists(category):
      os.mkdir(category)
      os.chdir(category)
      for problem in problems:
        f = open(problem, 'w+')  # open file in append mode
        source_code = '''
        info = [int(x) for x in input().split()]
        print(info)
        '''
        f.write(source_code)
        f.close()
    
    os.chdir(parent_dir)


    