def count_words(text):
	words = text.split()
	return len(words)

def count_characters(text):
	char_counts = {}
	for char in text.lower():
		if char in char_counts:
			char_counts[char] += 1
		else:
			char_counts[char] = 1
	return char_counts

def sort_character_counts(char_counts):
	def get_num(d):
		return d["num"]

	sorted_list = []
	for char, num in char_counts.items():
		if char.isalpha():
			sorted_list.append({"char": char, "num": num})
	sorted_list.sort(key=get_num, reverse=True)
	return sorted_list
