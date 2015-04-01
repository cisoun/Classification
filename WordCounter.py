#-*- coding: utf-8 -*-

def word_counter(filename):
	dict_words = dict()
	with open(filename, mode="r", encoding="utf-8") as file:
		for lines in file:
			for word in lines.split(" "):
				dict_words[word] = dict_words.get(word, 0) + 1
	return dict_words

if __name__ == '__main__':
	words = word_counter(r'C:\Users\Gary\Dropbox\HE_Arc\3emeAnnee\IA\TP\classification\pos\pos-0000.txt')
	print(words)