import shutil


shutil.make_archive(
  base_name=output_dir_path + output_filename_without_extension, 
  format="zip", 
  root_dir=input_root_dir)
