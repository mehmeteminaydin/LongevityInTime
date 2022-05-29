#visualize the results by using matplotlib
import matplotlib.pyplot as plt

#read file provided by preprocess.py
import pandas as pd
df = pd.read_csv('preprocessed.csv')

disorder_list = {"anxiety":0,"depression":0, "bipolar":0,"schizophrenia":0, 
                "psychosis":0, "dementia":0,"autism":0,
                "eating":0,"ocd":0,"paranoia":0}

#count how many times each of the diseases occured in the tweets in conjuction with mental health
for index, row in df.iterrows():
    for word in row['preprocessed'].split():
        for name in disorder_list:
            if(name == word):
                disorder_list[name] += 1

#scaling values between 0-100
total = sum(disorder_list.values())

for name in disorder_list:
    disorder_list[name] = (disorder_list[name]/total)*100

plt.bar(range(len(disorder_list)), list(disorder_list.values()), color = 'blue')
plt.xticks(range(len(disorder_list)), list(disorder_list.keys()), rotation='vertical')
plt.xlabel("Diseases or Disorders")
plt.ylabel("Percentage of Occurences")
plt.savefig('result.png', bbox_inches='tight')

    

