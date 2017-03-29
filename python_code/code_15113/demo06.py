import random 

cave_numbers =range(0,20)
cave =[]
for i in cave_numbers:
  cave.append([])
     
unvisited_caves = range(0,20)
visited_caves = [0]
unvisited_caves.remove(0)

while unvisited_caves !=[]:
    i = random.choice(visited_caves)
    if len(cave[i]) >=3:
        continue

    next_cave = random.choice(unvisited_caves)
    cave[i].append(next_cave)
    cave[next_cave].append(i)


    visited_caves.append(next_cave)
    unvisited_caves.remove(next_cave)

    for number in cave_numbers:
        print number,":",cave[number]
    print'---------'

    for i in cave_numbers:
        while len(cave[i])<3:
            passage_to = random.choice(cave_numbers)
            cave[i].append(passage_to)

    for number in cave_numbers:
        print number,":",cave[number]
    print '---------'
