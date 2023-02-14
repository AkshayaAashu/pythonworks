"""password validation"""

import re

pswd = 'XdsE83&!'
reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"

# compiling regex
match_re = re.compile(reg)

# searching regex
res = re.search(match_re, pswd)

# validating conditions
if res:
   print("Valid Password")
else:
   print("Invalid Password")