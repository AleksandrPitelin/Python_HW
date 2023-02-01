import re

tel = re.search(r'\+380'[0-4],input('enter a text: '))

print(tel[0] if tel else "Not found")