def  find_treasure(pos, steps):
	X, Y = pos
	for step in steps:
		if step == 'up':
			Y += 1
		elif step == 'down':
			Y -= 1
		elif step == 'right':
			X += 1
		elif step == 'left':
			X -= 1
	return (X,Y)

