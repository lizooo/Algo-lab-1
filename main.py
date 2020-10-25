import csv
from random import shuffle
from model import Hotel
from managers.insertion_sort import InsertSort
from managers.quick_sort import QuicksortEnd
from managers.suick_sort_middle_three import QuicksortMiddleThree

if __name__ == '__main__':

    hotels = []
    hotels2 = []
    hotels3 = []

    with open('hotels500.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            hotels.append(Hotel(int(line[0]), line[1], int(line[2])))

    shuffle(hotels)

    hotels2 = hotels.copy()
    hotels3 = hotels.copy()

    insert_sort_instance = InsertSort()
    list_of_hotels_sorted_by_visitors = insert_sort_instance.insertion_sort(hotels, key=lambda hotel: hotel.visitors_per_year)

    quick_sort_end_instance = QuicksortEnd()
    quick_sort_end_instance.quicksort(hotels2, key=lambda hotel: hotel.number_of_rooms)

    quick_sort_mid_instance = QuicksortMiddleThree()
    quick_sort_mid_instance.quick_sort(hotels3, key=lambda hotel: hotel.number_of_rooms)

    print(f'\t\t\t- i n s e t i o n   s o r t    r e s u l t -\n\n {hotels}')
    print(f'\t\t\t- q u i c k   s o r t  w i t h   e n d   p i v o t   r e s u l t -\n\n {hotels2}')
    print(f'\t\t\t- q u i c k   s o r t  w i t h   m i d d l e   p i v o t   r e s u l t -\n\n {hotels3}')