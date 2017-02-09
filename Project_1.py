from PIL import Image  #This imports the functionality of this python console to allow us to use images and manipulate them; called pilow. 

def medianOdd(myList):                  #This creates the function medianOdd which takes the input of "mylist"
    listLength = len(myList)            #MedianOdd is a function specific to lists with an odd number of elements. This line of codes says " create list length and set it equal to the length of "my list" by using the built in len function.
    sortedValues = sorted(myList)       #sortedvalues is set equal to the the list but in sorted form from least to greatest using the sorted function.
    middleIndex = (listLength + 1)//2 - 1   #this finds our median value. You have to add one because python starts counting at 0, then re subtract it for the correct number.
    return sortedValues[middleIndex]    #this returns the middle index or the median of the sortedValues.
    
imgList = []     #This creates the list imgList with nothing in it.

for i in range(9):          #this is a loop, from 0 - 9.
    imgList.append(Image.open("Project1Images/" + str(i + 1) + ".png"))     #This loops through all of the pictures. 
    
    
picW, picH = imgList[0].size            #this creates the variables picW and picH and they equal the size of imglist.

redPixelList = []                   #creates redPixelList with nothing in it.
greenPixelList = []                 #creates greenPixelList with nothing in it.
bluePixelList = []                  #creates bluePixelList with nothing in it.

myRed, myGreen, myBlue = imgList[6].getpixel((2,3))         #.getpixel is a part of pillow, myRed, myGreen, myBlue all equal the 5th element of imgList which is a pixel, so three numbers.

print(myRed, myGreen, myBlue)                               #prints the pixel numbers. 

canvas = Image.new("RGB", (picW, picH), "white")            #creates a new image. for us to put the new median pixels into.

for x in range(picW):                                       #loop for as long as picW
    for y in range(picH):                                   #this is a nested for loop therefore it is indented.
        for myImage in imgList:                             
            myRed, myGreen, myBlue = myImage.getpixel((x,y))            #myRed, myGreen, myBlue all equal the median pixel.
            redPixelList.append(myRed)                          #these lines add to the respective lists.
            greenPixelList.append(myGreen)
            bluePixelList.append(myBlue)
            
        medianRed = medianOdd(redPixelList)                 #adds median values
        medianGreen = medianOdd(greenPixelList)
        medianBlue = medianOdd(bluePixelList)
        
        canvas.putpixel((x,y), (medianRed, medianGreen, medianBlue))            #puts them onto the new picture.
        
        redPixelList = []                                                       #clears the lists so that a new set of median values can be added to the new picture.
        greenPixelList = []             
        bluePixelList = []
        

canvas.save("newpic.png")                                       #saves the new picture with the median values as newpic.png