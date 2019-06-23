"""
We can stop execution of the Python program with `breakpoint()` function which
will stop execution of the program in the given place and switches to Python debugger

This is useful to open a debugger right at the place where we need to examine
the state of the program

How to use:
- run the script with `python debug_with_breakpoint.py`
- the program will stop in the first `for` iteration, on the breakpoint() line
- we will get into pdb (Python debugger)
- while now in pdb:
    - we can see what `i` variable is by typing `i`
    - we can examine `processed_word` variable by typing `processed_word`
    - we can use any other pdb functionality
    - we can continue the execution of the program by typing `continue` and repeat the examination ^
"""

# Example of the interactive session:
# > python-debugging/debug_with_breakpoint.py(22)process_words()
# -> for i, word in enumerate(words_to_process):
# (Pdb) i
# 0
# (Pdb) processed_word
# 'Debugging'
# (Pdb) continue
# > python-debugging/debug_with_breakpoint.py(22)process_words()
# -> for i, word in enumerate(words_to_process):
# (Pdb) i
# 1
# (Pdb) processed_word
# 'With'

words = ['debugging', 'with', 'breakpoint()']

def process_words(words_to_process):
    for i, word in enumerate(words_to_process):
        processed_word = str.capitalize(word)
        breakpoint()

process_words(words)