with open('orig.txt', mode="r", encoding='utf-8') as words, \
        open(r'transcr.txt', encoding='utf-8') as transcriptions, \
        open('base.txt', mode="r", encoding='utf-8') as bases, \
        open('inf.txt', mode="r", encoding='utf-8') as lemmas:
    words = words.read()
    transcriptions = transcriptions.read()
    bases = bases.read()
    lemmas = lemmas.read()

words = words.split('\n')
transcriptions = transcriptions.split('\n')
bases = bases.split('\n')
lemmas = lemmas.split('\n')
words_to_transcriptions = dict(zip(words, transcriptions))
base_to_lemma = dict(zip(bases, lemmas))


def alg(word_input):
    word_input = " " + word_input
    if word_input in words_to_transcriptions.keys():
        for w in base_to_lemma.keys():
            if w in words_to_transcriptions[word_input]:
                result = base_to_lemma[w]
    if 'с' not in word_input[-2]:
        result = result.replace('ся', '')
        result = result.replace('сь', '')
    return result


x = 'n/a'
while True:
    x = input()
    print(alg(x))
    if x() == '':
        break
