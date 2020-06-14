import time


class BSort:
    """
    Class that implements Bubble sort.

    Attributes
    -----------
    data -- a Python list containing the elements to be sorted.

    Methods
    --------
    bubbleSort(drawData, timeTick) -- implements Bubble sort.
    getColorArray(currIdx, loopnum) -- generates a color array.
    """

    def __init__(self, data):
        """
        Constructs all the necessary attributes for the BSort object.

        Arguments:
        self.data = data

        Returns:
        None
        """
        self.data = data

    def bubbleSort(self, drawData, timeTick):
        """
        Performs Bubble sort on the data list.

        Arguments:
        drawData -- a function to draw on the Canvas
        timeTick -- time taken between two consecutive snapshots of the canvas

        Returns:
        None
        """

        for i in range(len(self.data)-1):
            for j in range(len(self.data) - i-1):
                drawData(self.data, self.getColorArray(j, i))
                time.sleep(timeTick)

                if self.data[j] > self.data[j+1]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]
                    drawData(self.data, self.getColorArray(j, i))
                    time.sleep(timeTick)
            time.sleep(timeTick)

    def getColorArray(self, currIdx, loopnum):
        """
        Generates a color array.

        Arguments:
        currIdx -- index of the current element
        loopnum -- depicting the loop number

        Returns:
        colorArray -- a sequence of colors
        """

        colorArray = []
        for x in range(len(self.data)):
            if x == currIdx or x == currIdx+1:
                colorArray.append('blue')
            elif x > len(self.data) - loopnum - 1:
                colorArray.append('green')
            else:
                colorArray.append('yellow')
        return colorArray
