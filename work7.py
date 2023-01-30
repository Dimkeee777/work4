# nums = [5, 7, 2, 4, 7, True, "hello", 6.7, [5, 7]]
#
# nums[0] = 50
# nums[5] = 1
#
#
# print(nums[-1][1])

# numbers = [5, 2, 7]
# numbers.append(100)
# numbers.insert(1, True)
#
# b = [5, 6, 8]
# numbers.extend(b)
# numbers.sort()
# # numbers.reverse()
#
# numbers.pop(-2)
# numbers.remove(6)
#
# # numbers.clear()
#
# # print(numbers.count(True))
#
# print(len(numbers))


# nums = [5, 2, 7, "50", False]
#
# for element in nums:
#     element *= 2
#     print(element)

n = int(input("Enter lenght: "))

user_list = []

i = 0

while i < n:
    string = "Enter element #" + str(i + 1) + ": "
    user_list.append(input(string))
    i += 1

print(user_list)



