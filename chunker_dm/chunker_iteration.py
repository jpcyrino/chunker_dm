from chunker_dm.chunker_lexicons import NewVocabularyLexicon, ChunkerLexicon
from analyser import Analyser


class ChunkerIteration():

	def __init__(self, chunker_lexicon, initial_parse, corpus):
		self.chunker_lexicon = chunker_lexicon
		self.initial_parse = initial_parse
		self.corpus = corpus # corpus precisa ser uma lista de frases, lista de palavras
		self.length_of_parse = 0

	def _parse_for_new_candidates(self):
		parser_for_new_candidates = Analyser(lexicon=self.chunker_lexicon)
		results = []
		for sentence in self.corpus:
			parse = parser_for_new_candidates.analyse(sentence)
			results.append(parse)
			self.length_of_parse += parse.total_cost
		return results

	def _create_new_vocabulary(self, list_of_parse_results, n_of_candidates): 
		results = []
		for parse_results in list_of_parse_results:
			results_of_join = []
			for i in range(0,len(parse_results),2):
				if i = len(parse_results)-1: 
					results_of_join.append(parse_results[i])
				else:
					results_of_join.append(parse_results[i] + parse_results[i+1])
			results.append(results_of_join)
		vocabulary = Counter()
		for tokens in results:
			vocabulary.update(tokens)
		return dict(vocabulary.most_common(n_of_candidates))

	def _create_new_vocabulary_lexicon(self, old_vocabulary, new_vocabulary):
		lexicon = NewVocabularyLexicon()
		lexicon.add_from_dict(old_vocabulary)
		lexicon.add_from_dict(new_vocabulary)
		return lexicon

	def _parse_with_new_vocabulary(self, lexicon_with_new_vocabulary):
		parser = Analyse(lexicon=lexicon_with_new_vocabulary)
		results = []
		for sentence in self.corpus:
			results.append(parser.analyse(sentence))
		return results

	def _create_lexicon_for_new_iteration(self, second_parse_results):
		lexicon = self.chunker_lexicon.clone_for_new_iteration()
		for tokens in second_parse_results:
			lexicon.add(tokens)
		return lexicon

	def start(self, n_of_candidates):
		new_vocabulary = self._create_new_vocabulary(self.initial_parse, n_of_candidates)
		old_vocabulary = self.chunker_lexicon.frequency_dict()
		lexicon_for_second_parse = self._create_new_vocabulary_lexicon(old_vocabulary, new_vocabulary)
		second_parse = self._parse_with_new_vocabulary(lexicon_for_second_parse)
		new_lexicon = self._create_lexicon_for_new_iteration(second_parse)
		parse_with_new_lexicon_parse = self.parse_for_new_candidates()
		return (new_lexicon, parse_with_new_lexicon, { 
			"lexicon_length" : new_lexicon.get_size(),
			"corpus_length" : self.length_of_parse,
			"model_length" : new_lexicon.get_size() + self.length_of_parse
			})








