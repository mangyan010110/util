#below 3 lines must be modified as needed
file_filter = '*.dwg'
source_dirs = 'D:\10_Shigoto\01_Tsuneishi Technical Services (Phils.), Inc\D10Afra\01_KEY PLAN\02_DRAWINGS\110916_DATA\000520 BODY;D:\10_Shigoto\01_Tsuneishi Technical Services (Phils.), Inc\D10Afra\01_KEY PLAN\02_DRAWINGS\110916_DATA\000510 SHELL'
destination_dir = 'D:\00_Continuous Professional Development\Udemy\Pyhton\Test Destination'

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
