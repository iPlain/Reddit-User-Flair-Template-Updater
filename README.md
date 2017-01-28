# Reddit userflair template updater
A simple python script to re-order the user flair templates of a subreddit by reading from a csv file.

Requires Python 3 and PRAW 4.
Remove the config.default.ini to config.ini, then update the config file to include your login info and desired subreddit.
Add a csv file with the format "flair_text;css_class", with each new flair on a new line.