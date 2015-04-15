from Document import Document
from FilesSelector import get_random_files_from

class Classification:
	"""docstring for Classification"""
	def __init__(self, listDocPos, listDocNeg):
		self.listDocPos = listDocPos
		self.listDocNeg = listDocNeg
		self.dictGlobalWordCount = dict()
		self.dictGlobalProb = dict()

	def classificate(self, document):
		self.classificateList(self.listDocPos, 0)
		self.classificateList(self.listDocNeg, 1)


	def classificateList(self, listDoc, index):
		for doc in listDoc:
			for k, v in doc.dictionary.items():
				self.dictGlobalWordCount[k] = self.dictGlobalWordCount.get(k, 0) + v
		
		for k, v in self.dictGlobalWordCount.items():
			try:
				self.dictGlobalProb[k][index] = v / len(self.dictGlobalWordCount)
			except KeyError:
				self.dictGlobalProb[k] = [0, 0]
				self.dictGlobalProb[k][index] = v / len(self.dictGlobalWordCount)
			

if __name__ == '__main__':
	listDocPos = [Document("pos/" + doc) for doc in get_random_files_from("pos", 0.1)]
	listDocNeg = [Document("neg/" + doc) for doc in get_random_files_from("neg", 0.1)]

	document = Document("pos/pos-0666.txt")
	classification = Classification(listDocPos, listDocNeg)
	classification.classificate(document)

	print(classification.dictGlobalProb),