#!/usr/bin/env python
import os
import zipfile

def addDirToZip(zipHandle, path, basePath=""):
    """
    Adding directory given by \a path to opened zip file \a zipHandle

    @param basePath path that will be removed from \a path when adding to archive

    Examples:
        # add whole "dir" to "test.zip" (when you open "test.zip" you will see only "dir")
        zipHandle = zipfile.ZipFile('test.zip', 'w')
        addDirToZip(zipHandle, 'dir')
        zipHandle.close()

        # add contents of "dir" to "test.zip" (when you open "test.zip" you will see only it's contents)
        zipHandle = zipfile.ZipFile('test.zip', 'w')
        addDirToZip(zipHandle, 'dir', 'dir')
        zipHandle.close()

        # add contents of "dir/subdir" to "test.zip" (when you open "test.zip" you will see only contents of "subdir")
        zipHandle = zipfile.ZipFile('test.zip', 'w')
        addDirToZip(zipHandle, 'dir/subdir', 'dir/subdir')
        zipHandle.close()

        # add whole "dir/subdir" to "test.zip" (when you open "test.zip" you will see only "subdir")
        zipHandle = zipfile.ZipFile('test.zip', 'w')
        addDirToZip(zipHandle, 'dir/subdir', 'dir')
        zipHandle.close()

        # add whole "dir/subdir" with full path to "test.zip" (when you open "test.zip" you will see only "dir" and inside it only "subdir")
        zipHandle = zipfile.ZipFile('test.zip', 'w')
        addDirToZip(zipHandle, 'dir/subdir')
        zipHandle.close()

        # add whole "dir" and "otherDir" (with full path) to "test.zip" (when you open "test.zip" you will see only "dir" and "otherDir")
        zipHandle = zipfile.ZipFile('test.zip', 'w')
        addDirToZip(zipHandle, 'dir')
        addDirToZip(zipHandle, 'otherDir')
        zipHandle.close()
    """
    basePath = basePath.rstrip("\\/") + ""
    basePath = basePath.rstrip("\\/")
    for root, dirs, files in os.walk(path):
        # add dir itself (needed for empty dirs
        zipHandle.write(os.path.join(root, "."))
        # add files
        for file in files:
            filePath = os.path.join(root, file)
            inZipPath = filePath.replace(basePath, "", 1).lstrip("\\/")
            #print filePath + " , " + inZipPath
            zipHandle.write(filePath, inZipPath)
