from pathlib import Path
import shutil
import os
import sys

if len(sys.argv) != 2:
    print('Invalid program arguments!!!')
    sys.exit(1)

file_filter = (sys.argv[1])
configs = open('config.txt', 'r').readlines()

print('Validating config.txt contents...')
for c in configs:
    ok = True
    sd, dd = c.split(';')
    if not sd.strip().endswith('/') or not dd.strip().endswith('/'):
        ok = False
    if '\\' in sd.strip() or '\\' in dd.strip():
        ok = False
    if not ok:
        print('Invalid/missing char found on config.txt. ' \
            'Replace all \\ with / and make sure all directory ends with /')
        sys.exit(1)

print('Copying files with file extraction filter as : ' + file_filter)
for c in configs:
    rn = 0
    sd, dd = c.split(';')
    print('Copying files from ' + sd + ' to ' + dd.strip() + '...')
    for d in Path(sd.strip()).rglob(file_filter):
        base, fn = os.path.split(d)
        if not os.path.isfile(dd.strip() + fn):
            shutil.copyfile(d, dd.strip() + fn)
        else:
            rn = rn + 1
            fn, ext = os.path.splitext(fn)
            fn = fn + '-duplicated-' + str(rn) + ext
            shutil.copyfile(d, dd.strip() + fn)
print('Done')
sys.exit(0)