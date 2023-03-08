true = True
false = False
import copy

SIZE = 8

def file_reading():
  table = []
  with open("B.in", 'r') as f:
    num = int(f.readline().strip())
    table.append(num)
    for i in range(num*(SIZE+1)):
      table.append(f.readline().strip())
  return table


def input_reading():
  table = []
  num = int(input().strip())
  table.append(num)
  for i in range(num*(SIZE+1)):
    table.append(input().strip())
  return table

class Game:
  def __init__(self, grid, moves):
    self.grid = []
    idCounter = 0
    for i in range(SIZE):
      row = grid[i]
      self.grid.append([])
      for x in row:
        self.grid[i].append(Tile(x,moves,idCounter))
        idCounter +=1
      
    #self.grid = [[Tile(x,moves,i) for x in row] for row in grid] I couldn't use list comprehnsion cause of the id thing
    self.moves = moves
    self.maxPoints = 0
    
  def run(self):
    running = True
    while(running):
      running = False
      for row in self.grid:
        for tile in row:
          if len(tile.paths) > 0:
            tile.explorePaths(self)
            running = True

  def isValid(self,x,y):
    return 0 <= x < SIZE and 0 <= y < SIZE

  def printSelf(self):
    #for row in self.grid:
    #  for tile in row:
    #    print(tile.letter),
    #  print
    print(self.maxPoints)
class Tile:
  def __init__(self,letter,moves,id):
    self.id = id
    self.letter = letter
    self.x = id%SIZE
    self.y = id//SIZE
    self.wall = False
    if letter == "W":
      self.wall = True
    self.points = 0
    if letter.isnumeric():
      self.points = int(letter)
    self.paths = []
    if letter == "S":
      self.paths.append(Path(0,moves,[],self.id))
      
  def explorePaths(self,game):
    for path in self.paths:
      if path.moves == 0:
        game.maxPoints = max(game.maxPoints,path.points)
      else:
        for i in range(-1,2,2):
          searchx = self.x + i
          searchy = self.y
          if game.isValid(searchx,searchy) and not game.grid[searchx][searchy].wall:
            curr = game.grid[searchx][searchy]
            plusPoints = curr.points
            if curr.id in path.ids:
              plusPoints = 0
            curr.paths.append(Path(path.points+plusPoints,path.moves-1,path.ids,curr.id))
          for i in range(-1,2,2):
            searchx = self.x
            searchy = self.y + i
            if game.isValid(searchx,searchy) and not game.grid[searchx][searchy].wall:
              curr = game.grid[searchx][searchy]
              plusPoints = curr.points
              if curr.id in path.ids:
                plusPoints = 0
              curr.paths.append(Path(path.points+plusPoints,path.moves-1,path.ids,curr.id))
        
            
    self.paths = []
    
class Path:
  def __init__(self,points,moves,ids,newid):
    self.points = points
    self.moves = moves
    self.ids = copy.copy(ids)
    self.ids.append(newid)

datatable = file_reading()
# datatable = input_reading()
data = iter(datatable)

for i in range(next(data)):
  moves = int(next(data))
  #print(moves)
  grid = []
  for i in range(SIZE):
    grid.append(next(data))
  game = Game(grid, moves)
  game.run()
  game.printSelf()