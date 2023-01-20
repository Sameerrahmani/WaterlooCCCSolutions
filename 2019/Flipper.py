Grid = [
  [1, 2],
  [3, 4] 
]

flip = str(input())

HCount = flip.count('H')
VCount = flip.count('V')

for h in range(HCount):
  temp = Grid[0]
  Grid[0] = Grid[1]
  Grid[1] = temp

for v in range(VCount):
  temp1 = [Grid[0][1], Grid[0][0]]
  temp2 = [Grid[1][1], Grid[1][0]]

  Grid[1] = temp2
  Grid[0] = temp1



print(*Grid[0], sep=' ')
print(*Grid[1], sep=' ')
