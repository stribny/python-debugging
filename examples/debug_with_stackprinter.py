"""
We can use stackprinter (https://github.com/cknd/stackprinter/) to enhance
the printed information that we get when an exeption is thrown

How to use:
- run the script with `python debug_with_stackprinter.py`
- observe a different stack trace printed in the console
"""

# The output:
# File debug_with_stackprinter.py, line 22, in <module>
#     18   def process_words(words_to_process):
#     19       for i, word in enumerate(words_to_process):
#     20           processed_word = str.capitalize(word)
#     21   
# --> 22   process_words(words)
#     ..................................................
#      words = ['debugging', 'with', 'stackprinter', 42, ]
#     ..................................................

# File debug_with_stackprinter.py, line 20, in process_words
#     18   def process_words(words_to_process):
#     19       for i, word in enumerate(words_to_process):
# --> 20           processed_word = str.capitalize(word)
#     ..................................................
#      words_to_process = ['debugging', 'with', 'stackprinter', 42, ]
#      i = 3
#      word = 42
#      processed_word = 'Stackprinter'
#     ..................................................

# TypeError: descriptor 'capitalize' requires a 'str' object but received a 'int'

import stackprinter
stackprinter.set_excepthook(style='darkbg2')

words = ['debugging', 'with', 'stackprinter', 42]

def process_words(words_to_process):
    for i, word in enumerate(words_to_process):
        processed_word = str.capitalize(word)

process_words(words)