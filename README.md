# Reddit userflair template updater
A simple python script to re-order the user flair templates of a subreddit by reading from a csv file.

Requires Python 3 and PRAW 4.

Rename the config.default.ini to config.ini, then update the config file to include your login info and desired subreddit.

You can now run output_current.py, which will output the existing flair selector options to a file called out.csv

Add a csv file with the format "flair_text;css_class", with each new flair on a new line, as will be seen in out.csv, named accordingly to the config, default is userflair_templates.csv