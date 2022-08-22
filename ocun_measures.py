from sys import argv
from statistics import mean


def preprocess(filename):
    with open(filename, encoding="utf-8", mode="r") as file:
        lines = file.read().split('\n')
    lines = [lines[i] for i in range(0,len(lines),3)]
    words = []
    for line in lines:
        line = line.lower()
        words += line.split(' ')
    return words

def preprocess_glosses(filename):
    with open(filename, encoding="utf-8", mode="r") as file:
        lines = file.read().split('\n')
    lines = [lines[i] for i in range(1,len(lines),3)]
    glosses = []
    for line in lines:
        line = line.lower()
        glosses += line.split(' ')
    return glosses

def fusion_per_morpheme(glosses):
    morphemes = []
    for gloss in glosses: 
        morphemes += gloss.split('-')
    n_fusions = 0
    for morpheme in morphemes:
        split_on_fusion = morpheme.split('.') 
        fusions = len(split_on_fusion)-1
        n_fusions += fusions
    return n_fusions/len(morphemes)

def mean_morpheme_exponence(glosses):
    morphemes = []
    for gloss in glosses: 
        morphemes += gloss.split('-')
    n_fusions = []
    for morpheme in morphemes:
        split_on_fusion = morpheme.split('.') 
        fusions = len(split_on_fusion)
        n_fusions.append(fusions)
    return sum(n_fusions)/len(n_fusions)



def n_words(words):
    return len(words)

def m_morphemes_per_word(words):
    n_morphemes = []
    for word in words:
        morphemes = word.split('-')
        n_morphemes.append(len(morphemes))
    return mean(n_morphemes)

def p_monomorphemic_words(words):
    n_monomorphemic = 0
    for word in words:
        morphemes = word.split('-')
        if(len(morphemes) == 1): n_monomorphemic += 1
    return n_monomorphemic/len(words)

if __name__ == "__main__":
    fname = argv[1]
    words = preprocess(fname)
    print(f"Número de palavras: {n_words(words)}")
    print(f"Média de morfemas por palavra: {m_morphemes_per_word(words)}")
    print(f"Proporção de palavras monomorfêmicas: {p_monomorphemic_words(words)}")
    glosses = preprocess_glosses(fname)
    print(f"Proporção de fusões por morfema: {fusion_per_morpheme(glosses)}")
    print(f"Exponência média dos morfemas: {mean_morpheme_exponence(glosses)}")


