def input_reading():
  table = []
  num = int(input().strip())
  table.append(num)
  for i in range(num):
    z = []
    for x in range(5):
      new = input().strip()
      z.append(new)
    table.append(z)
  for x in range(len(table)):
    if x > 0:
      bestquartet = 0
      for y in range(len(table[x])):
        if y != 0:
          line = table[x][y].split(" ")
          max = 0
          for item in line:
            if int(item) > max:
              max = int(item)
          bestquartet += max
      print(bestquartet)
