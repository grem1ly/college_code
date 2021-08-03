# HW 2: Text classification (part 1)            Emily Strand

# Import the proper modules:
    # glob for reading in multiple files
    # nltk for tokenizing the text
    # pickle for saving our created model to be used later

import glob
import nltk
import pickle


# Positive Files

pos_file_names = glob.glob('../data/train/pos/*')

total_pos_tokens = []


# Read the positive text files in your training set - use a for loop to iterate
    # through all the files within the directory specified above by glob.glob

for file in pos_file_names:
    pos_file = open(file, encoding = 'utf_8')
    pos_text = pos_file.read()
    
# Tokenize the text using NLTK - with the empty list defined outside of
    # the loop (total_pos_tokens), we add and store all the tokens for
    # each file to be used when creating the frequency distribution
    
    pos_tokens = nltk.word_tokenize(pos_text)
    total_pos_tokens = total_pos_tokens + pos_tokens
    
# Create a frequency distribution for all the positive reviews

pos_fd = nltk.FreqDist(total_pos_tokens)

# Calculate the number of positive samples in the training set - gives
    # us the P(pos) prior in reference to the negative samples

pos_count = len(pos_file_names)



# Negative Files
    # Follow the same steps as above

neg_file_names = glob.glob('../data/train/neg/*')

total_neg_tokens = []

for file in neg_file_names:
    neg_file = open(file, encoding = 'utf_8')
    neg_text = neg_file.read()
    neg_tokens = nltk.word_tokenize(neg_text)
    total_neg_tokens = total_neg_tokens + neg_tokens

neg_fd = nltk.FreqDist(total_neg_tokens)

neg_count = len(neg_file_names)



# Create a dictionary with the four keys specified below - these refer
    # to the two variables defined after each of the for loops

model = {
    'pos_count': pos_count,
    'neg_count': neg_count,
    'pos_fd': pos_fd,
    'neg_fd': neg_fd
}

print(model)

# With the line of code below, save the model to be used later for classification

pickle.dump(model, open('../output/sentiment.nb', 'wb'))
