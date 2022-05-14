import json

def load_json(filename):
    json_file = filename
    with open(json_file, 'r') as file:
        car_config = json.load(file)
    # now car_config is a dictionary equivalent to the JSON file
    return car_config


#
# def get_mat_bord():
#     """:return list of list - the bord game (matrix)"""
#
#     length = 7
#     all_cars_dict ={"O":[2,[2,3],0],"R":[2,[0,0],1]}
#     bord_lst = []
#
#     for row in range(length):
#         bord_lst.append(['_'] * length)
#
#     for x in all_cars_dict:
#         tmp_min_cor = all_cars_dict[x][1]
#             car_coordinates()
#
#
#     print(len(all_cars_dict))
#
# get_mat_bord()
# t = {'y': 1,'e':2}
# for key, valuein in enumerate(t):
#     print(key)
#     pr
#     # print(value)
#
# print(t.values())
# def make_upper():
# #     x = input('here')
# #     x = x.upper()
# #     print(x)
# # # make_upper()
# #
# # def trry():
# #     x = 1
# #     while x != 2:
# #         x += 1
# #         if x == 3:
# #             break
# #     else:
# #         print('stay')
# # trry()


