# LongevityInTime
![result](https://user-images.githubusercontent.com/76619772/170886212-aced2842-1a37-4f93-8588-4c21780beb56.png)

I have completed the task called "mental health web scrape" in the AI part. 

Firstly, I was going to use Scrapy to scrape Twitter (I have experience on Scrapy), but after searching on the internet, I found a better(easier) way to scrape Twitter by using "Twint" which is quite better than Twitter API since Twitter API has limitations regarding the number of tweets a user can scrape. Then, I scraped 10000 tweets which include the phrase "mental health". 

Secondly, Natural Language Processing tecniques have been applied on these raw data. At first, I have jointed hastags and the tweets' contents. Then, punctuations and stopwords have been removed by using NLTK library. Also, all uppercase characters in the string have been converted into lowercase characters. After applying tokenization to each texts, every word has been lemmatized by NLTK's Wordnet lemmatizer. 

Lastly, this preprocessed data has been analyzed in the analyzer.py file. I have counted each occurrence of the listed diseases or disorders which are mainly "anxiety","depression","bipolar disorder","schizophrenia","psychosis","dementia","autism","eating disorder","obsessive compulsive disorder" and "paranoia". Then, I have used matplotlib to visualize the result.
