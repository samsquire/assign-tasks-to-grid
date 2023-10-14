import math
from pprint import pprint

items = list(range(1, 20))
items2 = list(range(1, 20))
slots = {0: [[]], 1: [[]], 2: [[]]}


def assign_slots(items, slots):
  s = len(slots.keys())
  wrap = False
  m = 0
  padding = {k: len(v[0]) for k, v in slots.items()}
  padmax = max([v for v in padding.values()])
  for item in range(0, len(items)):
    wrap = False
    r = math.floor(item / s)
    m = item % s

    if item >= s:
      wrap = True
      
    if item < s and len(slots[item]) == 0:
      for i in range(len(slots[m][0]), padmax):
        slots[m][0].append(0)
      slots[item].append([items[item]])
      
    elif item < s and len(slots[item]) > 0:
      for i in range(len(slots[m][0]), padmax):
        slots[m][0].append(0)
      slots[item][0].append(items[item])
     
    elif wrap:
      # print("value", items[item], "item is", item, "padding is", padding[m], "length is ", len(slots[m][0]), "r is", r)
      
      slots[m][0].append(items[item])
      

    else:
      for i in range(len(slots[m][0]), padmax):
        slots[m][0].append(0)
      slots[m][0].append([items[item]])
  return slots


results = assign_slots(items, slots)
results2 = assign_slots(items2, slots)

pprint(results2)
running = True
end_of_batch = False
while running:
  has_items = False
  for slot in range(0, len(slots.keys())):
    if len(slots[slot][0]) > 0:
      has_items = True
      item = slots[slot][0]
      if len(item) > 0:
        work = item.pop(0)
        if work == 0:
          
          print("empty")
        else:
          print("doing", work)
        
      
        
  if has_items == False:
    running = False
    break

