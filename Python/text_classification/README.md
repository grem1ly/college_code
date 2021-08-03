
# Text Classification - Sentiment Analysis

* [Overview](##Overview)
* [The Classifier](##The Classifier)
* [The Code](##The Code)
* [Report](##Report)

## Overview

Text classification is a form of machine learning that categorizes text into specified classes. This can be something as simple as classifying emails as either spam or not spam, or something more complex like classifying various interview transcripts as [the interviewee] fitting under specific occupations.

There are several different applications of text classification, but one of the most common and the one I focus on involves sentiment analysis. Sentiment analysis specifically involves gauging/classifying the inherent sentiment (or attitude) of various texts. They often classify text as positive, negative, or neutral, and they are extremely influential for businesses such that they can easily track consumer behavior (e.g. attitudes towards specific products) and adjust decisions to sway them favorably.

I have created a rather simple binary text classifier that categorizes movie reviews as either being positive or negative. Essentially, it evaluates the language within each review, and identifies the overall polarity (i.e. positive or negative) based on a set of priors determined by a training set (i.e. movie reviews that are pre-annotated as either positive or negative).

## The Classifier

To classify a given review, we essentially want to evaluate the probability that it is positive and (separately) the probability that it is negative and then compare the results to identify which classification is more likely. Another way to think about this is to evaluate the probability of each class (e.g. positive, negative) given the movie review. The equation below represents the calculation needed to determine the probability of the positive class given a review<sup id="ref1">[1](#foot1)</sup>:

![Equation](/images/eq1.PNG)

The numerator of this equation:

![Numerator](/images/num.PNG)

includes a prior (i.e. *P(positive)*), calculated from the pre-annotated movie reviews, and a review specific calculation given the positive class (i.e. *P(review|positive)*). The calculation of the positive prior is extremely straightforward: simply take the number of positive reviews and divide that by the total number of reviews. Determining the probability of the review given the positive class is a little more complex. The equation for this is as follows:

![Conditionals](/images/cond_prob.PNG)

Specifically, we take each word within the review and calculate/retrieve the probability of their occurrence across the pre-annotated positive reviews. For instance, say the word "great" appears in the movie review and we want to determine the probability of it occurring given the positive class (i.e. *P(great|positive)*). We take the pre-annotated positive movie reviews, count how many times the word "great" appears, and then divide that by the total number of words (within that class). This is referred to as a conditional probability, meaning that the probability of the word "great" is conditioned on the positive class. In terms of the entire movie review, we find the conditional probabilities of every word and then multiply them together. This equation represents a bag-of-words model, such that it takes into account every word within a given review, but not the order in which they are written. This follows the naive bayes assumption that words are independent from each other. Now how the equation is written (i.e. word 1 followed by word 2, etc.) may imply order, but each conditional probability is independent of context (i.e. they could be switched around and the result would not change).

There are at least two additional factors that need to be taken into consideration before running the classifier: Smoothing and Underflow. These are explained below.

### Smoothing

As a reminder, the numerator of this equation is:

![Numerator](/images/num.PNG)

which can also be represented as the positive prior multiplied by the individual conditional probabilities:

![Numerator_long](/images/num2.PNG)

So, when classifying a movie review, what would happen if an occurring word isn't present in any of the pre-annotated movie reviews? Well, we'd end up with a conditional probability of 0, thus, a numerator of 0, thus a 0 probability of the review being positive. This type of situation doesn't exactly make for good classifications given the drastic effect of just one word. Therefore, most classifiers implement some type of smoothing to account for this.

This specific classifier implements add-one smoothing. It's not the best solution, but it's a good introduction to the practice. Add-one smoothing, or any kind of smoothing, alters the calculation of the conditional probabilities. Before, we essentially took the frequency of a word and divided that by the total number of words. With add-one smoothing, we take the frequency of a word plus one, and divide that by the total number of words (i.e. tokens) plus the size of the vocabulary (i.e. types: every word that occurs at least once) across both the positive and negative pre-annotated movie reviews. The difference is displayed below, where *n* represents the frequency of the word in question, *N* represents the total number of words, and *k* represents the vocabulary.

No Smoothing                                                     |  Add-One Smoothing
:---------------------------------------------------------------:|:----------------------------------------------------:
![Without_smoothing](/images/no_smooth.PNG)                      |  ![Smoothing](/images/smooth.PNG)

### Underflow

Let's say you have a training set (i.e. pre-annotated reviews) with thousands or millions of extremely long reviews, thus a large number of words. Any time you calculate the conditional probability of a rare word, or a word that appears less than say 2% of the time, for instance, the conditional probability could be extremely small, even too small to be represented. Therefore, it's best to log the conditional probabilities and then add them together.

![Log](/images/log.PNG)

Since the conditional probabilities are all logged, in terms of the numerator, it's also best to log the positive prior and add that when appropriate.

### Classification

When comparing the probabilities of a specific review belonging to the different classes to determine the more likely classification, the denominator *P(review)* is the same in both cases. It can be represented specifically by:

![Denominator](/images/den.PNG)

but the values for both denominators in *P(positive|review)* and *P(negative|review)* will be equal.

Therefore, only the numerators are essential for comparison. A common way to represent this comparison and to identify what is the most likely class a review belongs to is with the equation:

![Argmax](/images/argmax.PNG)

where arg max, a common mathematical function, identifies the class with the largest predictability.

Under the hood, at least with this classifier, it simply compares *P(positive)P(review|positive)* and *P(negative)P(review|negative)* and returns the classification with the higher probability.

### Accuracy

After testing any classifier, it's essential to calculate its accuracy, assuming a key is available that identifies the correct classifications. To calculate simple accuracy, you would just take the number of correct predictions and divide that by the total number of predictions. This isn't exactly informative, however, as it provides no insight about the specific classes. Therefore, better measures include calculating the precision, the recall, and finally, the F-score (combines precision and recall) of each class.

For the positive class in this classifier, precision is the fraction of movie reviews correctly classified as positive out of all the reviews predicted to be positive.

![Precision](/images/precision.PNG)

For the positive class in this classifier, recall is the fraction of movie reviews correctly classified as positive out of all the reviews that are actually positive.

![Recall](/images/recall.PNG)

The F-score for this particular classifier identifies a happy medium of sorts between precision and recall. The equation for this is as follows:

![F1](/images/f1.PNG)

The F-scores for the positive and negative classes in this classifier are around 0.6 and 0.4, respectively. This is extremely bad for a classifier, but for the purposes of learning how to design your own text classifier, it's a good start.

## The Code

 * The scripts to train, test, and calculate the accuracy of the classifier are in [/scripts](/scripts/nbtrain.py).
 * The training, test, and development data (sets) are in [/data](/data/devkey.txt), with `devkey.txt` as the test key.
 * All the output is stored in [/output](/output/predictions.txt). This includes `sentiment.nb`, created from [`nbtrain.py`](/scripts/nbtrain.py) which contains the model used to classify the test set. It also includes the output of [`nbtest.py`](/scripts/nbtest.py), which holds the classifier's predictions of the test set.

## Report

Check out the research project a few of my fellow students and I worked on that made use of a text classifier to analyze word variation across occupations: [Report](/report.pdf)

 </br></br>

 <b id="foot1">1</b> All following equations and explanations specifically involve the positive class, and they should be adapted accordingly for the negative class. [↩](#ref1)
