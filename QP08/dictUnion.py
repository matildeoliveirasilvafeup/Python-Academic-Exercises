def union_with(combine, dict1, dict2):
	def join_values(key):
		if key in dict1 and key in dict2:
			return combine(dict1[key], dict2[key])
		elif key in dict1:
			return dict1[key]
		else:
			return dict2[key]
	return {key:join_values(key) for key in dict1.keys() | dict2.keys()}
