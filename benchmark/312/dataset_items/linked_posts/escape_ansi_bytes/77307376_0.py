child.sendline("ls backup")
child.expect(r"[0-9]{8}_[0-9]{4}.*")
print(child.after.split()) 
-> NG  ['20231016_1603\x1b[0m', '\x1b[01;34m20231016_1606\x1b[0m']

* Add ls option
child.sendline("ls  --color=never backup")
child.expect(r"[0-9]{8}_[0-9]{4}.*")
print(child.after.split()) 
-> OK!  ['20231016_1603', '20231016_1606']
