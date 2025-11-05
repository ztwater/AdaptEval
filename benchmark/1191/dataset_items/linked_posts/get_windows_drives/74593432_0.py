import os,re
regex = r"([^\s]*:)"
driver = os.popen("wmic logicaldisk get name").read()

print(re.findall(regex, driver))
