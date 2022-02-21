import unittest as ut
from chunker_dm.tokenizer import Tokenizer 


class TestTokenizer(ut.TestCase):

  def setUp(self):
    self.tok = Tokenizer("Isso é uma oração, e isso é outra.")

  def test_tokenizer_lowers_case(self):
    self.assertNotIn("Isso", self.tok.getTokens())
    
  def test_tokenizer_eliminates_non_alphanumeric_chars(self):
    self.assertNotIn("oração,", self.tok.getTokens())
    self.assertNotIn("outra.", self.tok.getTokens())
    self.assertIn("outra", self.tok.getTokens())
    self.assertIn("oração", self.tok.getTokens())
    
  def test_tokenizer_adds_from_other_texts(self):
    self.tok.add("Mais uma oração")
    self.assertIn("mais", self.tok.getTokens())
