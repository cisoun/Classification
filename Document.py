# -*- coding: utf8 -*-

import re

class Document:
	"""docstring for Document"""
	def __init__(self, filename):
		self.filename = filename
		self.useless_words = self.load_useless_words()
		self.dictionary = self.word_counter(filename)
		
	def __repr__(self):
		return self.filename

	def load_useless_words(self):
		"""
		Get in a list all useless words provided by frenchST.txt such as "le", "mes", "aussi",...
		:return: a list with all the useless words in the file
		"""
		words = []
		with open("frenchST.txt", encoding="utf-8", mode="r") as file:
			for lines in file:
				words.append(lines.rstrip("\n\r"))
		return words

	def word_counter(self, filename):
		dict_words = dict()
		with open(filename, mode="r", encoding="utf-8") as file:
			for lines in file:
				for word in lines.split(" "):
					word = word.lower()

					'''
					we tried to get all words with a regex. Example: "salut!" --> "salut", "bof..." --> "bof", "aujourd'hui" --> ["ajourd", "hui"], "moyen.les" --> ["moyen", "les"]
					But it doesn't work very well... So we drop it
					'''
					# words = re.findall(r'\w+', word, re.UNICODE)
					# print(words)

					if len(word) >= 3 and not (word in self.useless_words):
						dict_words[word] = dict_words.get(word, 0) + 1
		return dict_words