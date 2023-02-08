# When I ran the code to compare cat, monkey and banana:
# I found that the highest similarity was between cat and monkey.
# Followed by monkey and banana.
# The least similarity was found between cat and banana.
# I found it interesting that cat and monkey was more similar than monkey and banana.
# Also that it knew there was less similarity between cat and banana than monkey and banana.
# I made my own example up using 'bird', 'fly' and 'dog'. 'bird' and 'dog' were the most similar.
# 'bird' and 'fly' the next and the least similar were 'dog' and 'fly'.

import spacy
nlp = spacy.load('en_core_web_md')

print('''
============Compare cat, monkey and banana============
''')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

print('''
============Compare bird, fly and dog============
''')
word1 = nlp("bird")
word2 = nlp("fly")
word3 = nlp("dog")
print(word1,word2,word1.similarity(word2))
print(word3,word2,word3.similarity(word2))
print(word1,word3,word3.similarity(word1))



print('''
============Compare cat, apple, monkey and banana============
''')
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


print('''
============Compare sentences============
''')
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)