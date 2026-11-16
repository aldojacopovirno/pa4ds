# Assignment
# List the files in the folder that contains this script. For each file, print
# its full path and its size in bytes. Skip subfolders.
#
# Solution

from os import listdir
from os.path import dirname, abspath, getsize, isfile, join

# abspath(__file__) is the full path of this script; dirname keeps its folder.
folder = dirname(abspath(__file__))

# sorted makes the output order the same on every run.
for name in sorted(listdir(folder)):
    pathname = join(folder, name)

    # getsize works on folders too, but its result would not be a file size.
    if isfile(pathname):
        size = getsize(pathname)
        print(f"{pathname}: {size} bytes")
