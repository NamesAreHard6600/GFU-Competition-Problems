


def input_reading():
  table = []
  num = int(input().strip())
  for i in range(num):
    curops = []
    for y in range(int(input().strip())):
        curops.append(input().strip())
    table.append(curops)
  return table

def howmany(table):
    for item in table:
        total = 0
        current = 1
        while current <= 100:
            tempcurrent = current
            for operation in item:
                op = operation.split(" ")
                num = int(op[1])
                type = op[0]
                if type == "SUBTRACT":
                    tempcurrent -= num
                elif type == "ADD":
                    tempcurrent += num
                elif type == "MULTIPLY":
                    tempcurrent *= num
                elif type == "DIVIDE":
                    tempcurrent /= num
            if tempcurrent < 0 or tempcurrent % 1 != 0:
                total += 1
            current += 1
        print(total)




table = input_reading()
howmany(table)
