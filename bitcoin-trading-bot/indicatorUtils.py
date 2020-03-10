


def calculateMovingAverage(period, data):
    average = 0
    for x in range(period):
        average = average + data.get[x-1]

    return average/ period