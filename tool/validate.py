import os
a = open('path-to-youy/train.txt','r')
b = open('path-to-your/val.txt','w')
k = 0
for i in a:
    if k%50==0:  #根据你想要的验证集比例进行选择
        b.write(i) 
        k = k + 1
    else:
        k = k + 1
a,b.close()