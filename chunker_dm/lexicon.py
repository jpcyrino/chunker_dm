from collections import Counter
from math import log
from chunker_dm.tokenizer import Tokenizer

class Lexicon():

  def __init__(self, tokenizer=Tokenizer):
    self.lexicon = Counter()
    self.Tokenizer = tokenizer
    
  def add(self, text):
    tokenizer = self.Tokenizer(text)
    self.lexicon.update(tokenizer.getTokens())
    
  def frequency(self, token):
    return self.lexicon[token]
    
  def total(self):
    return self.lexicon.total()
    
  def frequency_dict(self):
    return dict(self.lexicon)
    

class ProbabilityLexicon(Lexicon):

  def probability(self, token):
    return self.lexicon[token]/self.lexicon.total()
  
  def probability_dict(self):
    return {token: self.probability(token) for token in self.lexicon}
    

class ComplexityLexicon(ProbabilityLexicon):

  def complexity(self, token):
    if self.frequency(token) == 0: 
      return None  

    return -log(self.probability(token),2)
    
  def complexity_dict(self):
    return {token: self.complexity(token) for token in self.lexicon}
    