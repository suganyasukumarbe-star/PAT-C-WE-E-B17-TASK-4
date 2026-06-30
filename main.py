

numbers=[10,501,22,37,100,999,87,351]
even_list=[num for num in numbers if num % 2 == 0]
odd_list=[num for num in numbers if num % 2 != 0]
print("Even List:", even_list)
print("Odd List:", odd_list)

def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
numbers=[10,501,22,37,100,999,87,351]
prime_list=[num for num in numbers if is_prime(num)]
print("Prime Numbers List:",prime_list)
print("Count of Prime Numbers:",len(prime_list))

def is_happy(n):
    seen=set()
    while n !=1 and n not in seen:
        seen.add(n)
        n=sum(int(digit) ** 2 for digit in str(n))
    return n==1
numbers=[10,501,22,37,100,999,87,351]
happy_numbers=[num for num in numbers if is_happy(num)]
print("Happy Numbers in list:",happy_numbers)
print("Total Count of Happy Numbers:",len(happy_numbers))

def sum_first_last(number):
    num_str=str(abs(number))
    first_digit=int(num_str[0])
    last_digit=int(num_str[-1])
    return first_digit+last_digit
num=9384
print(f"Sum of first and last digit of {num}:",sum_first_last(num))


def find_coin_combinations(coins1, target, index, current_comb, result):
    if target==0:
        result.append(list(current_comb))
        return
    if target<0 or index>=len(coins1):
        
        return

    # Include current coin
    current_comb.append(coins1[index])
    find_coin_combinations(coins1, target - coins1[index], index, current_comb, result)
    current_comb.pop()  # Backtrack

    # Skip current coin
    find_coin_combinations(coins1, target, index + 1, current_comb, result)

coins=[1,2,5,10]
combinations=[]
find_coin_combinations(coins, 10, 0, [], combinations)

print(f"Total ways: {len(combinations)}")
print("All combinations:")
for combo in combinations:
    print(combo)


list1 = [1, 2, 3, 4, 5, 9]
list2 = [3, 4, 5, 6, 7, 9]
list3 = [5, 8, 9, 10, 11]

# Finds elements present in all three lists
duplicates = list(set(list1) & set(list2) & set(list3))
print("Duplicate elements across all three lists:", duplicates)

from collections import Counter
def first_non_repeating(lst):
    counts = Counter(lst)
    for num in lst:
        if counts[num] == 1:
            return num
    return None

items = [2, 3, 4, 2, 3, 5, 4, 6]
print("First non-repeating element:", first_non_repeating(items))


def find_min_rotated(arr):
    low, high = 0, len(arr) - 1

    while low < high:
        mid = (low + high) // 2
        # If mid-element is greater than high element, minimum is on the right
        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid

    return arr[low]


rotated_list = [4, 5, 6, 7, 1, 2, 3]
print("Minimum element is:", find_min_rotated(rotated_list))


def find_triplet(lst, target):
    n = len(lst)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if lst[i] + lst[j] + lst[k] == target:
                    return [lst[i], lst[j], lst[k]]
    return None

given_list = [10, 20, 30, 9]
target_val = 59

print("Triplet found:", find_triplet(given_list, target_val))


def has_zero_sum_sublist(lst):
    sum_set = set()
    running_sum = 0

    for num in lst:
        running_sum += num
        if running_sum == 0 or running_sum in sum_set:
            return True
        sum_set.add(running_sum)

    return False


test_list = [4, 2, -3, 1, 6]
print("Does a zero-sum sublist exist?:", has_zero_sum_sublist(test_list))




