# -*- coding: utf8 -*-

import re
from UselessWords import useless_words

class Document:
	"""docstring for Document"""
	def __init__(self, filename):
		self.filename = filename
		self.useless_words = useless_words
		self.dictionary = self.word_counter(filename)
		
	def __repr__(self):
		return self.filename

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
					# for word in words....add to dict_word...
					# print(words)

					if len(word) >= 3 and not (word in self.useless_words):
						dict_words[word] = dict_words.get(word, 0) + 1
		return dict_words