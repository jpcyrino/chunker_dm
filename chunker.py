from chunker_dm import Chunker
from time import process_time
import sys
import csv

def chunk(file, n_iterations=20, morph=False):
	corpus = open(file, encoding="utf-8", mode="r").read()
	ch = Chunker(corpus)
	start = process_time()
	lexicon = ch.start(morph=morph, n_iterations=n_iterations)
	end = process_time()
	print("O chunker levou " + str(end-start) + " segundos para rodar")
	return lexicon.lexicon, ch.details


def results_to_csv(lexicon, details):
	with open("lexicon.csv", "w") as lexicon_file: 
		writer = csv.writer(lexicon_file)
		for key, value in dict(lexicon).items():
			writer.writerow([key, value])

	with open("details.csv", "w") as details_file:
		keys = details[0].keys()
		dict_writer = csv.DictWriter(details_file, keys)
		dict_writer.writeheader()
		dict_writer.writerows(details)



if __name__ == "__main__":
	file = sys.argv[1]
	iterations = 20
	if len(sys.argv) == 3:
		iterations = sys.argv[2]
	if len(sys.argv) == 4:
		iterations = sys.argv[2]
		morph = True if sys.argv[3] == "morph" else False
	lexicon, details = chunk(file, n_iterations=int(iterations), morph=morph)
	results_to_csv(lexicon, details)