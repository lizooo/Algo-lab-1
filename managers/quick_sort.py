from timeit import default_timer as timer
from datetime import timedelta


class QuicksortEnd:

    def __init__(self, swap_count=0, comparison_count=0):
        self.swap_count= swap_count
        self.comparison_count = comparison_count

    def quicksort(self, entry_list, key=lambda obj: obj):
        self.sorting_start_time = timer()
        self.quicksort_helper(entry_list, 0, len(entry_list) - 1, key)
        self.sorting_end_time = timer()

        print('\n \t\t  - q u i c k    s o r t   e n d   p i v o t - \n')
        print(f'executed in {timedelta(seconds=self.sorting_end_time - self.sorting_start_time)}')
        print(f'number of swaps = {self.swap_count} ')
        print(f'number of comparisons = {self.comparison_count} \n')

        return entry_list

    def quicksort_helper(self, entry_list, left, right, key):
        if left < right:
            self.comparison_count += 1
            pivot_final_resting_position = self.partition(entry_list, left, right, key)

            self.quicksort_helper(entry_list, left, pivot_final_resting_position - 1, key)
            self.quicksort_helper(entry_list, pivot_final_resting_position + 1, right, key)

    def partition(self, entry_list, left, right, key):
        pivot = key(entry_list[right])
        #                                                   8 3 6 4 1 7 9 3
        border = left - 1
        for iterator in range(left, right):
            self.comparison_count += 1
            if key(entry_list[iterator]) <= pivot:
                border += 1
                self.swap(entry_list, border, iterator)

        self.swap(entry_list, border+1, right)
        return border + 1

    def swap(self, entry_list, first_element, second_element):
        self.swap_count += 1
        placeholder = entry_list[first_element]
        entry_list[first_element] = entry_list[second_element]
        entry_list[second_element] = placeholder




