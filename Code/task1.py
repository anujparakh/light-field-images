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
        # Get the size of the image
        nrows, ncols = image.shape [:-1]
        # Size of the output
        spatialRows = int(nrows / 7)
        spatialCols = int(ncols / 7)
        # Create all 4 output images
        imageTopLeft = getView(image, 1, 1)
        imageTopRight = getView(image, 1, 7)
        imageBottomLeft = getView(image, 7, 1)
        imageBottomRight = getView(image, 7, 7)

        # Write the outputs
        cv2.imwrite(outputDir + imageName[:-4] + "_view11" + ".jpg", imageTopLeft)
        cv2.imwrite(outputDir + imageName[:-4] + "_view12" + ".jpg", imageTopRight)
        cv2.imwrite(outputDir + imageName[:-4] + "_view21" + ".jpg", imageBottomLeft)
        cv2.imwrite(outputDir + imageName[:-4] + "_view22" + ".jpg", imageBottomRight)



