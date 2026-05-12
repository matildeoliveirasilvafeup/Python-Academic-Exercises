def extract_email_names(emails):
	return [email.split('@') [0] for email in emails]

"""
def extract_email_names(emails):
    return list(map(lambda e: e.split('@')[0], emails))
"""
