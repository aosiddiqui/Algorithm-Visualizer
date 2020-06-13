import time

class BSort:

    def bubbleSort(data, drawData, timeTick):
        for i in range(len(data)-1):
            for j in range(len(data)- i-1):
                drawData(data, ['blue' if x == j or x == j+1 else 'yellow' for x in range(len(data))])
                time.sleep(timeTick)

                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
                    time.sleep(timeTick)
        drawData(['blue' for x in range(len(data))], data)