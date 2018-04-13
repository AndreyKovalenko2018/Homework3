#1
while True:
   try:
       s = input('Enter words:')
       print(s[2], s[-2], s[0:5], s[0:-2], s[::2], s[1::2], s[::-1], s[::-2],s[-2:0:-1], len(s), sep='\n')
   except IndexError as e:
       print('Try again! Error:',e)