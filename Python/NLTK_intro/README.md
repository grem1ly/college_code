# NLTK Intro

The Natural Language Toolkit (NLTK) is a wildly popular collection of libraries used for all things Natural Language Processing (NLP) - a form of artificial intelligence that enables computational processing of human languages.

There are countless applications for which NLTK can be used (e.g. tokenization, POS tagging), but this particular script ([`inaugural_address_comp.py`](./inaugural_address_comp.py)) and application is great for familiarizing yourself with the most basic methods of tokenization and creating frequency distributions, as well as learning how to analyze the output in interesting and appropriate ways.

This script enables the parsing, so to speak, and the creation of frequency distributions of inaugural addresses (or really any piece of text), which is useful for analyzing the vocabulary used in different time periods. We specifically look at the most frequently used words.

## The Analysis (Washington's 1798 inaugural address vs. Obama's 2009 inaugural address)

The most salient aspect about both these distributions is that the most frequent words are function words rather than content words. So, all the words that appear are strictly used to construct the grammar of the addresses, not necessarily what they’re about. In this regard, the two addresses are extremely similar just like millions of other long bodies of texts. That being said, there was one noticeable difference between the two addresses, which primarily has to do with the chosen pronouns. Based on the twenty most common words, Washington implements first person singular pronouns ("I" and "my"), whereas Obama implements first person plural pronouns ("our," "we," and "us"). Maybe this has something to do with the drastic difference in time period and what the objectives were for the country at that time or it could be down to Obama and Washington’s dispositional differences, but from what I can tell, this seems to be the only discernable distributional difference.
