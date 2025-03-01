x = compile('print(55)', 'test', 'eval')  #Compile text as code, and the execute it
exec(x)

y = compile('print(55)\nprint(88)', 'test', 'exec') #Compile more than one statement, and the execute it
exec(y)
