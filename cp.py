#below 3 lines must be modified as needed
file_filter = '*.dwg'
source_dirs = 'D:/10_Shigoto/05_Asia Projects Engineering Pte Ltd (APECO)/C1805 - PIPERACK/'
destination_dir = 'D:/Test/Destination/'

#actual script to copy the files
from pathlib import Path
import shutil
import os

print('Copying files...')
rn = 0
for sd in source_dirs.split(';'):
    for d in Path(sd).rglob(file_filter):
        #print(d)
        base, fn = os.path.split(d)
        if not os.path.isfile(destination_dir + fn):
            shutil.copyfile(d, destination_dir + fn)
            print('copied as : ' + str(d))
        else:
            rn = rn + 1
            fn, ext = os.path.splitext(fn)
            fn = fn + '-duplicated-' + str(rn) + ext
            shutil.copyfile(d, destination_dir + fn)
            print('copied as : ' + base + '\\' + fn)
print('Done')
