def switch_dict(adict):
	new_dict = {}
	for key in adict:
		value = adict[key]
		if value not in new_dict:
			new_dict[value] = [key] #cria lista com a key
		else: new_dict[value].append(key)
	return new_dict



