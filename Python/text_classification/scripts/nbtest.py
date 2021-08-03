# HW 3: Text classification (part 2)        Emily Strand


# Import the proper modules:
    # pickle for loading the sentiment.nb file
    # glob for reading in multiple files
    # nltk for tokenizing the text
    # math for taking the log of the class and conditional probabilities
import pickle
import glob
import nltk
import math



# Create an output file that will store the test files and their predicted class
output_file = open('../output/predictions.txt', 'w')

# Open the model created from part 1 to classify the test set
model = pickle.load(open('../output/sentiment.nb', 'rb'))

# Calculate the priors based on the positive and negative file counts of the training set (stored in the model)
pos_prior = model['pos_count'] / (model['pos_count'] + model['neg_count'])
neg_prior = model['neg_count'] / (model['pos_count'] + model['neg_count'])

# Obtain a comprehensive frequency distribution of the training data
    # Use this later for add-one smoothing (need the total number of types of both classes)
fd = model['pos_fd'] + model['neg_fd']



# Access the directory containing the files to be classified
test_files = glob.glob('../data/test/*')


# Create two "empty" variables to be later used in calculating P(review|class)
    # Need to continously add the log of the conditional properties of each word within this variable
cond_probs_pos_sum = 0
cond_probs_neg_sum = 0



# Create a for loop that will open, read, and tokenize each review
for file in test_files:
    test_file = open(file, encoding = 'utf_8')
    test_text = test_file.read()
    test_tokens = nltk.word_tokenize(test_text)

# Create a for loop within the for loop in order to iterate through each token in each review
    # Calculate the conditional probability of each word/token (with add-one smoothing) for each class
    # Using the "empty" variables created outside the loops,
    # take the log of each conditional probability and add them together
    for token in test_tokens:
        cond_prob_pos = (model['pos_fd'][token] + 1) / (model['pos_fd'].N() + fd.B())
        cond_prob_neg = (model['neg_fd'][token] + 1) / (model['neg_fd'].N() + fd.B())
        cond_probs_pos_sum = cond_probs_pos_sum + math.log(cond_prob_pos)
        cond_probs_neg_sum = cond_probs_neg_sum + math.log(cond_prob_neg)
        
# Back within the first loop, calculate P(class|review) by adding the already summed (logged) conditional probabilites
    # for each class to the log of their respective prior
    prob_pos_given_review = math.log(pos_prior) + cond_probs_pos_sum
    prob_neg_given_review = math.log(neg_prior) + cond_probs_neg_sum

# Using a conditional statement, within the first loop, identify which probability (pos or neg) is bigger
    # Aka the argmax
    if prob_pos_given_review < prob_neg_given_review:
        pred_label = 'neg'
    else:
        pred_label = 'pos'

# Print each file and it's label to the output_file first created at the beginning
    # (the backslashes bothered me, so I changed them to forwardslashes)
    print(file.replace('\\', '/'), pred_label, file = output_file)

# Set the summed (logged) conditional probabilites back to zero for the next file 
    cond_probs_pos_sum = 0
    cond_probs_neg_sum = 0



# Close the output_file after all the review files are classified
output_file.close()


