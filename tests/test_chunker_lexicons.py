from chunker_dm.chunker_lexicons import NewVocabularyLexicon, ChunkerLexicon
import unittest as ut
from math import log

class TestNewVocabularyLexicon(ut.TestCase):

	def test_nvl_gets_vocabulary_through_frequency_dic(self):
		nvl = NewVocabularyLexicon()
		nvl.add("um novo dicionário")
		nvl.add_from_dict({'um': 8, 'novo': 9, 'dicionário': 3})
		self.assertEqual(nvl.frequency("um"),9)

	def test_nvl_raises_error_when_dict_not_passed(self):
		nvl = NewVocabularyLexicon()
		with self.assertRaises(TypeError):
			nvl.add_from_dict("um novo dicionário")

class TestChunkerLexicon(ut.TestCase):

	def test_adds_character_dict(self):
		cl = ChunkerLexicon()
		cl.create_character_dict("um novo texto")
		self.assertEqual(cl.character_dict['o'], 3)

	def test_size_of_lexicon(self):
		cl = ChunkerLexicon()
		cl.create_character_dict("um novo texto")
		cl.add_from_list(['u','um','n','novo'])
		test_size = -log(cl.character_dict['u']/cl.character_dict.total(),2)
		test_size += -log(cl.character_dict['m']/cl.character_dict.total(),2)
		test_size += -log(cl.character_dict['n']/cl.character_dict.total(),2)
		test_size += -log(cl.character_dict['o']/cl.character_dict.total(),2)
		test_size += -log(cl.character_dict['v']/cl.character_dict.total(),2)
		test_size += -log(cl.character_dict['o']/cl.character_dict.total(),2)
		self.assertEqual(cl.get_size(), test_size)

	def test_clone_of_lexicon(self):
		cl = ChunkerLexicon()
		cl.add("um novo texto")
		cl.create_character_dict("um novo texto")
		clone = cl.clone_for_new_iteration()
		self.assertEqual(cl.character_dict['o'], clone.character_dict['o'])
		self.assertNotEqual(cl.total(), clone.total())
