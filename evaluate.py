from sys import argv
from statistics import mean
from chunker_dm import Chunker

def preprocess(filename):
    with open(filename, encoding="utf-8", mode="r") as file:
        lines = file.read().split('\n')
    lines = [lines[i] for i in range(0,len(lines),3)]
    words = []
    for line in lines:
        line = line.lower()
        words += line.split(' ')
    return words

def create_lexicon(words):
    lexicon = set()
    for word in words:
        lexicon = lexicon | set(word.split('-'))
    return lexicon, len(lexicon)

def chunk(words, new_words=20):
    words_as_string = '\n'.join(words)
    chunker = Chunker(words_as_string)
    lexicon, parse = chunker.start(True, 25, new_words)
    return lexicon, parse

def compare_lexicons(chunker_lexicon, linguist_lexicon): 
    common_lexicon = chunker_lexicon & linguist_lexicon
    xi = len(common_lexicon)/len(chunker_lexicon)
    gamma = len(common_lexicon)/len(linguist_lexicon)
    return xi, gamma, common_lexicon

def compare_words(chunker_words, linguist_words):
    results = []
    for n in range(0,len(chunker_words)): 
        if chunker_words[n] == linguist_words[n]: 
            results += [1]
        else: 
            results += [0]
    sigma = mean(results)
    return sigma

def run_stage(linguist_words, n_iterations):
    chunker_lexicon, chunker_words = chunk(linguist_words, n_iterations)
    return chunker_lexicon, chunker_words

def run(linguist_words, n_iterations):
    linguist_lexicon, sizeof_linguist_lexicon = create_lexicon(linguist_words)
    chunker_lexicon, chunker_words = run_stage(linguist_words, n_iterations)
    chunker_words = ['-'.join(word) for word in chunker_words]
    # Descomentar para detectar problemas...
    # print(len(chunker_words))
    # print(len(linguist_words))
    # print(list(zip(chunker_words,linguist_words))
    chunker_lexicon = set(chunker_lexicon.lexicon.keys())
    sizeof_chunker_lexicon = len(chunker_lexicon)
    xi, gamma, common_lexicon = compare_lexicons(chunker_lexicon, linguist_lexicon)
    sigma = compare_words(chunker_words, linguist_words)
    print(f"Resultado para {n_iterations} morfemas novos por rodada")
    print(f"-------------------------------------------------------")
    print(f"Comprimento do léxico do chunker: {len(chunker_lexicon)}")
    print(f"Comprimento do léxico do linguista: {len(linguist_lexicon)}")
    print(f"Comprimento do léxico comum: {len(common_lexicon)}")
    print(f"Medida ξ: {xi}")
    print(f"Medida γ: {gamma}")
    print(f"Medida σ: {sigma}")


if __name__ == "__main__":
    filename = argv[1]
    linguist_words = preprocess(filename)
    run(linguist_words, 10)
    run(linguist_words, 25)
    run(linguist_words, 50)
    run(linguist_words, 100)
    run(linguist_words, 500)
    run(linguist_words, 1000)
    run(linguist_words, 5000)
    run(linguist_words, 10000)

    



