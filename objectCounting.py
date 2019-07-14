"""
Name Surname: Ezgi Subasi
Number: 041701022
Date: 05.03.2019
Code: This code provides counting object's number
with using Levialdi and TSF Algorithms.

"""

import tkinter as tk
from tkinter.filedialog import *
import PIL
from PIL import Image, ImageTk
import numpy as np
import csv
import random as random

#Global Variables
ONE=None
openedImage=None
binaryImage=None
framedImage=None
iteration2=None
nCol, nRow, orNRow, orNCol = 0, 0, 0, 0
pixelMapAsString = ""

#GUI Creation
root = tk.Tk()
xSize, ySize = 900, 600
size = str(xSize)+"x"+str(ySize)
root.geometry(size)
root.title("Programing Studio")
root.configure(bg='white')

#Create Drop Down Menu
menu = Menu(root)
root.config(menu=menu)

#Main 3x3 GUI Grid Partioning
for r in range(3):
    for c in range(3):
        if r == 0:
            Label(root, bg='white').grid(row=r, column=c, padx=20, pady=20)
        elif r == 1:
            Label(root, bg='white').grid(row=r, column=c, padx=180, pady=20)
        else:
            Label(root, bg='white').grid(row=r, column=c, padx=180, pady=20)

#Opening an image
def openImage():
    try:
        openFileFormats = (("all files", "*.*"), ("png files", "*.png"))  # File formats for easy search
        path = askopenfilename(parent=root, filetypes=openFileFormats)  # Basic file pick gui
        fp = open(path, "rb")  # Read file as a byte map
        global openedImage
        openedImage = Image.open(fp).convert('1', dither=Image.NONE)  # Convert byte map to Image then grayscaling of the image
    except:
        reset()
    imageProcess()

#Prints image's information and changes colored images to the black-white form.
def imageProcess():
    global openedImage
    nCol, nRow = openedImage.size
    print("-------------------------------------------")
    print("Image size : \nHorizontal : ", nCol, "\nVertical : ", nRow)
    print("-------------------------------------------")

    colorMap = openedImage.load() # Images to pixel map because of converting return average of RGB

    global framedImage
    # Creates an image with 2 additional columns and rows for framing edges
    framedImage = Image.new('RGB', ((nCol+2), (nRow+2)), color='black').convert('1', dither=Image.NONE)
    #convert 1 : black white image
    #convert L : gray scaled image

    for r in range(1, nRow+1):
        for c in range(1, nCol+1):
            framedImage.putpixel((c, r), colorMap[c-1, r-1]) #Coloring framed image

    colorMap = framedImage.load() # Images to pixel map
    orNCol, orNRow = nCol, nRow

    nCol, nRow = framedImage.size
    print("-------------------------------------------")
    print("Framed Image size : \nHorizontal : ", nCol, "\nVertical : ", nRow)
    print("-------------------------------------------")


    print("-------------------------------------------")
    print("Framed Image size : \nHorizontal : ", nCol, "\nVertical : ", nRow)
    print("-------------------------------------------")

    #creates binary 2d array with zeros
    global binaryImage
    binaryImage = [[0 for x in range(nCol)] for y in range(nRow)]

    global img1
    global pixelMapAsString
    #Create binary image according to pixel map
    for r in range(nRow):
        for c in range(nCol):
            if colorMap[c,r] > 200:
                binaryImage[r][c] = 1
            else:
                binaryImage[r][c] = 0
            pixelMapAsString += str(binaryImage[r][c])
        pixelMapAsString += "\n"

    defImg = ImageTk.PhotoImage(framedImage)
    img1.config(image=defImg)
    img1.image = defImg
    img1.update()
    print(pixelMapAsString)

#Creates images with random objects.
def createImg():
    global binaryImage, binaryCanvas4, pixelMapAsString
    ONE = 150  # 1-valued pixel intensity
    bim = binary_image(100, 100, ONE)
    new_img = np2PIL(bim)
    arr = PIL2np(new_img)
    binaryImage = arr

    nrow, ncol = new_img.size
    #Change pixel image into the strings.
    for r in range(nrow):
        for c in range(ncol):
            if arr[r, c] > 149:
                binaryImage[r][c] = 1
            else:
                binaryImage[r][c] = 0
            pixelMapAsString += str(binaryImage[r][c])
        pixelMapAsString += "\n"

    #Upload image in the GUI.
    defImg = ImageTk.PhotoImage(new_img)
    img1.config(image=defImg)
    img1.image = defImg
    img1.update()

#Creates random objects.
def binary_image(nrow,ncol,Value):
    x, y = np.indices((nrow, ncol))
    mask_lines = np.zeros(shape=(nrow,ncol))

    a = random.randint(1, nrow)
    b = random.randint(1, ncol)
    c = random.randint(1, 100)
    d = random.randint(1, 9)
    e = random.randint(1, 9)

    x0, y0, r0 = a, b, 103
    x1, y1, r1 = a, b, 10
    x2, y2, r2 = 30, c, 10
    x3, y3, r3 = c, 30, 10
    x4, y4, r4 = 70, a, 10

    for i in range(50, 70):
        mask_lines[e][i] = 1
        mask_lines[a][i + d] = 1
        mask_lines[b][i + d] = 1
        mask_lines[d][i + e] = 1
        mask_lines[c][i + e] = 1

    mask_square1 = np.fmax(np.absolute(x - x1), np.absolute(y - y1)) <= r1
    mask_square2 = np.fmax(np.absolute(x - x2), np.absolute(y - y2)) <= r2
    mask_square3 = np.fmax(np.absolute(x - x3), np.absolute(y - y3)) <= r3
    mask_square4 = np.fmax(np.absolute(x - x4), np.absolute(y - y4)) <= r4
    imge = np.logical_or(
        np.logical_or(np.logical_or(np.logical_or(mask_lines, mask_square2), mask_square1), mask_square3),
        mask_square4) * Value

    return imge

#Convert image into the numpy array.
def PIL2np(img):
    nrows = img.size[0]
    ncols = img.size[1]
    print("nrows, ncols : ", nrows, ncols)
    imgarray = np.array(img.convert("L"))
    return imgarray

#Convert numpy array into the image.
def np2PIL(im):
    print("size of arr: ", im.shape)
    img = Image.fromarray(np.uint8(im))
    return img

def reset():
    print("")

#Writes the binary form of the image's into the canvas.
def writeBinaryToScreen():
    global binaryCanvas5
    global pixelMapAsString
    fontSize = 3
    binaryCanvas5.select_clear()
    binaryCanvas5.delete("lvTag")
    binaryCanvas5.create_text(200, 0, text=pixelMapAsString, font=("Ariel", fontSize, "bold"), tag="lvTag",anchor=N)
    binaryCanvas5.update()

#Writes the levialdi's iteration on the binary form into the canvas.
def binaryLEV(arrayLEV, nrow, ncol):
    global binaryCanvas
    strArray1 = ""
    for r in range(nrow):
        for c in range(ncol):
            strArray1 += str(arrayLEV[r][c])
            print(arrayLEV[r][c], end="")
        print("")
        strArray1 += "\n"
    binaryCanvas.select_clear()
    binaryCanvas.delete("levialditext")
    binaryCanvas.create_text(200, 0, text=strArray1, font=("Ariel", 2), tag="levialditext", anchor=N)
    binaryCanvas.update()

#Writes the tsf's iteration on the binary form into the canvas.
def binaryTSF(arrayTSF, nrow, ncol):
    global binaryCanvas3
    strArray2 = ""
    for r in range(nrow):
        for c in range(ncol):
            strArray2 += str(arrayTSF[r][c])
            print(arrayTSF[r][c], end="")
        print("")
        strArray2 += "\n"
    binaryCanvas3.select_clear()
    binaryCanvas3.delete("tsftext")
    binaryCanvas3.create_text(200, 1, text=strArray2, font=("Ariel", 2), tag="tsftext", anchor=N)
    binaryCanvas3.update()

def levialdi():
    global binaryImage
    global binaryCanvas
    global iterationLEV
    global nccLEV

    originalArrayLEV = binaryImage
    nrow = len(originalArrayLEV)
    ncol = len(originalArrayLEV[1])

    w, h = nrow + 2, ncol + 2
    copiedArrayLEV = [[0 for x in range(w)] for y in range(h)]

    for i in range(0, nrow):
        for j in range(0, ncol):
            copiedArrayLEV[i][j] = 0

    for i in range(0, nrow):
        for j in range(0, ncol):
            copiedArrayLEV[i][j] = originalArrayLEV[i][j]

    iterationLEV = 0
    nccLEV = 0
    flag = True
    while flag:
        flag = False
        binaryLEV(copiedArrayLEV, nrow, ncol)
        for i in range(1, nrow - 1):
            for j in range(1, ncol - 1):
                copiedArrayLEV[i][j] = originalArrayLEV[i][j]
                if originalArrayLEV[i - 1][j - 1] == 0 and originalArrayLEV[i - 1][j] == 0 and \
                        originalArrayLEV[i - 1][j + 1] == 0 and originalArrayLEV[i][j - 1] == 0 \
                        and originalArrayLEV[i][j] == 1 and originalArrayLEV[i][j + 1] == 0 and \
                        originalArrayLEV[i + 1][j - 1] == 0 and originalArrayLEV[i + 1][j] == 0\
                        and originalArrayLEV[i + 1][j + 1] == 0:
                    nccLEV = nccLEV + 1
                    LEVprintNCC(nccLEV)
                    flag = True
                # augmented condition
                if originalArrayLEV[i][j - 1] == 1 and originalArrayLEV[i + 1][j] == 1\
                        and originalArrayLEV[i][j] == 0:
                    copiedArrayLEV[i][j] = 1
                    flag = True
                # delete condition
                elif originalArrayLEV[i + 1][j - 1] == 0 and originalArrayLEV[i][j] == 1 and \
                        originalArrayLEV[i + 1][j] == 0 and originalArrayLEV[i][j - 1] == 0:
                    copiedArrayLEV[i][j] = 0
                    flag = True
        if flag:
            for a in range(0, nrow):
                for b in range(0, ncol):
                    originalArrayLEV[a][b] = copiedArrayLEV[a][b]
            iterationLEV += 1
            LEVprintIteration(iterationLEV)

def tsf():
    global binaryImage
    global binaryCanvas3
    global nccTSF
    global iterationTSF

    originalArrayTSF = binaryImage

    nrow = len(originalArrayTSF)
    ncol = len(originalArrayTSF[1])

    w, h = nrow+2, ncol+2
    copiedArrayTSF = [[0 for x in range(w)] for y in range(h)]

    for i in range(0, nrow):
        for j in range(0, ncol):
            copiedArrayTSF[i][j] = 0

    for i in range(0, nrow):
        for j in range(0, ncol):
            copiedArrayTSF[i][j] = originalArrayTSF[i][j]

    nccTSF = 0
    iterationTSF = 0
    flag = True
    while flag:
        binaryTSF(copiedArrayTSF, nrow, ncol)
        flag = False
        for a in range(1, nrow - 1, 2):
            for b in range(1, ncol - 1, 2):
                copiedArrayTSF[a][b] = originalArrayTSF[a][b]
                valueOfCp = countingCp(a, b, originalArrayTSF)
                if originalArrayTSF[a][b] == 0:
                    if valueOfCp == 1 and ((originalArrayTSF[a][b - 1] == 1 and originalArrayTSF[a - 1][b] == 1) or (
                            originalArrayTSF[a][b - 1] == 1 and originalArrayTSF[a+1][b] == 1)):
                        copiedArrayTSF[a][b] = 1
                        flag = True
                else:
                    valueOfBp = countingBp(a, b, originalArrayTSF)
                    checkZero = calculateZeros(a, b, originalArrayTSF)
                    if valueOfBp == 0:
                        nccTSF += 1
                        TSFprintNCC(nccTSF)
                        copiedArrayTSF[a][b] = 0
                        flag = True
                    if valueOfBp == 1:
                        if (originalArrayTSF[a - 1][b - 1] == 0 and originalArrayTSF[a + 1][b - 1] == 0) \
                                and valueOfCp == 1 and checkZero > 0:
                            copiedArrayTSF[a][b] = 0
                            flag = True
                    else:
                        if valueOfCp == 1 and checkZero > 0:
                            copiedArrayTSF[a][b] = 0
                            flag = True

        for a in range(2, nrow - 1, 2):
            for b in range(2, ncol - 1, 2):
                copiedArrayTSF[a][b] = originalArrayTSF[a][b]
                valueOfCp = countingCp(a, b, originalArrayTSF)
                if originalArrayTSF[a][b] == 0:
                    if valueOfCp == 1 and ((originalArrayTSF[a][b - 1] == 1 and originalArrayTSF[a - 1][b] == 1) or (
                            originalArrayTSF[a][b - 1] == 1 and originalArrayTSF[a+1][b] == 1)):
                        copiedArrayTSF[a][b] = 1
                        flag = True
                else:
                    valueOfBp = countingBp(a, b, originalArrayTSF)
                    checkZero = calculateZeros(a, b, originalArrayTSF)
                    if valueOfBp == 0:
                        nccTSF += 1
                        TSFprintNCC(nccTSF)
                        copiedArrayTSF[a][b] = 0
                        flag = True
                    if valueOfBp == 1:
                        if (originalArrayTSF[a - 1][b - 1] == 0 and originalArrayTSF[a + 1][b - 1] == 0) \
                                and valueOfCp == 1 and checkZero > 0:
                            copiedArrayTSF[a][b] = 0
                            flag = True
                    else:
                        if valueOfCp == 1 and checkZero > 0:
                            copiedArrayTSF[a][b] = 0
                            flag = True
        if flag:
            for i in range(0, nrow):
                for j in range(0, ncol):
                    originalArrayTSF[i][j] = copiedArrayTSF[i][j]

        for a in range(2, nrow - 1, 2):
            for b in range(1, ncol - 1, 2):
                copiedArrayTSF[a][b] = originalArrayTSF[a][b]
                valueOfCp = countingCp(a, b, originalArrayTSF)
                if originalArrayTSF[a][b] == 0:
                    if valueOfCp == 1 and ((originalArrayTSF[a][b - 1] == 1 and originalArrayTSF[a - 1][b] == 1) or (
                            originalArrayTSF[a][b - 1] == 1 and originalArrayTSF[a+1][b] == 1)):
                        copiedArrayTSF[a][b] = 1
                        flag = True
                else:
                    valueOfBp = countingBp(a, b, originalArrayTSF)
                    checkZero = calculateZeros(a, b, originalArrayTSF)
                    if valueOfBp == 0:
                        nccTSF += 1
                        TSFprintNCC(nccTSF)
                        copiedArrayTSF[a][b] = 0
                        flag = True
                    if valueOfBp == 1:
                        if (originalArrayTSF[a - 1][b - 1] == 0 and originalArrayTSF[a + 1][b - 1] == 0) \
                                and valueOfCp == 1 and checkZero > 0:
                            copiedArrayTSF[a][b] = 0
                            flag = True
                    else:
                        if valueOfCp == 1 and checkZero > 0:
                            copiedArrayTSF[a][b] = 0
                            flag = True
        for a in range(1, nrow - 1, 2):
            for b in range(2, ncol - 1, 2):
                copiedArrayTSF[a][b] = originalArrayTSF[a][b]
                valueOfCp = countingCp(a, b, originalArrayTSF)
                if originalArrayTSF[a][b] == 0:
                    if valueOfCp == 1 and ((originalArrayTSF[a][b - 1] == 1 and originalArrayTSF[a - 1][b] == 1) or (
                            originalArrayTSF[a][b - 1] == 1 and originalArrayTSF[a+1][b] == 1)):
                        copiedArrayTSF[a][b] = 1
                        flag = True
                else:
                    valueOfBp = countingBp(a, b, originalArrayTSF)
                    checkZero = calculateZeros(a, b, originalArrayTSF)
                    if valueOfBp == 0:
                        nccTSF += 1
                        TSFprintNCC(nccTSF)
                        copiedArrayTSF[a][b] = 0
                        flag = True
                    if valueOfBp == 1:
                        if (originalArrayTSF[a - 1][b - 1] == 0 and originalArrayTSF[a + 1][b - 1] == 0) \
                                and valueOfCp == 1 and checkZero > 0:
                            copiedArrayTSF[a][b] = 0
                            flag = True
                    else:
                        if valueOfCp == 1 and checkZero > 0:
                            copiedArrayTSF[a][b] = 0
                            flag = True
        if flag:
            for i in range(0, nrow):
                for j in range(0, ncol):
                    originalArrayTSF[i][j] = copiedArrayTSF[i][j]
            iterationTSF += 1
            TSFprintIteration(iterationTSF)


def TSFprintNCC(ncctsf):
    binaryCanvas4.select_clear()
    binaryCanvas4.delete("tsfncc")
    binaryCanvas4.create_text(200, 40, text="TSF ", font=("Ariel", 20), tag="tsfncc")
    binaryCanvas4.create_text(200, 80, text="NCC: ", font=("Ariel", 20), tag="tsfncc")
    binaryCanvas4.create_text(200, 120, text=ncctsf, font=("Ariel", 20), tag="tsfncc")
    binaryCanvas4.update()

def LEVprintNCC(ncclev):
    binaryCanvas2.select_clear()
    binaryCanvas2.delete("levialdincc")
    binaryCanvas2.create_text(200, 40, text="LEV ", font=("Ariel", 20), tag="levialdincc")
    binaryCanvas2.create_text(200, 80, text="NCC: ", font=("Ariel", 20), tag="levialdincc")
    binaryCanvas2.create_text(200, 120, text=ncclev, font=("Ariel", 20), tag="levialdincc")
    binaryCanvas2.update()

def TSFprintIteration(it):
    binaryCanvas4.select_clear()
    binaryCanvas4.delete("tsfiteration")
    binaryCanvas4.create_text(200, 160, text="Iteration: ", font=("Ariel", 20), tag="tsfiteration")
    binaryCanvas4.create_text(200, 200, text=it, font=("Ariel", 20), tag="tsfiteration")
    binaryCanvas4.update()

def LEVprintIteration(it):
    binaryCanvas2.select_clear()
    binaryCanvas2.delete("levialdiiteration")
    binaryCanvas2.create_text(200, 160, text="Iteration: ", font=("Ariel", 20), tag="levialdiiteration")
    binaryCanvas2.create_text(200, 200, text=it, font=("Ariel", 20), tag="levialdiiteration")
    binaryCanvas2.update()

def countingBp(i, j, binaryArray1):
    neighborsArray = [binaryArray1[i][j], binaryArray1[i - 1][j - 1],
                      binaryArray1[i - 1][j], binaryArray1[i - 1][j + 1],
                      binaryArray1[i][j + 1], binaryArray1[i + 1][j + 1],
                      binaryArray1[i + 1][j], binaryArray1[i + 1][j - 1], binaryArray1[i][j - 1]]
    countBp = 0
    for x in range(1, 9):
        if neighborsArray[x] == 1:
            countBp += 1
    return countBp

def countingCp(i, j, binaryArray2):
    neigborsArray2 = [binaryArray2[i][j], binaryArray2[i - 1][j - 1], binaryArray2[i - 1][j],
                      binaryArray2[i - 1][j + 1], binaryArray2[i][j + 1], binaryArray2[i + 1][j + 1],
                      binaryArray2[i + 1][j], binaryArray2[i + 1][j - 1], binaryArray2[i][j - 1]]
    for t in range(3, 9):
        if (t % 2 != 0) and (neigborsArray2[t - 1] == neigborsArray2[t + 1] == 1):
            neigborsArray2[t] = 1
    if neigborsArray2[2] == 1 and neigborsArray2[8] == 1:
        neigborsArray2[1] = 1

    newBp = 0
    for x in range(1, 9):
        if neigborsArray2[x] == 1:
            newBp += 1

    countTp = 0
    for q in range(1, 8):
        if neigborsArray2[q] == 0 and neigborsArray2[q + 1] == 1:
            countTp += 1
    if neigborsArray2[8] == 0 and neigborsArray2[1] == 1:
        countTp += 1
    if newBp == 8:
        return 1
    else:
        return countTp

def calculateZeros(i, j, binaryArray3):
    neigborsArray3 = [binaryArray3[i - 1][j - 1], binaryArray3[i - 1][j], binaryArray3[i - 1][j + 1],
                      binaryArray3[i][j + 1], binaryArray3[i + 1][j + 1], binaryArray3[i + 1][j],
                      binaryArray3[i + 1][j - 1], binaryArray3[i][j - 1]]
    countingZero = 0
    for t in range(0, 6):
        if neigborsArray3[t] == 0 and neigborsArray3[t+1] == 0 and neigborsArray3[t+2] == 0:
            countingZero += 1
    if neigborsArray3[7] == 0 and neigborsArray3[0] == 0 and neigborsArray3[1] == 0:
        countingZero += 1
    elif neigborsArray3[6] == 0 and neigborsArray3[7] == 0 and neigborsArray3[0] == 0:
        countingZero += 1
    return countingZero

def fileImage():
    return openImage(), writeBinaryToScreen()

def createImage():
    return createImg(), writeBinaryToScreen()

def save():
    global nccForLEV, nccForTSF
    f = open('outputs.csv', 'w')
    f.write('Levialdi: NCC: {}, Iterations: {}'.format(nccLEV, iterationLEV))
    f.write("\n")
    f.write('TSF: NCC: {}, Iterations{}: '.format(nccTSF, iterationTSF))
    f.close()


subMenu = Menu(menu)
menu.add_cascade(label="Input Image", menu=subMenu)
subMenu.add_command(label="File Image", command=fileImage)
subMenu.add_command(label="Create Image", command=createImage)

Levialdi = Button(root, text='Levialdi', borderwidth=1, command=levialdi, relief=RAISED)
Levialdi.grid(row=0, column=1, sticky=NW, padx=150, pady=20)

TSF = Button(root, text='TSF', borderwidth=1, command=tsf, relief=RAISED)
TSF.grid(row=0, column=1, sticky=NW, padx=200, pady=20)

Save = Button(root, text='Save', borderwidth=1, command=save, relief=RAISED)
Save.grid(row=0, column=2, sticky=NW, padx=200, pady=20)

binaryCanvas = Canvas(root, borderwidth=2, bg="white", bd=3, relief="groove")
binaryCanvas.grid(row=1, column=1, sticky=W + E + N + S)

binaryCanvas2 = Canvas(root, borderwidth=2, bg="white", bd=3, relief="groove")
binaryCanvas2.grid(row=1, column=2, sticky=W + E + N + S)

binaryCanvas3 = Canvas(root, borderwidth=2, bg="white", bd=3, relief="groove")
binaryCanvas3.grid(row=2, column=1, sticky=W + E + N + S)

binaryCanvas4 = Canvas(root, borderwidth=2, bg="white", bd=3, relief="groove")
binaryCanvas4.grid(row=2, column=2, sticky=W + E + N + S)

binaryCanvas5 = Canvas(root, borderwidth=2, bg="white", bd=3, relief="groove")
binaryCanvas5.grid(row=2, column=0, sticky=W + E + N + S)

img1 = Label(root, borderwidth=2, bg="white", fg="black", bd=3, relief="groove")
img1.grid(row=1, column=0, sticky=W + E + N + S)

root.mainloop()
