import praw
import configparser
import csv


config = configparser.ConfigParser()
config.read('config.ini')

USERAGENT = 'script:userflair_template_grabber:1.0 (by /u/iPlain)'
username = config['Login']['username']
password = config['Login']['password']
client_id = config['Login']['client_id']
client_secret = config['Login']['client_secret']

target_subreddit = config['Misc']['target_subreddit']

r = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=USERAGENT, username=username, password=password)

sub = r.subreddit(target_subreddit)

templates = praw.models.reddit.subreddit.SubredditFlairTemplates(sub)


with open('out.csv', 'w', newline = '') as csvfile:
	w = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	for t in templates:
		w.writerow([t['flair_text'], t['flair_css_class']])