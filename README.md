# NLP_26_PROJECT_10
Repo for NLP project 10 by Akseli, Tino and Kasperi



### Project instructions:

### Project 10: Zips Law distribution in food domain.
## This project investigates various facets of the Zips law and how it can be empirically tested on a set of well-
## known corpuses.

# Download the Suomi24 dataset from The Suomi24 Corpus 2001-2017, VRT version 1.1 – META-SHARE (csc.fi).
# You should click on the access location http://urn.fi/urn:nbn:fi:lb-2020021802
# Select University of Oulu in Korp and then login with your university credential to have access to the data. The
# data is quite large 65GB, so you should make sure that either your local computer (s) or cloud server account
# will be able to handle it and run basic search.

1. Consider the Fineli database of Finnish food maintained by THL, which includes over 4000 foods and
their nutrition intake, see Frontpage - Fineli, for database access and detail. Write a script that search for
food entries (Fineli) in Suomi24 and retrieve the threads and messages where these foods occurred
together with the associated date of the threads. Now we want to investigate the occurrence of these
foods over time. Write a script that gathers the foods occurred monthly and calculate the total nutrition
intake by summing up the corresponding nutrition intake of each food according to Fineli database, and
draw the graph of timely evolution (monthly) of the nutrition intake according to the mentioned food.

2. Write a script that gathers the thread titles associated with the identified foods in 1) in each month to
form a single dataframe (for each month). Now we want to determine the sentiment polarity of each
dataframe. For this purpose, use the AFINN model for sentiment analysis that employs simple lexicon-
based approach, see implementation in GitHub - fnielsen/afinn: AFINN sentiment analysis in Python, to
determine the overall monthly when inputting each dataframe. Draw the evolution of sentiment score
and nutrition intake on the same plot, and calculate the Pearson correlation to evaluate the correlation
between the two entities.

3. Repeat 2) when considering yearly evolution of sentiment and nutrition intake instead of monthly
evolution. Comment on whether further refinement of the timely evolution can illustrate correlation
between the two entities.

4. Now we want to explore the food diversity according to the records in 1). For this purpose, write a script
that calculates the number of distinct foods in each dataframe (monthly), and then draw on the same plot
the timely evolution of the food diversity and nutrition intake, and then calculates the Pearson
correlation between the two entities. Repeat this process when yearly evolution is considered instead of
monthly evolution.

5. The use of Fineli for quantifying food diversity may not be ideal, propose your own manual
categorization based on your understand of the various types of foods mentioned in Fineli, and then re-
process specification 4) accordingly.

6. Now we want to explore the asymptotic behavior of the vocabulary employed in 1). For this purpose,
suggest a script that calculates the vocabulary size of thread titles gathered in month 1, in month 1 and 2,
in month 1, 2 & 3, and so on. Next write a scripts that shows the evolution of the vocabulary size with
respect to number of tokens in Month 1, Month 1 &2, Month 1, 2 & 3, and so on, and study the fitting of
the Heap’s law. Evaluate the goodness of fit using R-squared and adjusted R-squared statistics.

7. Write a script that computes the length of thread titles identified in 1) and suggest a 20 bin subdivision
of the length size. Then construct the graph of the frequency of each bin with respect to the ranking, and
study the fitting of Zipfs’ law distribution. Provide the corresponding R-squared and adjusted R-squared
statistics.

8. Suggest your own initiative to apply more advanced LLMs or transformer-based approach to study the
nutrition content of food mentioned in Suomi24 search outcome. Especially, devise the prompting
strategy to identify the foods liked and disliked by users, and then report the yearly evolution of the
(average over total number of items) nutrition score for both liked items and disliked ones.

9. Identify from your reported literature state of the art method that you can accommodate to achieve any
of specification above. Motivate your answers and manipulations by appropriate literature citation.