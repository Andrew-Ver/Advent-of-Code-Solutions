import re

with open('input', 'r') as f:
	PUZZLE_INPUT = [ln.strip() for ln in f.readlines()]


location_graph = {}

#Graph implementation from https://www.educative.io/
def add_vertex(v, graph: dict = location_graph):
  if v not in graph:
    graph[v] = []

def add_edge(v1, v2, e, graph: dict = location_graph):
  if v1 in graph and v2 in graph:
    temp = [v2, e]
    graph[v1].append(temp)

for distance_between_cities in PUZZLE_INPUT:
	city_one, city_two = re.findall(r'\w{4,}', distance_between_cities)
	distance = int(re.search(r'\d+', distance_between_cities).group())
	add_vertex(city_one)
	add_vertex(city_two)
	add_edge(city_one, city_two, distance)
	add_edge(city_two, city_one, distance)

def visited_each_closest_city(part: int, city_graph=location_graph) -> int:
	#The distance is shorter/longer depending on the city you start from
	if part == 1:
		distances_for_each_start_city = [] 
		for start_city in list(location_graph.keys()):
			current_city = start_city
			visited = set()
			distance_travelled = 0
			while len(visited) < len(location_graph.keys()):
				closest_neighbour = min([loc for loc in location_graph[current_city] if loc[0] not in visited], key=lambda x: x[1])
				visited.add(current_city)
				visited.add(closest_neighbour[0])
				distance_travelled += closest_neighbour[1]
				current_city = closest_neighbour[0]
			distances_for_each_start_city.append(distance_travelled)
		return min(distances_for_each_start_city)
	elif part == 2:
		distances_for_each_start_city = [] 
		for start_city in list(location_graph.keys()):
			current_city = start_city
			visited = set()
			distance_travelled = 0
			while len(visited) < len(location_graph.keys()):
				furthest_neighbour = max([loc for loc in location_graph[current_city] if loc[0] not in visited], key=lambda x: x[1])
				visited.add(current_city)
				visited.add(furthest_neighbour[0])
				distance_travelled += furthest_neighbour[1]
				current_city = furthest_neighbour[0]
			distances_for_each_start_city.append(distance_travelled)
		return max(distances_for_each_start_city)

print(f'{visited_each_closest_city(part=1)} is the minimum distance travelled to visit all cities (Part One)')
print(f'{visited_each_closest_city(part=2)} is the maximum distance travelled to visit all cities (Part Two)')
