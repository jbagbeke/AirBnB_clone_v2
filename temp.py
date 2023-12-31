from models import storage
from models.state import State


states = storage.all(State)
print("\n\n")
print(states)
print('\n\n')
state_cities = {v: sorted(v.cities, key=lambda x: x.name) for v in states.values() if v.cities}
print('\n\n')
print(state_cities)
print('\n\n')
