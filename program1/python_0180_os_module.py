import os



'''
1) Go to the amplifier at the left bottom corner of your computer
2) Press and type 'cmd', press enter, your computer terminal will be brought up.

Then you can try some windows command in the terminal.

Example 1) Show me the date
Command: date /t
'''

# os.system("date /t")


'''
Example 2) Open the notepad
Command: notepad
'''

# os.system("notepad")


'''
Example 3) Open the chrome browser, take me to the youtube music channel
Command: 
'''

# os.system('start chrome "https://www.youtube.com/feed/music"')

print(os.name) # nt, which means: my computer is on Windows NT platform

print(os.getcwd()) # cwd means: current working directory.