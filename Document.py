class Document:
	"""docstring for Document"""
	def __init__(self, filename):
		self.filename = filename
		self.dictionary = self.word_counter(filename)
		
	def __repr__(self):
		return self.filename

	def word_counter(self, filename):
		dict_words = dict()
		with open(filename, mode="r", encoding="utf-8") as file:
			for lines in file:
				for word in lines.split(" "):
					dict_words[word] = dict_words.get(word, 0) + 1
		return dict_words