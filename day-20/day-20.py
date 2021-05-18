import re
from copy import deepcopy

with open('input', 'r') as f:
	contents = f.readlines()
	data = [ln.strip() for ln in contents]

particles = {}

for i in range(len(data)):
	coord_names = ['pos_x', 'pos_y', 'pos_z', 'vel_x', 'vel_y', 'vel_z', 'accel_x', 'accel_y', 'accel_z']
	coords = list(map(int, re.findall(r'-?\d+', data[i])))
	particles[i] = dict(zip(coord_names, coords)) 
	#To Check for Part Two Collisions
	particles[i]['position_list'] = [particles[i]['pos_x'], particles[i]['pos_y'], particles[i]['pos_z']]

#Part One
#Lowest Absolute sum of acceleration and then lowest velocity 
particles_total_acceleration = {}
for k in particles.keys():
	s = sum(map(abs, [particles[k]['accel_x'], particles[k]['accel_y'], particles[k]['accel_z']]))
	particles_total_acceleration[k] = s
particles_total_acceleration = [k for k in particles_total_acceleration.keys() if particles_total_acceleration[k] == min(particles_total_acceleration.values())]

part_one = min(particles_total_acceleration, key=lambda x: sum([particles[x]['vel_x'], particles[x]['vel_y'], particles[x]['vel_z']]))
print(f'The Particle that will stay closest to position <0, 0, 0> is {part_one} (Part One)')

#Part Two
def check_for_collisions(particles_dict: dict) -> list:
	collision_position_coords = [dup for dup in [particles_dict[p]['position_list'] for p in particles_dict] if [particles_dict[p]['position_list'] for p in particles_dict].count(dup)>1]
	return [p for p in particles_dict if particles_dict[p]['position_list'] in collision_position_coords]

def update_particles(particles: dict) -> dict:
	new_particles = deepcopy(particles)
	for p in new_particles.keys():
		new_particles[p]['vel_x'] += new_particles[p]['accel_x']
		new_particles[p]['vel_y'] += new_particles[p]['accel_y']
		new_particles[p]['vel_z'] += new_particles[p]['accel_z']
		new_particles[p]['pos_x'] += new_particles[p]['vel_x']
		new_particles[p]['pos_y'] += new_particles[p]['vel_y']
		new_particles[p]['pos_z'] += new_particles[p]['vel_z']
		# To Check for Collisions
		new_particles[p]['position_list'] = [new_particles[p]['pos_x'], new_particles[p]['pos_y'], new_particles[p]['pos_z']]
	return new_particles

def part_two(particles_dict: dict) -> int:
	for _ in range(1000):
		particles_dict = update_particles(particles_dict)
		for p in check_for_collisions(particles_dict):
			del particles_dict[p]
	return len(particles_dict)

print(f'{part_two(particles)} left after removing collisions (Part Two)')