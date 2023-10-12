import math
from pprint import pprint

items = list(range(1, 20))
items2 = list(range(1, 20))
slots = {0: [], 1: [], 2: []}


def assign_slots(items, slots):
  s = len(slots.keys())
  wrap = False
  for item in range(0, len(items)):
    wrap = False
    r = math.floor(item / s)
    m = item % s
    if item > s:
      wrap = True
    print(m)
    if item < s and len(slots[item]) == 0:
      slots[item].append([items[item]])
    elif item < s and len(slots[item]) > 0:
      slots[item][len(slots[item]) - 1].append(items[item])
    elif wrap:
      slots[m][len(slots[m]) - 1].append(items[item])
    else:
      slots[m].append([items[item]])
  return slots


results = assign_slots(items, slots)
results2 = assign_slots(items2, slots)

pprint(results2)
