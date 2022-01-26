#below 3 lines must be modified as needed
file_filter = '*.txt'
source_dirs = 'D:/src1/'
destination_dir = 'D:/dest/'

#actual script to copy the files
from pathlib import Path
import shutil
import os

print('Copying files...')
for sd in source_dirs.split(';'):
    for d in Path(sd).rglob(file_filter):
        print(d)
        _, fn = os.path.split(d)
        if not os.path.isfile(destination_dir + fn):
            shutil.copyfile(d, destination_dir + fn)
        else:
            print('skipping, already exists on destination folder: ' + fn)
print('Done')