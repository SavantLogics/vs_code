#! python3
# Copies an entire folder and its cotents into a ZIP file whose filename increments on a Windows based machine 

import zipfile
import os

def backup_to_zip(folder):
    
    # Backup entire contents of "folder" into a ZIP file.
    folder = os.path.abspath('D:\\Zippy_Folder') # make sure folder is absolute
    
    # Figure out the filename this code should use based on what file already exist. 
    number = 1
    while True:
        zip_file_name = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_file_name):
            break
        number = number + 1
        
    # Create the ZIP file.
    print(f'Creating {zip_file_name}...')
    backupZip = zipfile.ZipFile(zip_file_name, 'w')
        
        # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        # Add the current folder to the ZIP file.
        backupZip.write(foldername)
        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue # don't back up the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done')
        
backup_to_zip('D:\\Zippy_Folder')
