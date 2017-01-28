import praw
import configparser
import csv

"""
CSV must be formatted as follows:
default_hover_text;css_class

"""

config = configparser.ConfigParser()
config.read('config.ini')

USERAGENT = 'script:userflair_template_updater:1.0 (by /u/iPlain)'
username = config['Login']['username']
password = config['Login']['password']
client_id = config['Login']['client_id']
client_secret = config['Login']['client_secret']

target_subreddit = config['Misc']['target_subreddit']

csv_file = config['Misc']['csv_file']

hovertext_editable = config['Misc'].getboolean('hovertext_editable')

r = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=USERAGENT, username=username, password=password)

sub = r.subreddit(target_subreddit)

templates = praw.models.reddit.subreddit.SubredditFlairTemplates(sub)

flairs = csv.reader(open(csv_file),delimiter=';')

templates.clear()

for row in flairs:
	templates.add(row[0],row[1],hovertext_editable)
	print('Adding: ' + row[0] + ', ' + row[1])
	