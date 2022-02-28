from collections import Counter
from chunker_dm.tokenizer import Tokenizer
from chunker_dm.lexicon import ComplexityLexicon
from math import log


class NewVocabularyLexicon(ComplexityLexicon):

	def add_from_dict(self, dictionary):
		if type(dictionary) is not dict: raise TypeError
		self.lexicon.update(dictionary)


class ChunkerLexicon(ComplexityLexicon):

	def __init__(self, tokenizer=Tokenizer):
		self.lexicon = Counter()
		self.Tokenizer = tokenizer
		self.size = 0

	def create_character_dict(self, text):
		tokenizer = self.Tokenizer(text)
		tokens = tokenizer.getTokens()
		self.character_dict = Counter()
		for token in tokens: 
			self.character_dict.update(list(token))

	def clone_for_new_iteration(self):
		lexicon = ChunkerLexicon()
		lexicon.character_dict = self.character_dict
		return lexicon

	def _size_of_word(self, word):
		total = self.character_dict.total()
		size = 0
		for c in list(word):
			probability = self.character_dict[c]/total
			complexity = -log(probability, 2)
			size += complexity
		return size

	def get_size(self):
		return self.size

	def add_from_list(self, parse_results):
		for token in parse_results: 
			if len(token) > 1:
				self.size += self._size_of_word(token)
			self.lexicon.update(token)
