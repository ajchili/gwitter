import twitter
import re

api = twitter.Api(consumer_key='',
                  consumer_secret='',
                  access_token_key='',
                  access_token_secret='')

gender = '' # male or female
names = tuple(open('{}s.txt'.format(gender), 'r'))
f = open('{}_tweets.txt'.format(gender), 'w+', encoding='utf-16')

for name in names:
    name = name.replace('\n', '')
    print('Current handle: {}'.format(name))
    statuses = api.GetUserTimeline(screen_name=name,
                               count=300,
                               include_rts=False)
    for status in statuses:
        f.write(re.sub(r'\s+', ' ', status.text) + '\n')

f.close()
