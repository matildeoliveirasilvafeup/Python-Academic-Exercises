def dogs(h_age):
	dog_age = 0
	if h_age == 1:
		dog_age += 10.5
	elif h_age == 2:
		dog_age += 10.5 * 2
	else:
		ate_2_anos = 2 * 10.5
		dog_age += 4 * (h_age - 2) + ate_2_anos

	return dog_age
