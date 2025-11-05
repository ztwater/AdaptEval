def WriteDirectoryToZipFile( zipHandle, srcPath, zipLocalPath = "", zipOperation = zipfile.ZIP_DEFLATED ):
    basePath = os.path.split( srcPath )[ 0 ]
    for root, dirs, files in os.walk( srcPath ):
        p = os.path.join( zipLocalPath, root [ ( len( basePath ) + 1 ) : ] )
        # add dir
        zipHandle.write( root, p, zipOperation )
        # add files
        for f in files:
            filePath = os.path.join( root, f )
            fileInZipPath = os.path.join( p, f )
            zipHandle.write( filePath, fileInZipPath, zipOperation )
