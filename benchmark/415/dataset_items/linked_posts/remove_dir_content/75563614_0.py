import os

def remove_files_in_folder(folderPath):
        # loop through all the contents of folder
        for filename in os.listdir(folderPath):
            # remove the file
            os.remove(f"{folderPath}/{filename}")

remove_files_in_folder('./src/inputFiles/tmp')
