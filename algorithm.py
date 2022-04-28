import time

set_1 = [1, 2, 3, 9] 
set_2 = [1, 2, 4, 4]
set_3 = [6, 4, 3, 2, 1, 7]

# 8, 8, 9

def algorithm(array, sum):
    if max(array) == sum:
        print("True if")

    elif max(array) > sum:
        for i in array:
            for j in array:
                if i - j == sum:
                    print("True elif")
                    break
    else:
        for i in array:
            for j in array:
                if i + j == sum:
                    print("True else")
                    break


def algorithm_2(array, sum):
    if max(array) == sum:
        print("True if")

    elif max(array) > sum:
        for i in array:
           if max(array) - i == sum:
               print("True elif")
    else:
        for i in array:
            if max(array) + i == sum:
               print("True else")

start = time.time()
algorithm(set_3, 9)
print("The time is: ", (time.time() - start)*1000000, "μs")

start = time.time()
algorithm_2(set_3, 9)
print("The time is: ", (time.time() - start)*1000000, "μs")