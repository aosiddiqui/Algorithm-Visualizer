import time

class MSort:
    """
    Class that implements Merge sort.

    Attributes:
    -----------
    data -- a Python list containing the elements to be sorted.

    Methods:
    --------
    mergeSort(drawData, timeTick) -- performs merge sort.
    merge(left, middle, right, drawData, timeTick) -- merges the left and right
                                                      sublists.
    getColorArray(left, middle, right) -- generates a color array.
    """

    def __init__(self, data):
        """
        Constructs all the necessary attributes for the MSort object.

        Arguments:
        self.data = data

        Returns:
        None
        """

        self.data = data

    def mergeSort(self, left, right, drawData, timeTick):
        """
        Performs Merge sort on the data list.

        Arguments:
        left -- starting index of the sublist
        right -- ending index of the sublist
        drawData -- a function to draw on the Canvas
        timeTick -- time taken between two consecutive snapshots of the Canvas

        Returns:
        None
        """

        if left < right:
            middle = (left + right) // 2
            self.mergeSort(left, middle, drawData, timeTick)
            self.mergeSort(middle+1, right, drawData, timeTick)
            self.merge(left, middle, right, drawData, timeTick)

    def merge(self, left, middle, right, drawData, timeTick):
        """
        Merges the left and right sublists.

        Arguments:
        left -- starting index of the sublist
        middle -- middle element index of the sublist which needs to be sorted
        right -- ending index of the sublist
        drawData -- a function to draw on the Canvas
        timeTick -- time taken between two consecutive snapshots of the canvas

        Returns:
        None
        """

        drawData(self.data, self.getColorArray(left, middle, right))
        time.sleep(timeTick)

        leftPart = self.data[left:middle+1]
        rightPart = self.data[middle+1: right+1]

        leftIdx = rightIdx = 0

        for dataIdx in range(left, right+1):
            if leftIdx < len(leftPart) and rightIdx < len(rightPart):
                if leftPart[leftIdx] <= rightPart[rightIdx]:
                    self.data[dataIdx] = leftPart[leftIdx]
                    leftIdx += 1
                else:
                    self.data[dataIdx] = rightPart[rightIdx]
                    rightIdx += 1

            elif leftIdx < len(leftPart):
                self.data[dataIdx] = leftPart[leftIdx]
                leftIdx += 1
            else:
                self.data[dataIdx] = rightPart[rightIdx]
                rightIdx += 1

        drawData(self.data, ["green" if x >= left and x <= right else "white" for x in range(len(self.data))])
        time.sleep(timeTick)

    def getColorArray(self, left, middle, right):
        """
        Generates a color array.

        Arguments:
        left -- starting index of the sublist
        middle -- middle element index of the sublist which needs to be sorted
        right -- ending index of the sublist

        Returns:
        colorArray -- a color sequence
        """

        colorArray = []
        for i in range(len(self.data)):
            if i >= left and i <= right:
                if i <= middle:
                    colorArray.append("yellow")
                else:
                    colorArray.append("blue")
            else:
                colorArray.append("white")

        return colorArray
