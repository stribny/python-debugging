"""
We can use modern Python f-strings to easily print variables to the output
console of the program

How to use:
- run the script with `python debug_with_console_f_strings.py`
- observe our state (i, processed_word) printed in the console
"""

# The output:
# i=0, processed_word=Debugging
# i=1, processed_word=With
# i=2, processed_word=Console
# i=3, processed_word=F-strings

words = ['debugging', 'with', 'console', 'f-strings']

def process_words(words_to_process):
    for i, word in enumerate(words_to_process):
        processed_word = str.capitalize(word)
        print(f"i={i}, processed_word={processed_word}")
        # In Python 3.8 we can use = specifier
        # print(f"{i=}, {processed_word=}")

process_words(words)