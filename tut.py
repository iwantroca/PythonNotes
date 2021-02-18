import os 
from datetime import datetime

print(os.getcwd())

print(os.listdir())

# mod_time = os.stat('pgm.py').st_mtime
# print(datetime.fromtimestamp(mod_time)) 

for dirpath, dirname, filename in os.walk('.'):
    print('Current Path: ', dirpath)
    print('Directories: ', dirname)
    print('Files: ', filename)
    print()