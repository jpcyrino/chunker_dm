from collections import Counter
from .tokenizer import Tokenizer
from .lexicon import ComplexityLexicon
from math import log


class NewVocabularyLexicon(ComplexityLexicon):

	def add_from_dict(self, dictionary):
		if type(dictionary) is not dict: raise TypeError
		self.lexicon.update(dictionary)


class ChunkerLexicon(ComplexityLexicon):

	def __init__(self, tokenizer=Tokenizer):
		self.lexicon = Counter()
		self.character_dict = Counter()
		self.Tokenizer = tokenizer

	# def frequency_dict(self):
	   #	frequencies = Counter()
	   #    frequencies.update(self.lexicon)
	   #    frequencies.update(self.character_dict)
	   #    return dict(frequencies)

	def create_character_dict(self, corpus):
		self.character_dict = Counter()
		for sentence in corpus: 
			tokenizer = self.Tokenizer(sentence)
			tokens = tokenizer.getTokens()
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
		size = 0
		for token in self.lexicon:
			if len(token) > 1:
				size += self.complexity(token)
		return size

	def add_from_list(self, parse_results):
		for token in parse_results:
			self.lexicon.update([token])
