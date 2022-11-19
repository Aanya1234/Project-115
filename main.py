
import os


# Source file path
source = 'main.txt'

# destination file path
dest = 'newfile.txt'


# Now rename the source path
# to destination path
# using os.rename() method
os.rename(source, dest)
print("Source path renmaed to destination path successfully.")