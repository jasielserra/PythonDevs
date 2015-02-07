def reverse(text):
	s = []
	for letter in text:
		s.append(letter)
	s.reverse()
	return "".join(s)
