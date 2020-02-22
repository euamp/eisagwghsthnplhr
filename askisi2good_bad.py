from collections import Counter
def good_bad(text):
    vowels = ('a', 'e', 'i', 'o', 'u')
    bad = ('f','c','k','r')
    dict_words={}
    list_of_words = text.split(' ')
    for word in list_of_words:
        if len(word)<=2:
             dict_words[word] = 'good'
        else:
            no_vowels = ''.join([l for l in word.lower() if l not in vowels])
            wc = Counter(no_vowels)
            s = max(wc.values()) 
            i = list(wc.values()).index(s)
            most_occured = no_vowels[i]
            if most_occured in bad:
                dict_words[word] = 'bad'
            else:
                dict_words[word] = 'good'
    for i,j in dict_words.items():
        print ('The word {} is {}'.format(i,j))


'''
with open('check.txt', 'r') as file:
    data = file.read().replace('\n', '')
good_bad(data)
'''
