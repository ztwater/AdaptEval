import commands   
size = commands.getoutput('du -sh /path/').split()[0]
