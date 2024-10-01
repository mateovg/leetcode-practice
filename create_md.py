import os
import sys
import re

table_header = """
| Problem                                        | Tags         | Approach | Notes/Follow Ups |
"""

"""
example file:
## Array

 - [x] 1. [Two Sum](https://leetcode.com/problems/two-sum)

 - [ ] 2. [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock)

 - [ ] 3. [Majority Element](https://leetcode.com/problems/majority-element)
"""

def create_md(file_name):
    # Read
    with open(file_name, 'r') as f:
        print(f"Reading {file_name}")
        lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
    # Write
    with open('problems.md', 'w') as f:
        f.write(table_header)
        for line in lines:
            # We want to match the markdown link so [problem_name](link)
            problem = re.search(r'\d+\.\s+\[([^\]]+)\]\(([^)]+)\)', line)
            if problem:
                problem_name = problem.group(1)
                problem_link = problem.group(2)
                f.write(f'| [{problem_name}]({problem_link}) | | | |\n')
                
                
if __name__ == '__main__':
    create_md('problems')