from timeit import default_timer as timer
from datetime import timedelta


class InsertSort:

    def __init__(self, swap_count=0, comparison_count=0):
        self.swap_count = swap_count
        self.comparison_count = comparison_count

    def insertion_sort(self, entry_list, key=lambda obj: obj):
        insertion_start_time = timer()

        for i in range(1, len(entry_list)):
            current_number = entry_list[i]
            j = i - 1
            while j >= 0 and key(entry_list[j]) < key(current_number):
                self.comparison_count += 2
                entry_list[j + 1] = entry_list[j]
                j -= 1
                self.swap_count += 1
            entry_list[j + 1] = current_number
            self.swap_count += 1

        print( '\n \t\t\t\t  - i n s e r t i o n     s o r t - \n')
        print(f'executed in {timedelta(seconds=timer() - insertion_start_time)}')
        print(f'number of swaps = {self.swap_count} ')
        print(f'number of comparisons = {self.comparison_count} \n')
        return entry_list