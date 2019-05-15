'''
Write a script that searches a folder (and all its subfolders) on your computer and compiles a list of all of
all .jpg files (with the complete path of the files).

If you are feeling bold, create a list for each kind of file extension you find in the folder.

Start with a small folder to make it easy to check if your program is working correctly. Then sub out the
folder name with a bigger folder. This program should work for any specified folder on your computer.


'''
from pathlib import Path

def find_files(root, extensions):
    ext = 0
    for ext in extensions:
        yield from Path(root).glob(f'**/*.{ext}')
    return ext

for file in find_files(Path.home() / 'Documents' / 'lab_folder', ['jpg']):
    print(file)
