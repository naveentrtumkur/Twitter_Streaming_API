import langid 
try:
    import json
except ImportError:
    import simplejson as json

# We use the file saved from last step as example
tweets_fn = 'twitter_ten_1000_tweets'
tweets_file = open(tweets_fn, "r")
d={}
d_langid={}
for line in tweets_file:
    try:
        # Read in one line of the file, convert it into a json object 
        tweet = json.loads(line.strip())
        if 'text' in tweet: # only messages contains 'text' field is a tweet
            #print tweet['lang'] # This is the tweet's id
            if tweet['lang'] in d.keys():
                d[tweet['lang']]=d.get(tweet['lang'], 0)+1
            else:
                d[tweet['lang']]=1
            #print tweet['created_at'] # when the tweet posted
	    # Printing of when the tweet was created and tweet posted.
            #print tweet['text'] # content of the tweet
            classify=langid.classify(tweet['text'])
            classify=classify[0]
            if classify in d_langid.keys():
                d_langid[classify]=d_langid.get(classify, 0)+1
            else:
                d_langid[classify]=1
            #print tweet['user']['id'] # id of the user who posted the tweet
            #print tweet['user']['name'] # name of the user, e.g. "Wei Xu"
            #print tweet['user']['screen_name'] # name of the user account, e.g. "cocoweixu"

            #hashtags = []
            #for hashtag in tweet['entities']['hashtags']:
            #    hashtags.append(hashtag['text'])
            #print hashtags

    except:
        # read in a line is not in JSON format (sometimes error occured)
        continue


data_modified=STRING_DATA = dict([(str(k), v) for k, v in d.items()])
print (d)
print (data_modified)
sum=0
for key,value in data_modified.items():
    sum+=value 
print (sum)
print (d_langid)
sum=0
for key,value in d_langid.items():
    sum+=value
print (sum)
