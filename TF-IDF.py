import math, re
doc1name = "Example.txt"
doc2name = "Example_2.txt"
doc3name = "Example_3.txt"
doc1 = open(doc1name)
doc1 = doc1.read()
doc2 = open(doc2name)
doc2 = doc2.read()
doc3 = open(doc3name)
doc3 = doc3.read()
score = []
doclist = doc1, doc2, doc3
wordlist = doc1.split(" ") + doc2.split(" ") + doc3.split(" ")
for i in range(0, len(wordlist)):
    wordlist[i] = re.sub("\\n", " ", wordlist[i])
    wordlist[i] = re.sub("_", " ", wordlist[i])
wordlist = re.findall("\w+", str(wordlist))
k = 1


def tf(word, doc):
    return doc.count(str(word)) / len(doc)


def n_contains(word, doclist):
    return sum(1 for doc in doclist if str(word) in doc)


def idf(word, doclist):
    return math.log(len(doclist) / (1 + n_contains(word, doclist)))


def tfidf(word, doc, doclist):
    return tf(word, doc) * idf(word, doclist)
for i, doc in enumerate(doclist):
    for j in range(0, len(wordlist)):
        score.append(tfidf(j, doc, doclist))
for i, doc in enumerate(doclist):
    if i == 0:
        documentname = doc1name
    elif i == 1:
        documentname = doc2name
    else:
        documentname = doc3name
    print("Top three words in {}:".format(documentname))
    scores = {word: tfidf(word, doc, doclist) for word in wordlist}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:3]:
        if k == 1:
            l = "H"
        elif k == 2:
            l = "Second h"
        else:
            l = "Third h"
        print("\t{}ighest TF-IDF: \"{}\" (TF-IDF = {})".format(l, word, round(score, 5)))
        if k < 3:
            k += 1
        else:
            k = 1
