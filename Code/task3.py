import numpy as np
import cv2

# Constants
imageNames = ["LF_01.png", "LF_02.png"]

def readImage(imagePath):
    image = cv2.imread(imagePath, cv2.IMREAD_COLOR)
    return image

# circshift implementation similar to matlab
def circ_shift(toShift, shift):
    shifted = np.roll(toShift, shift[0], axis = 0)
    shifted = np.roll(shifted, shift[1], axis = 1)
    return shifted

def getView(image, u, v):
    nrows, ncols = image.shape [:-1]
    # Size of the output
    spatialRows = int(nrows / 7)
    spatialCols = int(ncols / 7)
    imageToReturn = np.zeros([spatialRows, spatialCols, 3])
    
    for i in range(0, spatialRows):
            for j in range(0, spatialCols):
                imageToReturn[i][j] = image[i * 7 + u - 1][j * 7 + v - 1]
    return imageToReturn

def refocusImage(image, allImageViews, d):
    nrows, ncols = image.shape [:-1]
    # Size of the output
    spatialRows = int(nrows / 7)
    spatialCols = int(ncols / 7)
    imageAddedUp = np.zeros([spatialRows, spatialCols, 3])

    # Add all the shifted images
    for u in range(-3, 4):
        for v in range(-3, 4):
            # Calculate shifts
            du = u * d
            dv = v * d
            shiftedImage = circ_shift(allImageViews[u + 3][v + 3], [du, dv])
            imageAddedUp = np.add(imageAddedUp, shiftedImage)
            print("du = " + str(du) + ", dv = " + str(dv))
            print("Added " + str(u) + ", " + str(v))
            print("-----------------------------------")

    # Average the added images
    imageAddedUp = (imageAddedUp / 49)
    return imageAddedUp.astype(int)

if __name__ == '__main__':
    # Setting up the input output paths
    inputDir = '../Images/'
    outputDir = '../Results/'

    # Find views for each image
    for imageName in imageNames:
        # Do everything for each image
        image = readImage(inputDir + imageName)
        
        # Get all the image views
        allImageViews = []
        for i in range(1, 8):
            imageViewRow = []
            for j in range(1, 8):
                imageViewRow.append(getView(image, i, j))
            allImageViews.append(imageViewRow)
        
        # Refocus at different depths
        for d in range(-2, 3):
            imageRefocused = refocusImage(image, allImageViews, d)
            cv2.imwrite(outputDir + imageName[:-4] + "_refocused_d" + str(d) + ".jpg", imageRefocused)
        print("Refocused Image " + imageName)


