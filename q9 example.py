# def is_present_in_list(number_to_search, list_to_search):
#     length_of_list = len(list_to_search)
#     if length_of_list == 0:
#         return False
#     if length_of_list == 1:
#         if number_to_search == list_to_search[0]:
#             return True
#         else:
#             return False
#     first_half_of_list = list_to_search[:length_of_list/2]
#     second_half_of_list = list_to_search[length_of_list/2:]
#     return is_present_in_list(number_to_search, first_half_of_list) or is_present_in_list(number_to_search, second_half_of_list)
# print (is_present_in_list(3, [3, 5, 7, 8, 4, 6, 2, 1, 9]))
# print (is_present_in_list(10, [3, 5, 7, 8, 4, 6, 2, 1, 9]))

# def is_present_in_list(number_to_search, list_to_search):
#     counter = 0
#     while (counter < len(list_to_search)):
#         if number_to_search == list_to_search[counter]:
#             return True
#         counter += 1
#     return False
# print (is_present_in_list(3,[3, 5, 7, 8, 4, 6, 2, 1, 9]))
# print (is_present_in_list(10, [3, 5, 7, 8, 4, 6, 2, 1, 9]))