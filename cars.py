import csv
import os


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, passenger_seats_count, photo_file_name, carrying):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'car'
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, body_whl, carrying):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        self.body_width = 0
        self.body_height = 0
        self.body_length = 0
        if body_whl:
            whl = body_whl.split('x')
            self.body_length = float(whl[0])
            self.body_width = float(whl[1])
            self.body_height = float(whl[2])

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'spec_machine'
        self.extra = extra


def make_car(row):
    brand = row[1]
    passenger_seats_count = row[2]
    photo_file_name = row[3]
    carrying  = row[5]


def make_truck(row):
    brand = row[1]
    passenger_seats_count = row[2]
    photo_file_name = row[3]
    carrying  = row[5]


def make_truck(row):
    brand = row[1]
    passenger_seats_count = row[2]
    photo_file_name = row[3]
    carrying = row[5]
    extra  = row[6]


def get_car_list(csv_filename):
    car_list = []

    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            try:
                pass
            except:
                pass
        return car_list


if __name__ == '__main__':
    print(get_car_list('cars.csv'))
