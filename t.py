import re

pattern = r'(.*?)=(.*?)\"'

t1 = 'name="John"'
t2 = 'age="25"'
t3 = 'color="blue"'

r1 = re.match(pattern, t1)

print(r1.group(2).strip())
