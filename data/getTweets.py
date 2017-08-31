import twitter
import re

api = twitter.Api(consumer_key='',
                  consumer_secret='',
                  access_token_key='',
                  access_token_secret='')

name = ''
f = open('eval_tweets.txt', 'w+', encoding='utf-16')

statuses = api.GetUserTimeline(screen_name=name,
                               count=50,
                               include_rts=False)
for status in statuses:
    f.write(re.sub(r'\s+', ' ', status.text) + '\n')

f.close()
