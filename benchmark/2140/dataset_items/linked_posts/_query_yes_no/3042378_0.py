# raw_input returns the empty string for "enter"
yes = {'yes','y', 'ye', ''}
no = {'no','n'}

choice = raw_input().lower()
if choice in yes:
   return True
elif choice in no:
   return False
else:
   sys.stdout.write("Please respond with 'yes' or 'no'")
