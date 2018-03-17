import re

string = " sdjkhf kdsfh ksdhf js sfh  sf skdfh  "
print(re.sub(r'[" "]+', '*', string.strip()))