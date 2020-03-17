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
        
        allImageViews = []
        for i in range(1, 8):
            for j in range(1, 8):
                allImageViews.append(getView(image, i, j))
        
        # First Case: 7x7
        imageAverage = np.mean(allImageViews, axis=0)
        cv2.imwrite(outputDir + imageName[:-4] + "_aperture_77" + ".jpg", imageAverage)
        print(imageName + " first case done")

        # Second Case: Central 5x5

        imagesToAverage = []
        for i in range (2, 7):
            for j in range(2, 7):
                imagesToAverage.append(allImageViews[(i - 1) * 7 + (j - 1)])

        imageAverage = np.mean(imagesToAverage, axis=0)
        cv2.imwrite(outputDir + imageName[:-4] + "_aperture_55" + ".jpg", imageAverage)
        print(imageName + " second case done")

        # Third Case: Central 3x3

        imagesToAverage = []
        for i in range (3, 6):
            for j in range(3, 6):
                imagesToAverage.append(allImageViews[(i - 1) * 7 + (j - 1)])

        imageAverage = np.mean(imagesToAverage, axis=0)
        cv2.imwrite(outputDir + imageName[:-4] + "_aperture_33" + ".jpg", imageAverage)
        print(imageName + " third case done")

        # Fourth Case: Central View(4,4)

        cv2.imwrite(outputDir + imageName[:-4] + "_aperture_11" + ".jpg", allImageViews[3 * 7 + 3])
        print(imageName + " fourth case done")




