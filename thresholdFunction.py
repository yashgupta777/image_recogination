from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time as tm
from statistics import mean

def createExamples():
    numberArrayExamples = open('numArEx.txt','a')
    numbersWeHave = range(1,10)
    for eachNum in numbersWeHave:
        print (eachNum)
        for furtherNum in numbersWeHave:
            # you could also literally add it *.1 and have it create
            # an actual float, but, since in the end we are going
            # to use it as a string, this way will work.
            print(str(eachNum)+'.'+str(furtherNum))
            imgFilePath = 'images/numbers/'+str(eachNum)+'.'+str(furtherNum)+'.png'
            ei = Image.open(imgFilePath)
            eiar = np.array(ei)
            eiarl = str(eiar.tolist())

            print(eiarl)
            lineToWrite = str(eachNum)+'::'+eiarl+'\n'
            numberArrayExamples.write(lineToWrite)

def threshold_function(imageArray):
    balanceAr = []
    newAr = imageArray
    '''Above, we define the function, and we specify that we're expecting a parameter, the imageArray.
     This will be that array that we've been seeing with the pixel values. 
     Next, we define the balanceAr as an empty list, and the newAr, for now, is the imageArray.
     We cannot modify the actual iar without NumPy throwing a fit, so we do this. 
     Balance array, at the end, will be averaged, to find our threshold.'''
    for eachRow in imageArray:
        for eachPix in eachRow:
            print(eachPix[:3])
            avgNum = mean(eachPix[:3])
            print(avgNum)
            balanceAr.append(avgNum)
            #print(eachPix)
            #tm.sleep(5)
            #avgNum = mean(eachPix[:3])
            #balanceAr.append(avgNum)
    balance = mean(balanceAr)
    print(balance)
    '''What we've added for now is, from the average of the balance array, we then assess each pixel. 
    If the pixel is brighter than the average, then it is a white. If it is darker than the average, then it is black.'''
    for eachRow in newAr:
        for eachPix in eachRow:
            if mean(eachPix[:3]) > balance:
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
                eachPix[3] = 255
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
                eachPix[3] = 255
    '''Now, what we can do with this function is feed in the image array, and we're going to be returned the thresholded image array.'''
    return newAr

createExamples()
'''
i = Image.open('images/numbers/0.1.png')
iar = np.array(i)
i2 = Image.open('images/numbers/y0.4.png')
iar2 = np.array(i2)

i3 = Image.open('images/numbers/y0.5.png')
iar3 = np.array(i3)
print(iar3)
i4 = Image.open('images/sentdex.png')
iar4 = np.array(i4)
threshold_function(iar)
threshold_function(iar2)
threshold_function(iar3)
threshold_function(iar4)


fig = plt.figure()
ax1 = plt.subplot2grid((8, 6), (0, 0), rowspan=4, colspan=3)
ax2 = plt.subplot2grid((8, 6), (4, 0), rowspan=4, colspan=3)
ax3 = plt.subplot2grid((8, 6), (0, 3), rowspan=4, colspan=3)
ax4 = plt.subplot2grid((8, 6), (4, 3), rowspan=4, colspan=3)

ax1.imshow(iar)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)

plt.show()
'''

