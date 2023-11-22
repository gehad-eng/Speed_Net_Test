# this app is using python to test the internet speed 

import speedtest  
from pystyle import *
print(Box.Lines('[+] this app for speed net [+]'))
Write.Print('please wait the app is runing ...', Colors.red, interval=0.1)
print('\n')


st = speedtest.Speedtest()

# download 

dst = st.download()
d = round(dst / (10**6), 2)

#upload 
ust = st.upload()
u = round(ust/ (10**6),2)

Write.Print('the net speed is:\n', Colors.green , interval=0.1)

print('your Download speed is :', d , 'MB')
print('Your Upload speed is : ', u , 'MB')

input('\n press any key to exit')

