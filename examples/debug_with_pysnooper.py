"""
We can use PySnooper (https://github.com/cool-RR/pysnooper) to automatically
print the state of the program as it is executed line by line

Many options exists to configure the output

How to use:
- run the script with `python debug_with_pysnooper.py`
- observe the state of the program as it is executed printed in the console
"""

# The output:
# Starting var:.. words_to_process = ['debugging', 'with', 'PySnooper']
# 12:04:18.919933 call        15 def process_words(words_to_process):
# 12:04:18.920111 line        16     for i, word in enumerate(words_to_process):
# New var:....... i = 0
# New var:....... word = 'debugging'
# 12:04:18.920229 line        17         processed_word = str.capitalize(word)
# New var:....... processed_word = 'Debugging'
# 12:04:18.920332 line        16     for i, word in enumerate(words_to_process):
# Modified var:.. i = 1
# Modified var:.. word = 'with'
# 12:04:18.920437 line        17         processed_word = str.capitalize(word)
# Modified var:.. processed_word = 'With'
# 12:04:18.920526 line        16     for i, word in enumerate(words_to_process):
# Modified var:.. i = 2
# Modified var:.. word = 'PySnooper'
# 12:04:18.920635 line        17         processed_word = str.capitalize(word)
# Modified var:.. processed_word = 'Pysnooper'
# 12:04:18.920754 line        16     for i, word in enumerate(words_to_process):
# 12:04:18.920846 return      16     for i, word in enumerate(words_to_process):
# Return value:.. None

import pysnooper

words = ['debugging', 'with', 'PySnooper']

@pysnooper.snoop()
def process_words(words_to_process):
    for i, word in enumerate(words_to_process):
        processed_word = str.capitalize(word)

process_words(words)