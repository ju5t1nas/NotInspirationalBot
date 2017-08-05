from PIL import Image, ImageDraw, ImageFont
from Inspirotron_Quotes_Engine import getAQuote, linecount
from Inspirotron_Formating_Quotes import findLongestLineAndNumberOfLines
from glob import glob
from random import randint
from os import getcwd


def getFinalImage():
    #We get information about our randomly chosen background
    imageInfo = pickRandomImageFromFile()
    print("Got Image Info Successfully!")
    #We get a randomly chosen Font
    fontInfo = pickRandomFontFromFile()
    print("Got Font Info Successfully!")
    # We open the selected random background
    image = Image.open(imageInfo[0])
    print("Opened Image Successfully!")
    #We get information about our random quote from out Quote Generator
    textInfo = getAQuote()
    print("Got Text Info Successfully!")
    #We separate the quote and other info
    text = textInfo[0]

    #We get the approximation of the longest line segment.
    longestLine = text[0:textInfo[1][0]]
    print("The number of lines is " + str(textInfo[1][1]))

    #We start searching for appropriate fontsize by starting at smallest font.
    fontSize = 1

    #We load the font.
    fontL = ImageFont.truetype(fontInfo[0], fontSize)
    #We set the fraction fo image's width we wish to be covered by the quote.
    img_fraction = imageInfo[2]

    #We iterate through increasing font sizes until we find one that is just under required image fraction.
    while fontL.getsize(longestLine)[0] < (img_fraction * image.size[0]):
        fontSize += 1
        fontL = ImageFont.truetype(fontInfo[0], fontSize)
    #Since the while loop will return a fontsize one point too large, we must subtract by one.
    fontSize -= 1
    fontL = ImageFont.truetype(fontInfo[0], fontSize)


    #print(font.getsize(longestLine)[0], img_fraction * image.size[0])

    #We obtain the best approximation for the quote size.
    trueSize = [fontL.getsize(longestLine)[0], fontSize * textInfo[1][1] * 1.6]
    draw = ImageDraw.Draw(image)

    textPosition = findTextPosition(imageInfo[1],fontSize,image.size, trueSize)
    print(textPosition)


    #Drawing thin border for the text by drawing it in black and shifting it by a pixel,
    #then drawing white text on top.
    draw.text((textPosition[0] - 1, textPosition[1]), text, font=fontL, fill=(0,0,0))
    draw.text((textPosition[0] + 1, textPosition[1]), text, font=fontL, fill=(0,0,0))
    draw.text((textPosition[0], textPosition[1] - 1), text, font=fontL, fill=(0,0,0))
    draw.text((textPosition[0], textPosition[1] + 1), text, font=fontL, fill=(0,0,0))
    draw.text(textPosition, text, font=fontL, fill=(255,255,255))

    image.save("out.jpeg")

    return text

def pickRandomImage(pathToFolder):
    print(glob(pathToFolder + "/*.jpeg"))
    ListOfImages = glob(pathToFolder + "/*.jpeg")
    ImageIndex = randint(0, len(ListOfImages)-1)
    return  ListOfImages[ImageIndex]

def pickRandomImageFromFile():
    photoFile = open("Photo_Info")
    line = photoFile.readlines()[randint(0, linecount("Photo_Info"))]
    filePath, position, fraction = line.split(";", 3)
    return [filePath, position, float(fraction)]

def pickRandomFontFromFile():
    fontFile = open("Font_Info")
    line = fontFile.readlines()[randint(0, linecount("Font_Info"))]
    fontPath = line.split(";", 1)
    return fontPath

def findTextPosition(positionStr, fontSize, imageSize, textSize):
    pos = (1,1)
    if positionStr == "TL":
        pos = (1, int(fontSize//3))
    if positionStr == "TC":
        pos = (int((imageSize[0] - textSize[0])//2), int(fontSize//3))
    if positionStr == "TR":
        pos = (int(imageSize[0] -textSize[0]), int(fontSize//3))
    if positionStr == "CL":
        pos = (1, int((imageSize[1] -textSize[1])//2))
    if positionStr == "CC":
        pos = (int((imageSize[0] - textSize[0])//2), int((imageSize[1] -textSize[1])//2))
    if positionStr == "CR":
        pos = (int(imageSize[0] - textSize[0]), int((imageSize[1] -textSize[1])//2))
    if positionStr == "BL":
        pos = (1, int(imageSize[1] -textSize[1]))
    if positionStr == "BC":
        pos = (int((imageSize[0] - textSize[0])//2), int(imageSize[1] -textSize[1]))
    if positionStr == "BR":
        pos = (int(imageSize[0] - textSize[0]), int(imageSize[1] - textSize[1]))
    return pos

getFinalImage()