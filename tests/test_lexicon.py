import unittest as ut
from chunker_dm.lexicon import Lexicon, ProbabilityLexicon, ComplexityLexicon


class TestLexicon(ut.TestCase):

  def test_lexicon_adds_tokens_from_text(self):
    lex = Lexicon()
    lex.add("Isso é uma frase")
    self.assertEqual(lex.total(), 4)

  def test_lexicon_counts_frequency_of_word(self):
    lex = Lexicon()
    lex.add("Essa aqui é uma frase para testar uma classe de Léxico")
    self.assertEqual(lex.frequency("uma"), 2)
    self.assertEqual(lex.frequency("frase"),1)
    
  def test_lexicon_tokenizes_properly(self):
    lex = Lexicon()
    lex.add("Uma frase.")
    self.assertEqual(lex.frequency("frase"),1)
    self.assertEqual(lex.frequency("frase."),0)   

  def test_gets_frequency_dict(self):
    lex = Lexicon()
    lex.add("Uma frase.")
    fdict = lex.frequency_dict()
    self.assertIs(type(fdict), dict)
    self.assertEqual(fdict["uma"], 1)

class TestProbabilityLexicon(ut.TestCase):

  def test_gets_probability_of_token(self):
    plex = ProbabilityLexicon()
    plex.add("Duas palavras.")
    self.assertEqual(plex.probability("duas"),0.5)
    self.assertEqual(plex.probability("palavras"),0.5)
    
  def test_gets_probability_dict(self):
    plex = ProbabilityLexicon()
    plex.add("Uma frase.")
    pdict = plex.probability_dict()
    self.assertIs(type(pdict), dict)
    self.assertEqual(pdict["uma"], 0.5)
    
class TestComplexityLexicon(ut.TestCase):
 
  def test_gets_complexity_dict(self):
    clex = ComplexityLexicon()
    clex.add("Uma frase.")
    cdict = clex.complexity_dict()
    self.assertIs(type(cdict), dict)
    self.assertEqual(cdict["uma"], 1)