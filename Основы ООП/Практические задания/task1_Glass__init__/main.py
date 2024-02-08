from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        # TODO инициализировать объект "Стакан"
        if not isinstance(capacity_volume, (int, float)) or not isinstance(occupied_volume, (int, float)):
            raise TypeError('Ошибка типа! Параметр должен быть int или float')

        if capacity_volume < 0 or occupied_volume < 0:
            raise ValueError('Ошибка! Объем не может быть отрицательным')

        if capacity_volume < occupied_volume:
            raise ValueError('Ошибка! Реальный объем не может быть меньше занятого')
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume


if __name__ == "__main__":
    # TODO инициализировать два объекта типа Glass
    glass1 = Glass(500.6, 300)
    print(glass1.capacity_volume, glass1.occupied_volume)
    glass2 = Glass(250, 300)
    print(glass2.capacity_volume, glass2.occupied_volume)

    # TODO попробовать инициализировать не корректные объекты
