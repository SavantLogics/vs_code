from pathlib import Path
import os

# Opening files with the Open() function

wf = Path('D:\\Documents\\Other\\UsingTheWrite_Text.txt')
written_File = open('D:\\Documents\\Other\\UsingTheWrite_Text.txt')
print(wf.read_text())