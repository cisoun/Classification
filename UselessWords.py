#-*- coding: utf-8 -*-

class UselessWords:

	@staticmethod
	def _load_useless_words():
		"""
		Get in a list all useless words provided by frenchST.txt such as "le", "mes", "aussi",...
		:return: a list with all the useless words in the file
		"""
		words = []
		with open("frenchST.txt", encoding="utf-8", mode="r") as file:
			for lines in file:
				words.append(lines.rstrip("\n\r"))
		return words

useless_words = UselessWords._load_useless_words()