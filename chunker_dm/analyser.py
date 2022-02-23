class Analyser():

	def __init__(self, lexicon=None):
		self.lexicon = lexicon

	def _cleanup(self):
		self.costs = [0]
		self.tokens = []
		self.total_cost = 0
		self.sentence = ""

	def _lookup_candidates(self, candidates):
		_candidates = dict()
		for token in candidates:
			complexity = self.lexicon.complexity(token)
			if complexity: 
				_candidates[token] = complexity
		return _candidates

	def _choose_candidate(self, candidates, char_index):
		_candidates = self._lookup_candidates(candidates)
		if len(_candidates) == 0: 
			self.costs.append(1000 + self.costs[char_index])
			self.tokens.append(self.sentence[char_index])
			return
		for candidate in _candidates:
			_candidates[candidate] += self.costs[char_index - len(candidate) + 1]
		chosen = min(_candidates, key=_candidates.get)
		self.costs.append(_candidates[chosen])
		self.tokens.append(chosen)

	def _build_sentence(self):
		position = len(self.tokens)-1
		words = []
		while position >= 0:
			word = self.tokens[position]
			words.append(word)
			position -= len(word)
		return list(reversed(words))

	def set_lexicon(self, lexicon): 
		self.lexicon = lexicon

	def analyse(self, sentence):
		if not self.lexicon: raise RuntimeError('Lexicon is not set!')
		self._cleanup()
		self.sentence=sentence.lower()
		l = len(self.sentence)
		for char_index in range(0,l):
			_candidates = []
			for start_index in range(0,char_index):
				_candidates.append(self.sentence[start_index:char_index+1])
			_candidates.append(self.sentence[char_index])
			self._choose_candidate(_candidates,char_index)
		self.total_cost = self.costs[-1]
		return self._build_sentence()