def  suggest_friendship(target_user, social_network):
	set_retorno = set()
	for name, friends in social_network.items():
		if name != target_user:
			common_friends = friends.intersection(social_network[target_user])
			if len(common_friends) >= 2 and name not in social_network[target_user]:
				set_retorno.add(name)
	return set_retorno


