
# 1. question

def question1(first_list: List[int], second_list: List[int]) -> List[int]:
    res: List[int] = []
    for el_first_list in first_list:
        if el_first_list in second_list:  # Fix here
            res.append(el_first_list)
    return res

# This will be a complexity of O(n). Since each list will take a complexity of O(n to complete.

# 2. question.

def question2(n: int) -> int:
    for _ in range(10):
        n **= 3
    return n

# Since the loop runs a fixed number of times (10 iterations), does the same fixed calc.
# The Complexity will be O(1).


# 3. question

def question3(first_list: List[int], second_list: List[int]) -> List[int]:
    temp: List[int] = first_list[:]
    for el_second_list in second_list:
        flag = False
        for check in temp:
            if el_second_list == check:  # Fix here
                flag = True
                break
        if not flag:
            temp.append(el_second_list)
    return temp

# In this code there is a nested loop.
# Complexity is O(n2)

# 4. question

def question4(input_list: List[int]) -> int:
    res: int = 0
    for el in input_list:
        if el > res:
            res = el
    return res

# the function will iterate over all elements once,
# So the time complexity will be O(n).

