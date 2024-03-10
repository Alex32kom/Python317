import re

s = "my-p@ssword"
reg = r"^[a-zA-Z0-9_@-]{6,18}$"
print(re.findall(reg, s))
