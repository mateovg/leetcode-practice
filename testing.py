import time
from typing import Callable, List


def run_tests(inputs: List[any], expected: List[any], func: Callable) -> None:
    for i, (input, expected) in enumerate(zip(inputs, expected)):
        print(f'Test case {i + 1}')
        start_time = time.time()
        res, output = test(input, expected, func)
        end_time = time.time()
        if not res:
            print(f"Test failed")
            print(f"Output: {output}")
        else:
            print("Test passed")
        print(f"Time: {end_time - start_time:.5f}s")

def test(input: any, output: any, func: Callable) -> bool:
    print("Input:", format_input(input))
    print(f"Expected:", format_expected(output))
    res = func(*input)
    return res == output, res

def format_expected(l: List[any]) -> str:
    if len(l) > 15:
        return ' '.join(map(str, l[:8])) + ' ...' + ' '.join(map(str, l[-8:]))
    return ' '.join(map(str, l))

def format_input(l: List[List[any]]) -> str:
    return ','.join(map(format_expected, l))