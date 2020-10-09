from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt" #needs to work to pass sprint

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# add cardinal directions for moving between rooms NSEW
# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

## code everything here ##
def reverse_directions(direction):
    if direction == 'n':
        return 's'
    elif direction == 's':
        return 'n'
    elif direction == 'w':
        return 'e'
    elif direction == 'e':
        return 'w'

path = []
visited_room = {}

# first room
visited_room[player.current_room.id] = player.current_room.get_exits()

# keep going until we visit every room
while len(visited_room) < (len(room_graph) - 1):
    if player.current_room.id not in visited_room:
        # add room to dict
        visited_room[player.current_room.id] = player.current_room.get_exits()
        print(path[-1])
        # get the room we just came from and remove it from exits.
        v = path[-1]
        visited_room[player.current_room.id].remove(v)

    # when we've already visited all the exits in the room
    while len(visited_room[player.current_room.id]) == 0:
        # get the next room back and travel backwards to find next room with unvisited exits
        reverse = path.pop()    
        traversal_path.append(reverse)
        player.travel(reverse)

    # get one of the exits
    directions = visited_room[player.current_room.id].pop(0)

    # add direction to traversal path
    traversal_path.append(directions)

    # get the reverse direction so we can travel back
    path.append(reverse_directions(directions))

    print(path)
    # travel to that exit
    player.travel(directions)

# q = Stack()
#         visited = set()

#         q.push(starting_vertex)

#         while q.size() > 0:

#             v = q.pop()

#             if v not in visited:
#                 print(v)

#                 visited.add(v)

#                 for neighbor in self.get_neighbors(v):
#                     q.push(neighbor)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
