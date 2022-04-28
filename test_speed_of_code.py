import time

array1 = [n for n in range(1, 500)]
array2 = [m for m in range(1000, 500, -1)]

def check_function(arr1, arr2):
    for i in arr1:
        for j in arr2:
            if i == j:
                return "True"
    return "False"


def check_function2(arr1, arr2):
    for i in arr1:
        if i in arr2:
            return "True"
    return "False"

def check_function3(arr1, arr2):
    if set(arr1).intersection(arr2):
        return "True"
    else:
        return "False"

start = time.time()
print("answer: ", check_function(array1, array2)) 
print("Function spent times: ", (time.time() - start)*1000000, "μs") 

start = time.time()
print("answer: ", check_function2(array1, array2)) 
print("Function spent times: ", (time.time() - start)*1000000, "μs") 

start = time.time()
print("answer: ", check_function3(array1, array2)) 
print("Function spent times: ", (time.time() - start)*1000000, "μs") 