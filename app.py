from chunker_dm.chunker_lexicons import ChunkerLexicon
from chunker_dm.chunker_iteration import ChunkerIteration
import regex

frases = open("biblia-em-txt.txt", encoding="utf-8", mode="r").read()
frases = regex.split(r"[.,;:!?\n]",frases)
frases = [regex.sub(r"\s","",f) for f in frases]

parse_frases = [list(f) for f in frases[0:800]]
cl = ChunkerLexicon()
cl.create_character_dict(frases[0:800])
cl.lexicon.update(cl.character_dict)

def iterate(lexicon, parse, corpus, iterations=50, new_vocabulary=20):
	l = lexicon
	p = parse
	d = None
	for i in range(0,iterations):
		ci = ChunkerIteration(l,p,corpus)
		l, p, d = ci.start(new_vocabulary)
		print(d)
	return l.lexicon



l = iterate(cl,parse_frases,frases[0:800])
for w in l:
	print(w)