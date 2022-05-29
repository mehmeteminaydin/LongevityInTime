import twint

c = twint.Config()

c.Search = ['mental health']       # topic
c.Limit = 10000     # number of Tweets to scrape
c.Store_csv = True       # store tweets in a csv file
c.Output = "mental_health.csv"     # path to csv file

twint.run.Search(c)