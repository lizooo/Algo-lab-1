class Hotel:

    def __init__(self, visitors_per_year: int, hotel_name: str, number_of_rooms: int):
        self.visitors_per_year = visitors_per_year
        self.hotel_name = hotel_name
        self.number_of_rooms = number_of_rooms

    def __str__(self):
        return ' '.join(
            ['{key}={value},'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__]) + '\n'

    def __repr__(self):
        return str(self)