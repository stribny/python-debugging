"""
We can use Python's logging module (https://docs.python.org/3/library/logging.html) 
to print information to a console, file or the network to examine what is happening in the program

The advantage of using logging instead of other debugging techniques is that it is suitable to 
be commited with the source and used in production

There is a lot of options we can use to configure where and how the information is printed, 
e.g. there are several log levels (debug, info, error), several formatting options (%, str.format)

How to use:
- run the script with `python debug_with_default_logging.py`
- observe state (i, processed_word) and exception printed with additional info such as name of
  the function or a line number
- observe that information is printed to the console and to a file at the same time
"""

# The output:
# DEBUG    process_words() 47	 i=0, processed_word=Debugging
# DEBUG    process_words() 47	 i=1, processed_word=With
# DEBUG    process_words() 47	 i=2, processed_word=Default
# DEBUG    process_words() 47	 i=3, processed_word=Logging
# ERROR    process_words() 49	 The word is not a string

import logging

FORMAT = '%(levelname)-8s %(funcName)s() %(lineno)d\t %(message)s'
formatter = logging.Formatter(FORMAT)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

file_handler = logging.FileHandler("log.txt")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

words = ['debugging', 'with', 'default', 'logging', 42]

def process_words(words_to_process):
    for i, word in enumerate(words_to_process):
        try:
            processed_word = str.capitalize(word)
            logger.debug('i=%d, processed_word=%s', i, processed_word)
        except TypeError:
            logger.error('The word is not a string')

process_words(words)