# Check Path Validity
from pathlib import Path
import os

# Map the path to a variable
# This is mapped to the file in Other folder
f = Path('D:/Documents/Other/myfile.txt') 

# This is mapped to the Documents folder
d = Path('D:/Documents') 

# Use the .exists (to check path) Use .is_dir (to check if its a directory) Use .is_file (to check if its a file)

d.exists()
f.exists()
d.is_file()
f.is_file()
f.is_dir()
d.is_dir()

print(d.exists())
print(f.exists())
print(f.read_text())