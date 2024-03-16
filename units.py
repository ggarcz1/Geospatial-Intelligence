class Units:
    def __init__(self, measure_distance: str, measure_time: str) -> None:
        dist = type(measure_distance)
        time = type(measure_time)
        if dist is str and time is str:
            self.measure_distance = measure_distance
            self.measure_time = measure_time
        else:
            self.measure_distance = self.measure_time = None

    def __str__(self) -> str:
        return f'{self.measure_distance}/{self.measure_time}'

    # returns a list of the items
    def display(self) -> list:
        return [f'{self.measure_distance}/{self.measure_time}']

    # TODO:
    # distance = ['mile', 'feet', 'inches', 'centimeter', 'meter', 'kilometer']
    #
    # time = ['millisecond', 'second', 'minute', 'hour']
    # #
    # if measure_distance in distance and measure_time in time:
    #     units = f'{measure_distance}/{measure_time}'
    # else:
    #     units = f'Error. Incompatible units measure_distance={measure_distance} and measure_time={measure_time}'
