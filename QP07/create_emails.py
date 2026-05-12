def create_emails(names, domains):
	return list(map(lambda e: e[0] + '@' + e[1],zip(names,domains) ))
