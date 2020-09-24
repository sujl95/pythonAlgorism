b = '10987'
for i in range(len(b)):
    if (b[i] == '0'):
        continue

    # Stores the current number having
    # current digit one less than current
    # digit in b
    curr = list(b)
    print(curr[i], '변경 전')
    curr[i] = str(((ord(curr[i]) - ord('0')) - 1) + ord('0'))
    print(curr[i], '변경 후')

    # Replace all following digits with 9
    # to maximise the product
    for j in range(i + 1, len(curr)):
        curr[j] = str(ord('9'))

        # Convert string to number
    num = 0
    for c in curr:
        num = num * 10 + (int(c) - ord('0'))

print(num)



# # Python3 Program to find the number
# # in a range having maximum product
# # of the digits
#
# # Returns the product of digits
# # of number x
# def product(x):
#     prod = 1
#     while (x):
#         prod *= (x % 10)
#         x //= 10;
#
#     return prod
#
#
# # This function returns the number having
# # maximum product of the digits
# def findNumber(l, r):
#     # Converting both integers to strings
#     a = str(l);
#     b = str(r);
#
#     # Let the current answer be r
#     ans = r
#
#     for i in range(len(b)):
#         if (b[i] == '0'):
#             continue
#
#         # Stores the current number having
#         # current digit one less than current
#         # digit in b
#         curr = list(b)
#         curr[i] = str(((ord(curr[i]) -
#                         ord('0')) - 1) + ord('0'))
#
#         # Replace all following digits with 9
#         # to maximise the product
#         for j in range(i + 1, len(curr)):
#             curr[j] = str(ord('9'))
#
#             # Convert string to number
#         num = 0
#         for c in curr:
#             num = num * 10 + (int(c) - ord('0'))
#
#             # Check if it lies in range and its
#         # product is greater than max product
#         if (num >= l and product(ans) < product(num)):
#             ans = num
#
#     return ans