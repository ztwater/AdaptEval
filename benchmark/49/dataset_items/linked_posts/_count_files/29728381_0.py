for root, dirs, files in os.walk(input_path):    
for name in files:
    if os.path.splitext(name)[1] == '.TXT' or os.path.splitext(name)[1] == '.txt':
        datafiles.append(os.path.join(root,name)) 


print len(files) 
