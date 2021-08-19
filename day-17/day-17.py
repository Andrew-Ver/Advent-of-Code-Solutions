from collections import deque
import hashlib

passcode = 'vkjiggvb' #From Puzzle Input

room_layout = [[x for x in range(4)] for y in range(4)]

def doors_open(path_taken: str, passcode=passcode) -> list:
	if len(path_taken):
		h = hashlib.md5((passcode+path_taken).encode()).hexdigest()
	else:
		h = hashlib.md5(passcode.encode()).hexdigest()
	return [True if d in 'bcdef' else False for d in h[:4]]
				
def valid(n: list, room=room_layout) -> bool:
	return (n[0] >= 0 and n[0] < len(room_layout)) and (n[1] >= 0 and n[1] < len(room_layout[0]))

queue = deque()
queue.append((0, 0, '')) #Start node
target = (3, 3) 
longest_path = 0
shortest_path = '.'*100

while queue:
	Y, X, path = queue.popleft()

	doors_available = doors_open(path)
	doors = [(Y-1, X), (Y+1, X), (Y, X-1), (Y, X+1)] # Doors UP, DOWN, LEFT, RIGHT
	directions = 'UDLR'
	#Neighbour if the door is available per the hash and valid 
	neighbour_doors = [(doors[d][0], doors[d][1], path+directions[d]) for d in range(len(doors_available)) if doors_available[d] and valid(doors[d])]
	
	if (Y, X) == target:
		longest_path = max(len(path), longest_path)
		if len(path) < len(shortest_path):
			shortest_path = path
	else:
		#enqueue neighbour door (Y, X, path(str) + direction)
		queue.extend(neighbour_doors)

print(f'Shortest Path to the vault: {shortest_path} (Part One)')
print(f'LONGEST PATH LENGTH: {longest_path} (Part Two)')