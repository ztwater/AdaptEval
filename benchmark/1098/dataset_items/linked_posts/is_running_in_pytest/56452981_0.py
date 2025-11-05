script_name = os.path.basename(sys.argv[0])
if script_name in ['pytest', 'py.test']:
  print('Running with pytest!')
