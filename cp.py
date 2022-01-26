#below 3 lines must be modified as needed
file_filter = '*.dwg'
source_dirs = 'D:\Test\000520 BODY;D:\Test\000510 SHELL'
destination_dir = 'D:\Test\Destination'

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
