from pathlib import Path

# First always point to the directory you want to make a file in
d = Path('D:/Documents/Other/UsingTheWrite_Text.txt')

# Use the .write_text() to create a new text file
d.write_text('This is a more precise way of creating text instead of using open().')

# Then test to make sure that path exists by using the Path Validity of .exists
d.exists()

# Read the text of a file by using .read_text()
d.read_text()