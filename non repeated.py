def find_non_repeating(arr):
    count_dict = {}
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    for num, count in count_dict.items():
        if count == 1:
            return num
    
    # If no non-repeating element is found
    return None

# Example usage:
arr = [1, 2, 3, 2, 1, 4, 4]
result = find_non_repeating(arr)
if result is not None:
    print("Non-repeating element:", result)
else:
    print("No non-repeating element found")
