from chunker_dm import Chunker
from time import process_time
import sys
import csv

def chunk(file, n_iterations=20, n_new_words=25, morph=False):
	corpus = open(file, encoding="utf-8", mode="r").read()
	ch = Chunker(corpus)
	start = process_time()
	lexicon, parse = ch.start(morph=morph, n_iterations=n_iterations, n_new_words=n_new_words)
	end = process_time()
	print("O chunker levou " + str(end-start) + " segundos para rodar")
	return lexicon.lexicon, ch.details, parse


def results_to_csv(lexicon, details):
	with open("lexicon.txt", encoding="utf-8", mode="w") as lexicon_file: 
		# writer = csv.writer(lexicon_file)
		for key, value in dict(lexicon).items():
			# writer.writerow([key, value])
			lexicon_file.write(key + "\n")

	with open("details.csv", encoding="utf-8", mode="w") as details_file:
		keys = details[0].keys()
		dict_writer = csv.DictWriter(details_file, keys)
		dict_writer.writeheader()
		dict_writer.writerows(details)

def parse_to_txt(parse):
	with open("segmented.txt", encoding="utf-8", mode="w") as parse_file:
		for word in parse: 
			parse_file.write('-'.join(word) + '\n')

if __name__ == "__main__":
	file = sys.argv[1]
	iterations = 20
	n_new_words= 25
	if len(sys.argv) == 4:
		iterations = sys.argv[2]
		n_new_words = sys.argv[3]
	if len(sys.argv) == 5:
		iterations = sys.argv[2]
		n_new_words = sys.argv[3]
		morph = True if sys.argv[4] == "morph" else False
	lexicon, details, parse = chunk(file, n_iterations=int(iterations), morph=morph, n_new_words=int(n_new_words))
	results_to_csv(lexicon, details)
	parse_to_txt(parse)