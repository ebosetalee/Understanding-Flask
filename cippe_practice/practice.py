import json


# with open("files/small_chops/samosa.json", "r") as data_file:
#         food = json.load(data_file)
#         ingredients = food["ingredients"]
#         # if ingredients[0]:
#         #     # print(food["ingredients"][1])
#         #     prep = food["ingredients"][0]
#         #     for index, item in enumerate(food["ingredients"]):
#                 # print(item.keys())
#                 # count = len(item[key])
#                 # print(count)
#         for item in ingredients:
#             if not item["name"]:
#                 for key in item.keys():
#                     # print(key)
#                     # print(item[key])
#                     # count = len(item[key])
#                     # print(count)
#                     if item[key] == dict:
#                         for names in item[key]:
#                             print(names["name"])
#                             print(names["quantity"])
#                             if names.get("type"):
#                                 print(names["type"])
#                             if names.get("requirement"):
#                                 print(names["requirement"])
#                             # count -= 1
#                     # prep = food["ingredients"][index]
#                     else:
#                         print("wowow")
#                         # print(item["name"])
#                         # print(item["quantity"])
#                         # if item.get("type"):
#                         #     print(item["type"])
#                         # if item.get("requirement"):
#                         #     print(item["requirement"])
#             else:
#                 print(item["name"])
#                 print(item["quantity"])
#                 if item.get("type"):
#                     print(item["type"])
#                 if item.get("requirement"):
#                     print(item["requirement"])




# with open("files/classic_hamburger.json", "r") as data_file:
#     food = json.load(data_file)
#     ingredients = food["ingredients"]
#     for item in ingredients:
        # if type(item) is dict:
        #     if item.get("name"):
        #         print(item["name"])
        #         if item.get("quantity"):
        #             print(item["quantity"])
        #         if item.get("type"):
        #             print(item["type"])
        #         if item.get("requirement"):
        #             print(item["requirement"])
        #     else:
        #         for key in item.keys():
        #             for names in item[key]:
        #                 if type(names) is dict:
        #                     print(names["name"])
        #                     print(names["quantity"])
        #                     if names.get("type"):
        #                         print(names["type"])
        #                     if names.get("requirement"):
        #                         print(names["requirement"])
        #                 else:
        #                     # print("category")
        #                     # print(names)
        #                     print(names)
#         else:
#             print(item)
"pancakes_and_scrambled_eggs/scrambled_eggs"


# with open("files/pancakes_and_scrambled_eggs/pancakes.json", "r") as data_file:
#     food = json.load(data_file)
    # steps = food["steps"]
    # for item in steps:
    #     if type(item) is dict:
    #         if item.get("action"):
    #             print(item["action"])
    #             if item.get("image"):
    #                 print(item["image"])
    #         elif item.get("description"):
    #             pass
    #         else:
    #             for key in item.keys():
    #                 for names in item[key]:
    #                     if type(names) is dict:
    #                         if names.get("name"):
    #                             print(names["name"])
    #                             print(names["action"])
    #                             if names.get("image"):
    #                                 print(names["image"])
    #                         elif names.get("action"):
    #                             print(names["action"])
    #                             if names.get("image"):
    #                                 print(names["image"])
    #                         else:
    #                             for keys in names.keys():
    #                                 print(keys) # category
    #                                 for its in names[keys]:
    #                                     if type(its) is dict:
    #                                         if its.get("name"):
    #                                         # if its
    #                                             print(its["name"])
    #                                         if its.get("action"):
    #                                             print(its["action"])
    #                                         if its.get("image"):
    #                                             print(its["image"])                                   
    #                     else:
    #                         # print("category") key
    #                         # print(names)
    #                         print(names)
    #     else:
    #         print("one by one, ;list")
    #         print(item)

import sqlite3


cippe_db = sqlite3.connect("cippe.db")
cursor = cippe_db.cursor()
recipies = cursor.execute("SELECT * FROM recipies")
# print(recipies.fetchall())
for name in recipies:
    print(name[1])

pi = "Pizza"
cippe_db = sqlite3.connect("cippe.db")
cursor = cippe_db.cursor()
recipies = cursor.execute("SELECT food_name FROM recipies WHERE food_name='Pizza'")
# recipies = cursor.execute("SELECT id FROM recipies WHERE recipies.food_name='Pizza'")
# recipies = cursor.execute("SELECT id FROM recipies WHERE recipies.food_name=?",(pi,))
# return jsonify({"status": "success", "data": recipies.fetchone()})
print(recipies.fetchone()[0])

ingredients = cursor.execute("SELECT * FROM ingredients WHERE food_id=4")
for item in ingredients.fetchall():
    print(item)
name = "Ewedu Soup"
cippe_db = sqlite3.connect("cippe.db")
cursor = cippe_db.cursor()
key = cursor.execute("SELECT id FROM recipies WHERE food_name=?",(name,))
key_id = key.fetchone()[0]
print(key_id)
if act == "ingredients":
    step_ingre = cursor.execute("SELECT * FROM ingredients WHERE food_id=?",(key_id,))
elif act == "steps":
    step_ingre = cursor.execute("SELECT * FROM steps WHERE food_id=?",(key_id,))