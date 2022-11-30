import random
import os
from playsound import playsound
import time
import keyboard

filenames=os.listdir('tek hece/fonem tanıma-e/')
categories=[[],[],[],[],[]]
i=0
while i<5:
    for filename in filenames:
        if i == 5:
            break
        if len(categories[i]) == 20:
            i+=1
        else:
            categories[i].append(filename.split(".")[0])

z=0
while z<5:
    for i in range(20):
        j=random.randint(0,len(categories[z])-1)
        playsound('tek hece/fonem tanıma-e/'+categories[z][j]+'.wav')
        tic = time.perf_counter()
        keyboard.wait('q')
        toc = time.perf_counter()
        print(categories[z][j].split("-")[0]," Tepki Süresi: ",toc-tic)
        categories[z].remove(categories[z][j])
        if(len(categories[z])==0):
            print(z+1,". tur bitti")
            z+=1
        if z == 5:
            break