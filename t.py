import re

man = 'Place.74d38981-1214-4fe1-9d2a-991ddd3a2308'

res = re.match(r'(.*?)\.', man)

print(res.group(1))
