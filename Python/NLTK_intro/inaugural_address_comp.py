# HW 1: Inaugural Assignment        Emily Strand


# 1 - Load president Washington's 1789 inaugural address

washington_file = open('./texts/1789-Washington.txt')

# 2 - Count total number of words (all tokens)

    # First the file needs to be read
    
washington_text = washington_file.read()

    # Next we have to import nltk and use word_tokenize()
    # to separate all the tokens to be added up
    
import nltk
washington_tokens = nltk.word_tokenize(washington_text)

    # The len() function can then be used to get the total count
    
washington_word_count = len(washington_tokens)
print("Washington's 1789 inaugural address word count: ", washington_word_count)
    # Output:   Washington's 1789 inaugural adress word count:  1535

# 3 - Find the 20 most frequent words (excluding non-words)

    # We use FreqDist() within nltk to first get the complete frequency distribution
    
washington_freq_dist = nltk.FreqDist(washington_tokens)

    # Then we use .mostcommon() to get the desired number of most common
    # words (we have to put in a value of 25 to take into account the
    # non-words that may appear) - results reported in the external pdf
    
washington_common_words = washington_freq_dist.most_common(25)
print(washington_common_words)

    # To make it more presentable, we can use a for loop

for word in washington_common_words:
	print("word: ", word[0], "	count: ", word[1])

# 4 - Repeat the steps above with Obama's 2009 inaugural address

obama_file = open('./texts/2009-Obama.txt')
obama_text = obama_file.read()

obama_tokens = nltk.word_tokenize(obama_text)
obama_word_count = len(obama_tokens)
print("Obama's 2009 inaugural address word count: ", obama_word_count)
    # Output:   Obama's 2009 inaugural address word count:  2701

obama_freq_dist = nltk.FreqDist(obama_tokens)
obama_common_words = obama_freq_dist.most_common(25)
print(obama_common_words)

for word in obama_common_words:
	print("word: ", word[0], "	count: ", word[1])

# 5 - Comment on the differences between the two addresses (in external pdf)
