# Check where I am at

# Import a couple libraries
from pathlib import Path
import os

# Append the .cwd (Current working directory) to figure out where I am
Path.cwd()

# To change directory
os.chdir('C:\\Windows\\System32')

# Check to see if changed to that directory
Path.cwd()