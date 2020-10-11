from timeit import default_timer as timer
from datetime import timedelta


class QuicksortMiddleThree:

    def __init__(self, swap_count_middle_three=0, comparison_count_middle_three=0):
        self.swap_count_middle_three = swap_count_middle_three
        self.comparison_count_middle_three = comparison_count_middle_three

    def quick_sort(self, entry_list, key=lambda obj: obj):

        self.quicksort_middle_start_time = timer()
        self.quick_sort_helper(entry_list, 0, len(entry_list) - 1, key)
        self.quicksort_middle_end_time = timer()

        print('\n \t\t  - q u i c k    s o r t   m i d d l e    p i v o t - \n')
        print(f'executed in {timedelta(seconds=self.quicksort_middle_end_time - self.quicksort_middle_start_time)}')
        print(f'number of swaps = {self.swap_count_middle_three} ')
        print(f'number of comparisons = {self.comparison_count_middle_three} \n')

        return entry_list

    def quick_sort_helper(self, entry_list, left, right, key):
        if left < right:
            self.comparison_count_middle_three +=1
            pivot_index = self.partition(entry_list, left, right, key)
            self.quick_sort_helper(entry_list, left, pivot_index - 1, key)
            self.quick_sort_helper(entry_list, pivot_index + 1, right, key)

    def partition(self, entry_list, left, right, key):
        pivot_index = self.get_pivot(entry_list, left, right, key)
        pivot_value = key(entry_list[pivot_index])
        self.swap(entry_list, pivot_index, left)
        border = left

        for i in range(left, right + 1):
            self.comparison_count_middle_three += 1
            if key(entry_list[i]) < pivot_value:
                border += 1
                self.swap(entry_list, i, border)
        self.swap(entry_list, left, border)

        return border

    def get_pivot(self, entry_list, left, rihgt, key):
        mid = (rihgt + left) // 2
        three_element_list = sorted([entry_list[left], entry_list[mid], entry_list[rihgt]], key=key)
        if three_element_list[1] == key(entry_list[left]):
            return left
        elif three_element_list[1] == key(entry_list[mid]):
            return mid
        return rihgt

    def swap(self, entry_list, first_element, second_element):
        self.swap_count_middle_three += 1
        placeholder = entry_list[first_element]
        entry_list[first_element] = entry_list[second_element]
        entry_list[second_element] = placeholder
