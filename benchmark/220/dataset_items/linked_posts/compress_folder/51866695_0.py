def zipDir( path, ziph ) :
 """
 Inserts directory (path) into zipfile instance (ziph)
 """
 for root, dirs, files in os.walk( path ) :
  for file in files :
   ziph.write( os.path.join( root, file ) , os.path.basename( os.path.normpath( path ) ) + "\\" + file )

def makeZip( pathToFolder ) :
 """
 Creates a zip file with the specified folder
 """
 zipf = zipfile.ZipFile( pathToFolder + 'file.zip', 'w', zipfile.ZIP_DEFLATED )
 zipDir( pathToFolder, zipf )
 zipf.close()
 print( "Zip file saved to: " + pathToFolder)

makeZip( "c:\\path\\to\\folder\\to\\insert\\into\\zipfile" )
