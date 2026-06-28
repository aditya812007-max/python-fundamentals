import re

email = input("whats ur email? ").strip()

if re.search(r'^\w+@[a-zA-Z0-9_]+\.edu.in$',email):
    print('valid')
else:
    print('invalid')