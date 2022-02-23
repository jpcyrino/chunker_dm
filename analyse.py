from chunker_dm.analyser import Analyser
from chunker_dm.utilities import create_lexicon_from_text_file
from time import process_time
	

L = create_lexicon_from_text_file("biblia-em-txt.txt")
A = Analyser(L)
frase = input("Qual frase você quer analisar? ")
start = process_time()
frase_analisada = A.analyse(frase)
end = process_time()
frase_print = " ".join(frase_analisada)
print("\nfrase analisada: " + frase_print)
print("| custo total: " + str(A.total_cost))
print("A consulta levou " + str(end-start) +" segundos")












