# list reversed
def get_list_from_user():
    user_input = input("Enter list items separated by comma: ")
    return [item.strip() for item in user_input.split(',')]

def reverse_list_slicing(lst):
    return lst[::-1]

def reverse_list_loop(my_list):
    reversed_list=[]
    for i in range(len(my_list) - 1, -1, -1):
        reversed_list.append(my_list[i])
    return reversed_list

def reverse_list_inplace(my_list):
    left = 0
    right = len(my_list) - 1
    while left < right:
        my_list[left], my_list[right] = my_list[right], my_list[left]
        left += 1
        right -= 1
    return my_list

if __name__ == "__main__":
    my_list = get_list_from_user()
    print(f"\n Original List: {my_list}")
    print(f" Reverser (slicing): {reverse_list_slicing(my_list)}")
    print(f" Reversed (loop): {reverse_list_loop(my_list)}")
    print(f" Reversed (in-place): {reverse_list_inplace(my_list.copy())}")