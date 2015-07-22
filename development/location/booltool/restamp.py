
def findtime(s1,t):
	if len(s1) == 1:
		if s1[0]["t"] > t:
			return None
		return s1[0]
	i = len(s1)/2
	if s1[i]["t"] > t:
		return findtime(s1[:i],t)
	return findtime(s1[i:],t)


def restamp(s1, s2):
	"""
	Given two arrays of stream data s1 and s2, returns a combined array with s1's
	timestamps, with d1 being s1's value, and d2 being the value of s2 at the closest
	smaller timestamp.
	"""

	result = []

	#First move the values of s1 to be within a valid range given s2
	i = 0
	while s1[i]["t"] < s2[0]["t"] and i < len(s1):
		i+=1
	j = len(s1) - 1
	while s1[j]["t"] > s2[-1]["t"] and j > 0:
		j -=1
	if i >=j:
		return []
	s1 = s1[i:j+1]

	#Next, generate the results
	for i in xrange(len(s1)):
		val = {
			"t": s1[i]["t"],
			"d": s1[i]["d"],
			"d2": findtime(s2,s1[i]["t"])["d"]
		}
		result.append(val)
	return result
