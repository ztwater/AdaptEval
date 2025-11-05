import re

s = """ 
"my name is daniel"  "mobile 8531111453733"[[[[[[--"i like pandas"
"location chennai"! -asfas"aadhaar du2mmy8969769##69869" 
@4343453 "pincode 642002""@mango,@apple,@berry" 
"""
print(re.findall(r'"(.*?)"', s))
