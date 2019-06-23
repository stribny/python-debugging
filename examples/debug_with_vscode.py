"""
We can use the built-in debugger in Visual Studio Code editor to interactively
step-through the program's execution and examine the variables

How to use:
- install VSCode (https://code.visualstudio.com/)
- install Python extension (https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- open debug_with_vscode.py in VSCode
- make sure Python's execution path is set to the virtual environment that we created with pipenv
  (see python.pythonPath in .vscode/settings.json for that)
- switch to Debug panel and add a new debug configuration (choose current file), this will create
  .vscode/launch.json configuration
- set breakpoints by clicking on the left side of the line number where you want to stop the execution
- click run on the Debug panel
- the program will start and stop at the line you have selected
- you will see all variables displayed in the debug panel and a new floating control panel to control the execution
"""

words = ['debugging', 'with', 'vscode']

def process_words(words_to_process):
    for i, word in enumerate(words_to_process):
        processed_word = str.capitalize(word) # set breakpoint here

process_words(words)