# -*- encoding: utf-8 -*-

from Document import Document
from FilesSelector import get_tupled_files
import math


def checkResult(document, result):
	return result in document.filename


class Classification:
	"""docstring for Classification"""
	def __init__(self, listDocPos, listDocNeg):
		self.listDocPos = listDocPos
		self.listDocNeg = listDocNeg
		self.dict_global_word_count = dict()
		self.dict_global_prob = dict()

		index_pos = 0
		index_neg = 1
		self.classificateList(self.listDocPos, index_pos)
		self.classificateList(self.listDocNeg, index_neg)

	def classificate(self, document):
		probPos = 0
		probNeg = 0
		result = "undefined"

		for word, occurence in document.dictionary.items():
			try:
				probPos += math.log(self.dict_global_prob[word][0])
				probNeg += math.log(self.dict_global_prob[word][1])
			except Exception:
				pass

		if(probPos > probNeg):
			result = "pos"
		else:
			result = "neg"

		return checkResult(document, result)


	def classificateList(self, listDoc, index):
		for doc in listDoc:
			for word, occurence in doc.dictionary.items():
				self.dict_global_word_count[word] = self.dict_global_word_count.get(word, 0) + occurence
		
		for word, occurence in self.dict_global_word_count.items():
			try:
				self.dict_global_prob[word][index] = (occurence + 1) / (len(self.dict_global_word_count)) #TODO: add number of positive words
			except KeyError:
				self.dict_global_prob[word] = [0, 0]
				self.dict_global_prob[word][index] = (occurence + 1)/ (len(self.dict_global_word_count)) #TODO: add number of negative words


if __name__ == '__main__':

	positive_slicing = 80
	list_learning_pos, list_test_pos = get_tupled_files("pos", positive_slicing)
	list_learning_neg, list_test_neg = get_tupled_files("neg", positive_slicing)

	list_doc_pos = [Document("pos/" + doc) for doc in list_learning_pos]
	list_doc_neg = [Document("neg/" + doc) for doc in list_learning_neg]

	list_test_pos = [Document("pos/" + doc) for doc in list_test_pos]
	list_test_neg = [Document("neg/" + doc) for doc in list_test_neg]

	classification = Classification(list_doc_pos, list_doc_neg)

	# Test corpus
	list_test_pos.extend(list_test_neg)
	corpus = list_test_pos
	total_document = len(corpus)
	correctly_analysed_doc = 0

	for document in corpus:
		is_result_OK = classification.classificate(document)
		if is_result_OK:
			correctly_analysed_doc += 1

	accuracy = (correctly_analysed_doc/total_document)*100
	print("accuracy:",accuracy)