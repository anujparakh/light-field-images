import numpy as np
import cv2

# Constants
imageNames = ["LF_01.png", "LF_02.png"]

def readImage(imagePath):
    image = cv2.imread(imagePath, cv2.IMREAD_COLOR)
    return image

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

if __name__ == '__main__':
    # Setting up the input output paths
    inputDir = '../Images/'
    outputDir = '../Results/'

    # Find views for each image
    for imageName in imageNames:
        # Do everything for each image
        image = readImage(inputDir + imageName)
        image = getView(image, 1, 1)
        print(image)
        print("-------------------------")
        print(np.roll(image, 1, axis=2))
        print("*************************")

        