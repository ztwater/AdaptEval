import os
import zipfile

def zipdir(path, ziph):
    # Iterate all the directories and files
    for root, dirs, files in os.walk(path):
        # Create a prefix variable with the folder structure inside the path folder. 
        # So if a file is at the path directory will be at the root directory of the zip file
        # so the prefix will be empty. If the file belongs to a containing folder of path folder 
        # then the prefix will be that folder.
        if root.replace(path,'') == '':
                prefix = ''
        else:
                # Keep the folder structure after the path folder, append a '/' at the end 
                # and remome the first character, if it is a '/' in order to have a path like 
                # folder1/folder2/file.txt
                prefix = root.replace(path, '') + '/'
                if (prefix[0] == '/'):
                        prefix = prefix[1:]
        for filename in files:
                actual_file_path = root + '/' + filename
                zipped_file_path = prefix + filename
                zipf.write( actual_file_path, zipped_file_path)


zipf = zipfile.ZipFile('Python.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir('/tmp/justtest/', zipf)
zipf.close()
