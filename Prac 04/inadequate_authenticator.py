__author__ = 'Micheal Brady-Mahoney'


users_username = input('Please enter your username: ')
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45''BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

if users_username in usernames:
    print('Access Granted :)')
else:
    print('Access Denied :(')
