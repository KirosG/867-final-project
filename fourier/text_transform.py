import re

activities = {'Walking': 1,
		'Jogging': 2,
		'Sitting': 3,
		'Standing': 4,
		'Upstairs': 5,
		'Downstairs': 6 }

f = open('C:/NachumPC-Ofir/6.867/Project/WISDM_ar_v1.1/WISDM_ar_v1.1_raw.txt', 'r')
#f = open('hi.txt', 'r')

t = open('C:/NachumPC-Ofir/6.867/Project/WISDM_ar_v1.1/raw.txt', 'w')

for line in f:
	if len(line)>=5:
		blah = line[:-3]
		p = re.compile('[A-Za-z]+')
		m = p.search(blah)
		activity = activities[m.group()]
		final = blah[0:m.start()]+str(activity)+blah[m.end():]
		t.write(final+'\n')