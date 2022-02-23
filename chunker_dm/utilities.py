from chunker_dm.lexicon import ComplexityLexicon

def create_lexicon_from_text_file(file_name, LexiconClass=ComplexityLexicon):
	chunkList = open(file_name, 
		encoding='utf-8', mode='r').read().split('\n')
	clex = LexiconClass()
	for chunk in chunkList: 
		clex.add(chunk)
	return clex