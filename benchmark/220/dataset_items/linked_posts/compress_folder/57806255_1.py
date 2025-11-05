$ cat zip_cap_dirs.py 
""" Zip 'cap_*' directories. """           
import os                                                                       
import zipfile as zf                                                            


for root, dirs, files in sorted(os.walk('.')):                                                                                               
    if 'cap_' in root:                                                          
        print(f"Compressing: {root}")                                           
        # Defining .zip name, according to Capítulo.                            
        cap_dir_zip = '{}.zip'.format(root)                                     
        # Opening zipfile context for current root dir.                         
        with zf.ZipFile(cap_dir_zip, 'w', zf.ZIP_DEFLATED) as new_zip:          
            # Iterating over os.walk list of files for the current root dir.    
            for f in files:                                                     
                # Defining relative path to files from current root dir.        
                f_path = os.path.join(root, f)                                  
                # Writing the file on the .zip file of the context              
                new_zip.write(f_path) 
