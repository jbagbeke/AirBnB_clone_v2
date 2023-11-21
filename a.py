import re

pattern = r'(.*?)="(.*?)"'
p2 = r'(.*?)=(\S+)'

t1 = 'name="John"'
t2 = 'age=25 now=2333'
t3 = 'color="blue"'

r1 = re.match(pattern, t1)
r2 = re.match(p2, t2)

if r2:
    print(r2.group(1))
    print(r2.group(2))

if r1:
    attribute_name = r1.group(1).strip()
    attribute_value = r1.group(2).strip()
    print(f"Attribute Name: {attribute_name}, Attribute Value: {attribute_value}")
else:
    print("No match found.")

