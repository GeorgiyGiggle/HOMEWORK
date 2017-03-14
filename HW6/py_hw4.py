from datetime import datetime, timedelta
import logging
from argparse import ArgumentParser
import os

# Birthday of an asshole
now = datetime.now()
friend_birthday = "2017-03-18"
formatted_friend_birthday = datetime.strptime(friend_birthday, "%Y-%m-%d")
if formatted_friend_birthday < now + timedelta(weeks=1):
    print("Get ready a chocolate cake")
else:
    print("Nah, still a lot of time to waste")

# Logging issues because of shitty code
logging.basicConfig(filename='log.log', filemode='w',
                    format='%(asctime)s - (%(message)s)', datefmt='%m/%d/%Y | %I:%M | %p',
                    level=logging.DEBUG)

logging.info("Info message")
logging.warning("Warning message")
logging.debug("Debug message")
logging.error("Error message")
logging.critical("Critical message")

# Argparse (NOT DONE)
parser = ArgumentParser()
parser.add_argument("-l", "--level", dest="input_filename",
                    help="input filename")
args = parser.parse_args()
print(args)
print(args.input_filename)

# Changing string format (NOT DONE)
birthday = "2017 03 18"
formatted_birthday = datetime.strptime(birthday, "%Y %m %d")
print(formatted_birthday)

# Directory list and file list
path = "F:/tools/CODING/HW6/"
directory = os.listdir(path)
filelist = []
dirlist = []
for item in directory:
    if os.path.isfile(item):
        filelist.append(item)
    elif os.path.isdir(item):
        dirlist.append(item)
print(filelist)
print(dirlist)

