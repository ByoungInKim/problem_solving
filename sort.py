import unittest

def bubble_sort(unsorted_lists):
    for i in range(0, len(unsorted_lists) - 1):
        for j in range(0, len(unsorted_lists) - 1):
            if (unsorted_lists[j] > unsorted_lists[j + 1]):
                unsorted_lists[j], unsorted_lists[j + 1]= unsorted_lists[j + 1], unsorted_lists[j]
                
    return unsorted_lists

def selection_sort(unsorted_lists):
    for i in range(0, len(unsorted_lists) - 1):
        min_index = i
        for j in range(i + 1, len(unsorted_lists)):
            if unsorted_lists[min_index] > unsorted_lists[j]:
                min_index = j
        unsorted_lists[i], unsorted_lists[min_index] = unsorted_lists[min_index], unsorted_lists[i]

    return unsorted_lists

def insertion_sort(unsorted_lists):
    for i in range(1, len(unsorted_lists)):
        start_index = i
        for j in range(i - 1, -1, -1):
            if unsorted_lists[j] > unsorted_lists[start_index]:
                unsorted_lists[j], unsorted_lists[start_index] = unsorted_lists[start_index], unsorted_lists[j]
                start_index = j
    return unsorted_lists

def merge_sort(unsorted_lists):
    sorted_list = []
    if len(unsorted_lists) > 1:
        half = int(len(unsorted_lists) / 2)
        left_list = unsorted_lists[:half]
        right_list = unsorted_lists[half:]

        left_list = merge_sort(left_list)
        right_list = merge_sort(right_list)

        left_index = 0
        right_index = 0
        while(True):
            if left_index >= len(left_list) and right_index >= len(right_list):
                break

            if len(left_list) <= left_index:
                sorted_list.append(right_list[right_index])
                right_index += 1
                continue
            elif len(right_list) <= right_index:
                sorted_list.append(left_list[left_index])
                left_index += 1
                continue

            if left_list[left_index] <= right_list[right_index]:
                sorted_list.append(left_list[left_index])
                left_index += 1
            else:
                sorted_list.append(right_list[right_index])
                right_index += 1
                                
        return sorted_list
    else:
        sorted_list += unsorted_lists
        return sorted_list

class unit_test(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertEqual([1, 2, 3, 4, 5, 6], bubble_sort([1, 3, 2, 5, 6, 4]))
        self.assertEqual([1, 2, 3, 4, 5, 6], bubble_sort([6, 4, 3, 1, 2, 5]))
        self.assertEqual([1, 2, 3, 4, 5, 6], bubble_sort([4, 1, 6, 3, 2, 5]))

    def test_selection_sort(self):
        self.assertEqual([1, 2, 3, 4, 5, 6], selection_sort([1, 3, 2, 5, 6, 4]))
        self.assertEqual([1, 2, 3, 4, 5, 6], selection_sort([6, 4, 3, 1, 2, 5]))
        self.assertEqual([1, 2, 3, 4, 5, 6], selection_sort([4, 1, 6, 3, 2, 5]))
    
    def test_insertion_sort(self):
        self.assertEqual([1, 2, 3, 4, 5, 6], insertion_sort([1, 3, 2, 5, 6, 4]))
        self.assertEqual([1, 2, 3, 4, 5, 6], insertion_sort([6, 4, 3, 1, 2, 5]))
        self.assertEqual([1, 2, 3, 4, 5, 6], insertion_sort([4, 1, 6, 3, 2, 5]))
    
    def test_merge_sort(self):
        self.assertEqual([1, 2, 3, 4, 5, 6], merge_sort([1, 3, 2, 5, 6, 4]))
        self.assertEqual([1, 2, 3, 4, 5, 6], merge_sort([6, 4, 3, 1, 2, 5]))
        self.assertEqual([1, 2, 3, 4, 5, 6], merge_sort([4, 1, 6, 3, 2, 5]))
    