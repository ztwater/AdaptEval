import zipfile

def zipFolder(toZipFolder, outputZipFile):
  """
    zip/compress a whole folder/directory to zip file
  """
  print("Zip for foler %s" % toZipFolder)
  with zipfile.ZipFile(outputZipFile, 'w', zipfile.ZIP_DEFLATED) as zipFp:
    for dirpath, dirnames, filenames in os.walk(toZipFolder):
      # print("%s" % ("-"*80))
      # print("dirpath=%s, dirnames=%s, filenames=%s" % (dirpath, dirnames, filenames))
      # print("Folder: %s, Files: %s" % (dirpath, filenames))
      for curFileName in filenames:
        # print("curFileName=%s" % curFileName)
        curFilePath = os.path.join(dirpath, curFileName)
        # print("curFilePath=%s" % curFilePath)
        fileRelativePath = os.path.relpath(curFilePath, toZipFolder)
        # print("fileRelativePath=%s" % fileRelativePath)
        # print("  %s" % fileRelativePath)
        zipFp.write(curFilePath, arcname=fileRelativePath)
  print("Completed zip file %s" % outputZipFile)
