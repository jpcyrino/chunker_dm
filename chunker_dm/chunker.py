from .chunker_lexicons import ChunkerLexicon
from .chunker_iteration import ChunkerIteration
import regex

class Chunker():

	def __init__(self, corpus):
		self.corpus = corpus

	def _prepare_corpus(self):
		prepared = self.corpus.replace("-"," ")
		prepared = regex.sub(r"\s+","",prepared)
		prepared = regex.split(r"[.,;:!?\n]",prepared)
		return prepared

	def _prepare_corpus_morphology(self):
		prepared = self.corpus.replace("-","")
		prepared = regex.sub(r"\s+"," ",prepared)
		prepared = regex.split(r"[\s.,;:!?\n]",prepared)
		return prepared

	def _create_lexicon(self, prepared_corpus):
		cl = ChunkerLexicon()
		cl.create_character_dict(prepared_corpus)
		cl.lexicon.update(cl.character_dict)
		return cl

	def _iterate(self, corpus, lexicon, n_iterations, n_new_words):
		parse = [list(c) for c in corpus]
		self.details = []
		for i in range(0,n_iterations):
			ci = ChunkerIteration(lexicon,parse,corpus)
			lexicon, parse, details = ci.start(n_new_words)
			if len(self.details) > 0:
				delta = details["model_length"] - self.details[-1]["model_length"]
				if delta == 0: break
				details["delta"] = delta
			else:
				details["delta"] = 0
			self.details.append(details)
			#print(details)
		return lexicon, parse

	def start(self, morph=False, n_iterations=50, n_new_words=25):
		if morph:
			corpus = self._prepare_corpus_morphology()
		else:
			corpus = self._prepare_corpus() 
		lexicon = self._create_lexicon(corpus)
		return self._iterate(corpus, lexicon, n_iterations, n_new_words)


