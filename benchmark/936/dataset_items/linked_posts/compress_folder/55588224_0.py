for root, dirs, files in os.walk("."):
    for sub_dir in dirs:
        zip_you_want = sub_dir+".zip"
        zip_process = zipfile.ZipFile(zip_you_want, "w", zipfile.ZIP_DEFLATED)
        zip_process.write(file_you_want_to_include)
        zip_process.close()

        print("Successfully zipped directory: {sub_dir}".format(sub_dir=sub_dir))
