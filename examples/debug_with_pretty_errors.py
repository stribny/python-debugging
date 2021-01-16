"""
We can use PrettyErrors (https://github.com/onelivesleft/PrettyErrors) to enhance
the printed information that we get when an exeption is thrown

How to use:
- run the script with `python debug_with_pretty_errors.py`
- observe a different stack trace printed in the console
"""

# The output:
# ********************************************************************************************************************
# 31 <module> /home/pstribny/playground/python-debugging/examples/debug_with_pretty_errors.py
# "/home/pstribny/playground/python-debugging/examples/debug_with_pretty_errors.py", line 31
# > process_words(words)

# 29 process_words /home/pstribny/playground/python-debugging/examples/debug_with_pretty_errors.py
# "/home/pstribny/playground/python-debugging/examples/debug_with_pretty_errors.py", line 29
  
#   words = ['debugging', 'with', 'stackprinter', 42]
  
#   def process_words(words_to_process):
#       for i, word in enumerate(words_to_process):
# >         processed_word = str.capitalize(word)
  
#   process_words(words)

# word: 42
# i: 3
# words_to_process: ['debugging', 'with', 'stackprinter', 42]
# processed_word: Stackprinter

# TypeError:
# descriptor 'capitalize' for 'str' objects doesn't apply to a 'int' object

import pretty_errors

pretty_errors.configure(
    separator_character = '*',
    filename_display    = pretty_errors.FILENAME_EXTENDED,
    line_number_first   = True,
    display_link        = True,
    lines_before        = 5,
    lines_after         = 2,
    line_color          = pretty_errors.RED + '> ' + pretty_errors.default_config.line_color,
    code_color          = '  ' + pretty_errors.default_config.line_color,
    truncate_code       = True,
    display_locals      = True
)

words = ['debugging', 'with', 'stackprinter', 42]

def process_words(words_to_process):
    for i, word in enumerate(words_to_process):
        processed_word = str.capitalize(word)

process_words(words)