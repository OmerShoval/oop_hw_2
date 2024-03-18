def sum_of_array(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum_of_array(arr[1:])


arr = [1, 2, 3, 4, 5]
print(sum_of_array(arr))


def length_of_string(s):
    if s == '':
        return 0
    else:
        return 1 + length_of_string(s[1:])


test_strings = ["hello", "", "a", "OpenAI", "recursive function"]
for test in test_strings:
    print(f"The length of '{test}' is {length_of_string(test)}.")
