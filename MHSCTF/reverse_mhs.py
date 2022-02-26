def reverse_roll(text):
	return text[::-1]

def reverse_swoop(text):
	text = list(text)
	for i in range(len(text)):
		text[i] = chr(ord(text[i]) - (i % 5))
	return ''.join(text)
	
print(reverse_roll(reverse_swoop("}12u7#dvl{$`fos_4jwchb}jelg")))
