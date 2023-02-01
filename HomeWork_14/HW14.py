import re
numphone1 = "+380"
numphone2 = "380"
numphone3 = "0"
for i in range (4):
    print(i)
if numphone1 is True:
    print(re.findall('\+380',numphone1))
elif numphone2 is True:
    print(re.findall('380',numphone2))
elif numphone3 is True:
    print(re.findall('0',numphone3))
else:print(ValueError)