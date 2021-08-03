# HW 4: Part-of-speech tagging              Emily Strand


# Import the proper modules:
    # nltk for everything (tokenizing, concordance tables, tagging)
import nltk


# Part 1 - concordance tables
    # Download the desired corpora from nltk
nltk.download('product_reviews_1')
nltk.download('reuters')

    # Tokenize each corpus - (I'm using the entirety of each corpus,
    # so it's not necessary to access the individual files)
product_tokens = nltk.corpus.product_reviews_1.words()
news_tokens = nltk.corpus.reuters.words()

    # Convert the tokens to nltk text and then create the concordance
    # tables using the desired focus word
product_text = nltk.Text(product_tokens)
product_text.concordance('press')

news_text = nltk.Text(news_tokens)
news_text.concordance('press')

    # Manually tag the lines of each concordance tables with the
    # appropriate part-of-speech tag for each instance of the focus word
    # (done on external pdf)




# Part 2: Parts-of-speech, automatic

    # Open and read the jabberwocky file to be tagged
jabberwocky_file = open('Jabberwocky.txt')
jabberwocky_text = jabberwocky_file.read()

    # Tokenize and tag the text
jabberwocky_tokens = nltk.word_tokenize(jabberwocky_text)
jabberwocky_tagged_text = nltk.pos_tag(jabberwocky_tokens)

    # Print each word and corresponding POS tag from the text
for word, tag in jabberwocky_tagged_text:
    print(word, tag)

    # Manually correct the incorrect tags (done on external pdf)




# Sentence Tokenization Problem: Tokenize sentences one at a time

    # Using the jabberwocky_text above,
    # tokenize the sentences first (rather than the words)
jabberwocky_sents = nltk.sent_tokenize(jabberwocky_text)

    # Loop through each sentence and tokenize the words within
    # Then get the corresponding POS tag for each word
for sent in jabberwocky_sents:
    words_per_sent = nltk.word_tokenize(sent)
    sent_tags = nltk.pos_tag(words_per_sent)
    print(sent_tags)





