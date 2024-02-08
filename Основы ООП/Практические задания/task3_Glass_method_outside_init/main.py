from typing import Union


class Glass:
    def __init__(self, occupied_volume: Union[int, float]):
        #  TODO заменить на метод
        self.capacity_volume = None

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0:
            raise ValueError
        self.occupied_volume = occupied_volume  # объем жидкости в стакане

#  TODO создать метод, который будет инициализировать атрибут capacity_volume
    def init_capacity_volume(self, capacity_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError('Объем стакана должен быть int или float')
        if capacity_volume < 0:
            raise ValueError('Объем стакана должен быть больше нуля')
        self.capacity_volume = capacity_volume


if __name__ == "__main__":
    glass = Glass(100)  # TODO инициализировать экземпляр класса Glass
    glass.init_capacity_volume(200)
    print(glass.capacity_volume)  # TODO распечатать атрибут capacity_volume
    print(glass.occupied_volume)  # TODO распечатать атрибут occupied_volume
