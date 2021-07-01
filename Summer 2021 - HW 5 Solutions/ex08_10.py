positive = 'amazing,beautiful,happy,wonderful,delight'
positive_words = positive.split(',')

negative = 'annoying,bad,terrible,weak,insane'
negative_words = negative.split(',')

sentence = input('Input Sentence: ')

words = sentence.split()

pos_count = 0
neg_count = 0


for i in range(0,len(words)):
    for j in range(0, len(positive_words)):
#        print(words[i],positive_words[j])
        if words[i]==positive_words[j]:
#            print(j)
            pos_count += 1
    for k in range(0, len(negative_words)):
        if words[i]==negative_words[k]:
            neg_count += 1


if pos_count > neg_count:
    print('Positive Sentiment')
elif neg_count > pos_count:
    print('Negative Sentiment')
