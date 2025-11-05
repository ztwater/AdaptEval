import win32com.client as com

def get_folder_size(path):
   try:
       fso = com.Dispatch("Scripting.FileSystemObject")
       folder = fso.GetFolder(path)
       size = str(round(folder.Size / 1048576))
       print("Size: " + size + " MB")
   except Exception as e:
       print("Error --> " + str(e))
