import re

print(re.findall(r"^\d{1,}\,\d{1,}$|^\d{1,}\.\d{1,}$|^\d{1,}$", '234,1111111qQ'))