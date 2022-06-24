import re

with open('input', 'r') as f:
	contents = f.readlines()
	rules = sorted([list(map(int, re.findall(r'\d+', ln))) for ln in contents])

lower_bound = 0 
upper_bound = 0
lowest_ip = None
allowed_ips = 0

for r in rules:
	if (r[0] -1) <= upper_bound:
		upper_bound = max(upper_bound, r[1])
	else:
		if not lowest_ip:
			lowest_ip = upper_bound+1
		allowed_ips += (r[0] - (upper_bound+1)) #The allowed IPs are between the previous upper-bound and the range rule's lower
		upper_bound = r[1]

allowed_ips += (4294967295 - upper_bound)
		
print(f'{lowest_ip} (Part One)')
print(f'{allowed_ips} (Part Two)')