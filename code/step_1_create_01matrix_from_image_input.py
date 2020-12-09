from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def transformPixel (x):
    #TransformPixelto01
    a, b, c = x
    if a < 150:
        return 1
    return 0

def savePixel (img):
    #SavePixelas01Array
    horizontal, vertical = img.size
    Y = np.zeros((vertical, horizontal ))
    for i in range(vertical):
        for j in range(horizontal):
            coordinate = j, i
            x = transformPixel(img.getpixel(coordinate))
            Y[i, j] = x
    return Y 
 
def determineCorner (Y):
    #DetermineIndexofCorners 
    Y_v = np.sum(Y, axis=1)
    Y_h = np.sum(Y, axis=0)
    v = Y_v.shape[0]
    h = Y_h.shape[0]
    for i in range (v):
        if Y_v[i] > 100:
            top = i
            break
    for i in range(v - 1, -1, -1):
        if Y_v[i] > 100:
            bottom = i
            break
    for i in range (h):
        if Y_h[i] > 100:
            left = i
            break
    for i in range(h - 1, -1, -1):
        if Y_h[i] > 100:
            right = i
            break
    return (top, bottom, left, right)
        
def reShape (Y):
    #NarrowSizeofMatrix
    top, bottom, left, right = determineCorner(Y)
    return Y[top : bottom, left : right]

def makeMatrixWithWidthPath (Z, x):
    #MakeTiniMatrixwithWidthofPath
    vertical = int(Z.shape[0] / x) + 1
    horizontal = int(Z.shape[1] / x) + 1
    a=int(x * 1/2)
    X=np.zeros((vertical, horizontal))
    for i in range(vertical):
        for j in range(horizontal):
            i_1 = int(x * (i + 1/2))
            j_1 = int(x * (j + 1/2))
            b = min(2, a)
            Z_1 = Z[i_1 - b : i_1 + b, j_1 - b : j_1 + b]
            sum = np.sum(Z_1)
            if sum > 1/2 * (2 * b + 1) * (2 * b + 1):
                X[i, j] = 1
            else: 
                X[i, j] = 0
    return X

def recoverFromTiniMatrix (Z, x):
    #RecoverMatrixfromTiniMatrix
    X = makeMatrixWithWidthPath(Z, x)
    vertical = Z.shape[0]
    horizontal = Z.shape[1]
    Z_new = np.zeros((vertical, horizontal))
    for i in range(vertical):
        for j in range(horizontal):
            i_1 = int((i + 1) / x)
            j_1 = int((j + 1) / x)
            if X[i_1, j_1] == 1:
                Z_new[i, j] = 1
            else: 
                Z_new[i, j] = 0
    return Z_new

def errorRecoverMatrix (Z, x):
    #CalculateChangeofNewMatrix
    Z_new = recoverFromTiniMatrix(Z, x)
    T = Z - Z_new
    vertical = T.shape[0]
    horizontal = T.shape[1]
    for i in range(vertical):
        for j in range(horizontal):
            if T[i, j] < 0:
                T[i, j] = (-1) * T[i,j]
    sumErr = np.sum(T) / (vertical * horizontal)
    return sumErr

def errorList (Z, array):
    #MakeaListOfErrorWithArangeOfWidth
    l = array.shape[0]
    X = np.zeros(l)
    for i in range(l):
        X[i] = errorRecoverMatrix(Z, array[i])
    return X

def determineWidthPath (Z, array):
    #DetermineWidthOfPath
    l = array.shape[0]
    d_min = 0
    min = errorRecoverMatrix(Z, array[0])
    for i in range(l):
        if errorRecoverMatrix(Z, array[i]) < min:
            min = errorRecoverMatrix(Z, array[i])
            d_min = array[i]
    return d_min

def lineGraphError (img, array):
    #DrawError
    Y = savePixel(img)
    Y_reshape = reShape(Y)
    s = errorList(Y_reshape, array)
    plt.plot(array, s, lw=2)
    plt.show()
    
def finalMatrix (path):
    #FinalFunction
    img = Image.open(path)
    Y = savePixel(img)
    Y_reshape = reShape(Y)
    d = determineWidthPath(Y_reshape, np.arange(12, 13, 0.05) )
    X = makeMatrixWithWidthPath(Y_reshape, d)
    return X


def drawDifferencesHorizontal (Z):
    #DrawDifferencesOfHorizontal
    horizontal_sum = Z.sum(axis = 1)
    fig, ax = plt.subplots()
    ax.plot(horizontal_sum)
    # plt.savefig('the_symmetry_test.png', dpi = 500, bbox_inches = 'tight', transparent = True, pad_inches = 0)
    # plt.show()
    
def drawDifferencesVertical (Z):
    #DrawDifferencesOfVertical
    vertical_sum = Z.sum(axis = 0)
    fig, ax = plt.subplots()
    ax.plot(vertical_sum)
    # plt.savefig('the_symmetry_test.png', dpi = 500, bbox_inches = 'tight', transparent = True, pad_inches = 0)
    # plt.show()


def determineIndexOfHorizontalChange (Z):
    #IndexOfHorizontalChanges
    points = []
    points.append(0)
    DIFFERENCE = 50
    horizontal_sum = Z.sum(axis = 1)
    n_rows = len(horizontal_sum)
    for i in range(0, n_rows - 1, 1):
        current_value = horizontal_sum[i]
        next_value = horizontal_sum[i + 1]
        if np.abs(current_value - next_value) > DIFFERENCE:
            points.append(i)
    points.append(len(horizontal_sum) - 1)
    rIndex = np.zeros(len(points))
    for i in range(len(points)):
        rIndex[i] = points[i]
    return rIndex

def determineIndexOfVerticalChange (Z):
    #IndexOfVerticalChanges
    points = []
    points.append(0)
    DIFFERENCE = 50
    vertical_sum = Z.sum(axis = 0)
    n_cols = len(vertical_sum)
    for i in range(0, n_cols - 1, 1):
        current_value = vertical_sum[i]
        next_value = vertical_sum[i + 1]
        if np.abs(current_value - next_value) > DIFFERENCE:
            points.append(i)
    points.append(len(vertical_sum) - 1)
    cIndex = np.zeros(len(points))
    for i in range(len(points)):
        cIndex[i] = points[i]
    return cIndex

def finalMatrix2 (path):
    #2ndVersionFinalMatrix
    img = Image.open(path)
    Y = savePixel(img)
    Z = reShape(Y)
    rIndex = determineIndexOfHorizontalChange(Z)
    cIndex = determineIndexOfVerticalChange(Z)
    n_cols = cIndex.shape[0]
    n_rows = rIndex.shape[0]
    finalMatrix = np.zeros((n_rows - 1, n_cols - 1))
    for i in range (0, n_rows - 1, 1):
        for j in range (0, n_cols - 1, 1):
            i_1 = int(rIndex[i]); i_2 = int(rIndex[i + 1])
            j_1 = int(cIndex[j]); j_2 = int(cIndex[j + 1])
            T = Z[i_1 : i_2, j_1 : j_2]
            sum = np.sum(T)
            if sum > 1/2 * (i_2 - i_1 + 1) * (j_2 - j_1 + 1):
                finalMatrix[i,j] = 1
            else: 
                finalMatrix[i,j] = 0
    return finalMatrix      
    
if __name__ == '__main__':
    path = r"C:\Users\dell\Files\images\input_image2.jpg"
    Z = finalMatrix2(path)
    T = finalMatrix(path)
