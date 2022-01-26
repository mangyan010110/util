#below 3 lines must be modified as needed
file_filter = '*.txt'
source_dirs = 'd:/myfiles;d:/src1'
destination_dir = 'd:/dest'

#actual script to copy the files
from pathlib import Path
import shutil
import os

print('Copying files...')
for sd in source_dirs.split(';'):
    for d in Path(sd).rglob(file_filter):
        print(d)
        shutil.copyfile(d, destination_dir)
print('Done')