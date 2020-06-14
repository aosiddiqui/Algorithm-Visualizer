import time


class QSort:
    """
    Class that implements Quick sort.

    Attributes:
    -----------
    data -- a Python list containing the elements to be sorted.

    Methods:
    --------
    partition(head, tail, drawData) -- returns the index of the element from
                                       where partitioning is to be done.
    quickSort(head, tail, drawData) -- implements quick sort.
    getColorArray(head, tail, border, currIdx, isSwaping=False) -- generates a
                                                                   color array.
    """

    def __init__(self, data):
        """
        Constructs all the necessary attributes for the QSort object.

        Arguments:
        self.data = data

        Returns:
        None
        """

        self.data = data

    def partition(self, head, tail, drawData, timeTick):
        """
        Returns the element index from which partitioning needs to be done.

        Arguments:
        head -- starting index of the sublist
        tail -- ending index of the sublist
        drawData -- a function to draw on the Canvas
        timeTick -- time taken between two consecutive snapshots of the canvas

        Returns:
        border -- the element from which partitioning needs to be done
        """

        border = head
        pivot = self.data[tail]

        drawData(self.data, self.getColorArray(head, tail, border, border))
        time.sleep(timeTick)

        for j in range(head, tail):
            if self.data[j] < pivot:
                drawData(self.data, self.getColorArray(head, tail, border, j))
                time.sleep(timeTick)
                drawData(self.data, self.getColorArray(head, tail, border, j, True))
                time.sleep(timeTick)
                self.data[border], self.data[j] = self.data[j], self.data[border]
                border += 1
            drawData(self.data, self.getColorArray(head, tail, border, j))
            time.sleep(timeTick)

        #swap pivot with border value
        drawData(self.data, self.getColorArray(head, tail, border, tail, True))
        time.sleep(timeTick)
        self.data[border], self.data[tail] = self.data[tail], self.data[border]
        return border

    def quickSort(self, head, tail, drawData, timeTick):
        """
        Performs Quick sort on the data list.

        Arguments:
        head -- starting index of the sublist
        tail -- ending index of the sublist
        drawData -- a function to draw on the Canvas
        timeTick -- time taken between two consecutive snapshots of the canvas

        Returns:
        None
        """

        if head < tail:
            partitionIdx = self.partition(head, tail, drawData, timeTick)

            # Left partition
            self.quickSort(head, partitionIdx-1, drawData, timeTick)

            # Right partition
            self.quickSort(partitionIdx+1, tail, drawData, timeTick)


    def getColorArray(self, head, tail, border, currIdx, isSwaping = False):
        """
        Generates a color array.

        Arguments:
        head -- starting index of the sublist
        tail -- ending index of the sublist
        border -- index of the border element
        currIdx -- index of the current element
        isSwaping -- boolean variable representing whether the swapping needs to be done or not

        Returns:
        colorArray -- a sequence of colors
        """
        colorArray = []
        for i in range(len(self.data)):
            # Base coloring
            if i >= head and i <= tail:
                colorArray.append('gray')
            else:
                colorArray.append('white')

            # Specific coloring
            if i == tail:
                colorArray[i] = 'blue'
            elif i == border:
                colorArray[i] = 'red'
            elif i == currIdx:
                colorArray[i] = 'yellow'

            if isSwaping:
                if i == border or i == currIdx:
                    colorArray[i] = 'green'

        return colorArray
