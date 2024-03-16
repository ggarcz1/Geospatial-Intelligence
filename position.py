import math


class Position:
    def __init__(self, timeI=0, time=0, speedI=0, speedF=0, accelX=0, accelY=0, accelZ=0, bearingI=0, bearingF=0):
        self.timeI = timeI
        self.time = time
        self.speedI = speedI
        self.speedF = speedF
        self.accelX = accelX
        self.accelY = accelY
        self.accelZ = accelZ
        self.bearingI = bearingI
        self.bearingF = bearingF

    # returns a pretty string representation of the coordinates
    def __str__(self):
        return f'Position(timeI={self.timeI}, time={self.time}, ' \
               f'speedI={self.speedI}, speedF={self.speedF}, ' \
               f'accelX={self.accelX}, accelY={self.accelY}, accelZ={self.accelZ}, ' \
               f'bearingI={self.bearingI}, bearingF={self.bearingF})'

    # returns a list of the coordinates
    def values(self) -> list:
        return [self.timeI, self.time,
                self.speedI, self.speedF,
                self.accelX, self.accelY, self.accelZ,
                self.bearingI, self.bearingF]

    # def