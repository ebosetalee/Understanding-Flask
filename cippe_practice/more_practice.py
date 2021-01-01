from flask import Flask, jsonify, send_file, request, flash, redirect, url_for
import json
import sqlite3
# from 


app = Flask(__name__)
app.secret_key = "star"

@app.route("/")
def home():
    return "Hello World"
    

@app.route("/recipies", methods=["GET", "POST"])
def recipies():
    cippie_db = sqlite3.connect("cippedb.db")
    cursor = cippie_db.cursor()
    if request.method == "POST":
        data = request.get_json()
        try:
            cippie_db.execute("INSERT INTO recipies VALUES(NULL, '{0}', '{1}', '{2}', '{3}')".format(
            data["name"], data["description"], data["top image"], data["bottom image"]))
            cippie_db.commit()
        except:
            return jsonify({"status": "error", "error": "Important keys(in this order): name, description, top image, bottom image"})
        return jsonify({"status": "success", "data": data}), 201
    recipe = cursor.execute("SELECT food_name FROM recipies")
    return jsonify({"status": "success", "data": recipe.fetchall()})


# if __name__ == "__main__":
#     app.run()


# from sqlalchemy import create_engine
# from sqlalchemy.orm import Session
# from sqlalchemy.ext.automap import automap_base


# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cippedb.db"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# db = SQLAlchemy(app)

# engine = create_engine("sqlite:///cippedb.db")
# # Session = session(engine)
# session = Session(engine)

# Base = automap_base()
# Base.prepare(engine, reflect=True)
# Recipie = Base.classes.recipies
# ingredient = Base.classes.ingredients

# if Recipie.get(Recipie.food_name == "Shinkafa2"):
#     print("true")

# recipe = db.Table("recipies", db.metadata, autoload=True, autoload_with=engine)
# recipe = session.query(Recipie).all()
# print(recipe)
# all_recipe = db.session.query("food_name from {}".format(recipe)).all()
# all_recipe = session.query(Recipie.food_name).all()
# print(all_recipe)


# {
#   "name": "Shinkafa 2",
#   "description": "Shinkafa (Rice Fufu)2 is a northern Nigerian fufu recipe that is prepared with the soft rice variety. It is usually served with Northern Nigerian soups: Miyan Kuka, Miyan Taushe etc. It goes well with other Nigerian Soups. The rice used for Tuwo Shinkafa should be the a soft rice variety that becomes sticky when cooked. This is so that the grains can be easily mashed to make a mass of fufu (tuwo).",
#   "top image": "https://guardian.ng/wp-content/uploads/2019/07/Tuwo-Shinkafa-PHOTO-Instagram-1728x1152.jpeg",
#   "bottom image": "https://scontent.flos7-1.fna.fbcdn.net/v/t1.0-9/12647352_1049780168376222_4455610281711881610_n.jpg?_nc_cat=104&ccb=2&_nc_sid=9267fe&_nc_ohc=K5Znhv7PHwAAX-JMoeL&_nc_ht=scontent.flos7-1.fna&oh=d743d21bd9f5e3b98d1b3ad3fcf2ebae&oe=5FC3E439"
# }

{
  "steps": [
    {
      "preparations": [
        "Rinse the rice in cold water and put in a sizeable pot."
      ]
    },
    "Pour just enough water to cover the rice and start cooking at medium heat.",
    "When the first dose of water dries up, check the rice by mashing it between your fingers. If the rice grains have even a tiny resistance when you press them, then it needs to be cooked some more.",
    "Reduce the heat to low, add a little bit more water and continue cooking till the water dries.",
    "Repeat the process till the rice is so soft that it melts when you press on it.",
    "Once you're happy, mash the rice with a wooden spatula by moving the rice in small quantities from the far end of the pot to your side of the pot.",
    "Fold the mound of tuwo and repeat till all the rice grains have turned into a mass of tuwo.",
    "Cover and leave it to steam for about 2 minutes.",
    "Mix thoroughly and dish serving quantities onto a thin plastic film and wrap them up. This wrapping prevents the tuwo from drying up"
  ]
}

{
    "name": "Rice",
    "quantity": "As required",
    "type": "Soft",
    "requirement" : "Important"
},
{
    "name": "Water",
    "quantity": "As required",
    "type" : "Clean",
    "requirement" : "Important"
},
{
    "name" : "Seasoning",
    "quantity" : "As required",
    "requirement" : "Optional"
},
{
    "name" : "Spice",
    "quantity" : "As required",
    "type" : "Maggi or Knorr"
    "requirement" : "Optional"
}

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
# "pancakes_and_scrambled_eggs/scrambled_eggs"


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

# import sqlite3


# cippe_db = sqlite3.connect("cippe.db")
# cursor = cippe_db.cursor()
# recipies = cursor.execute("SELECT * FROM recipies")
# # print(recipies.fetchall())
# for name in recipies:
#     print(name[1])

# pi = "Pizza"
# cippe_db = sqlite3.connect("cippe.db")
# cursor = cippe_db.cursor()
# recipies = cursor.execute("SELECT food_name FROM recipies WHERE food_name='Pizza'")
# # recipies = cursor.execute("SELECT id FROM recipies WHERE recipies.food_name='Pizza'")
# # recipies = cursor.execute("SELECT id FROM recipies WHERE recipies.food_name=?",(pi,))
# # return jsonify({"status": "success", "data": recipies.fetchone()})
# print(recipies.fetchone()[0])

# ingredients = cursor.execute("SELECT * FROM ingredients WHERE food_id=4")
# for item in ingredients.fetchall():
#     print(item)
# name = "Ewedu Soup"
# cippe_db = sqlite3.connect("cippe.db")
# cursor = cippe_db.cursor()
# key = cursor.execute("SELECT id FROM recipies WHERE food_name=?",(name,))
# key_id = key.fetchone()[0]
# print(key_id)
# if act == "ingredients":
#     step_ingre = cursor.execute("SELECT * FROM ingredients WHERE food_id=?",(key_id,))
# elif act == "steps":
#     step_ingre = cursor.execute("SELECT * FROM steps WHERE food_id=?",(key_id,))
# -H 'Content-Type: application/json'curl -X POST -H 'Content-Type: application/json' http://127.0.0.1:5000/recipies "{"name" : "Happy"}"
