def filter_emails_by_domain(emails, domain):
	return list(filter(lambda e: e.split('@')[1] == domain, emails))
