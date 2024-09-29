from typing import List
from testing import run_tests
from random import shuffle

def merge_sort(numbers: List[int]) -> List[int]:
    if len(numbers) <= 1:
        return numbers
    mid_point = len(numbers) // 2
    left = merge_sort(numbers[:mid_point])
    right = merge_sort(numbers[mid_point:])
    return merge(left, right)

def merge(left: List[int], right: List[int]) -> List[int]:
    """
    Take two sorted arrays and returns them merged inorder
    """
    sorted_array = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            sorted_array.append(left[l])
            l += 1
        else:
            sorted_array.append(right[r])
            r += 1
    
    sorted_array.extend(left[l:])
    sorted_array.extend(right[r:])
        
    return sorted_array

# Generate test cases
# TODO: Make this work
from typing import Generator

def generate_test_cases(length: int) -> Generator[List[List[int]], None, None]:
    """
    Generates test cases for sorting.
    
    Parameters:
    cases (int): The number of test cases to generate.
    length (int): The length of each list in the test cases.
    
    Returns:
    List[List[List[int]]]: A list of test cases, where each test case contains a pair:
                           [unsorted list, sorted list].
    """
    unsorted_list = list(range(1, length + 1))
    shuffle(unsorted_list)  
    expected = list(range(1, length + 1))
    yield [unsorted_list, expected]
# print(generate_test_cases(10, 10))
# run_tests(generate_test_cases(10, 10000), merge_sort)