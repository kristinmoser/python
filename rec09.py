#!C:\python27\python.exe
'''
Programmer: Kristin Moser
username: km3322
file_name= rec09.py

this program allows a person to create a list of items they will not buy from the grocery store
and then allows the rest of the family to create a list of items they want fromt the groccery store.

all items from both lists are checked to make sure they are at the gorcery store.
the items the family enters for the grocery list are checked to make sure they are not on the won't buy list.

'''
GROCERY_STORE = ["milk", "chocolate covered cherries", "apple", "rn on the cob",
                 "kampyo sushi", "asparagus", "avacado", "alfalfa", "acorn squash",
                 "almond package", "arugala bunch", "artichoke", "applesauce",
                 "wasabi", "udon noodles", "tunafish can", "apple juice", "avocado sushi",
                 "bruscetta", "bagel", "barley", "bisque", "bluefish", "bread",
                 "broccoli", "buritto", "babaganoosh", "cabbage", "chocolate cake",
                 "red velvet cake", "strawberry short cake", "carrots", "celery",
                 "cheese", "catfish", "chowder", "clams", "coffee", "corn", "crab",
                 "curry", "cereal", "chimichanga", "dumpling", "donut", "egg", "enchilada",
                 "eggroll", "english muffin", "edimame", "eel sushi", "o toro sashimi", "fajita",
                 "falafel", "fondu", "french toast", "french dip", "garlic", "ginger", "gnocchi",
                 "granola", "grape", "green bean", "guacamole", "gumbo", "grits", "graham crackers",
                 "halibut", "honey", "huenos rancheros", "hash browns", "hummus", "chocolate ice cream",
                 "strawberry ice cream", "cherry garcia ice cream", "puri", "veggie kurma", "jambalaya",
                 "kale", "ketchup", "kiwi", "kidney beans pckg", "great northern beans pckg", "lobster",
                 "linguine", "lasagna", "pepperoni pizza", "mushroom pizza", "pancakes", "quesadilla",
                 "quiche", "spinach", "spaghetti", "tater tots", "toast", "waffles", "walnuts", "peanuts",
                 "hazelnuts", "cranberries", "yogurt", "ziti", "zucchini", "canteloupe", "figs", "salt",
                 "pepper", "nutmeg", "yucca", "shichimi"]

QUIT_CHOICES = [ "done" , "DONE" , "exit" , "EXIT" , "quit" , "QUIT" , "Q"]

def makeIWontBuyList():
    '''allows the designated shopper to create a list of items they will not buy
    and makes sure the food entered is in the grocery store'''
    wontBuyList = []
    print ("Hey lucky designated shopper! It's time to make your I Won't Buy List!When you're done, enter 'quit'")
    bad_food = raw_input ("Enter a food you won't buy:")
    while bad_food not in QUIT_CHOICES:
        bad_food.lower()
        if bad_food in GROCERY_STORE:
            wontBuyList.append(bad_food)
        else:
            print ("Sorry. The grocery store doesn't sell that.")
        bad_food = raw_input ("Enter a food you won't buy:")
    return wontBuyList

def makeGroceryList(wontBuyList):
    '''allows the rest of the family to create a list of items they want the designated
    shopper to get from the grocery store. also makes sure that food item is actually
    at the grocery store and not in the won't buy list '''
    grocery_list = []
    print ("Now, let's make the shopping list! When you're done, enter 'quit'!")
    food = raw_input (" What do you want from the grocery store?")
    while food not in QUIT_CHOICES:
        food.lower()
        if food in GROCERY_STORE and food not in wontBuyList:
            grocery_list.append(food)
        else:    
            print ("Sorry. The grocery store doesn't sell that or your designated shopper does not want to buy that.")
        food = raw_input (" What do you want from the grocery store?")
    return grocery_list

def displayGroceryList(grocery_list):
    '''displays the grocery list in one column'''
    print ("-- FAMILY SHOPPING  LIST --")
    for n in grocery_list:
        print(n)

def main():
    wontBuyList = makeIWontBuyList()
    grocery_list = makeGroceryList(wontBuyList)
    displayGroceryList(grocery_list)

main()


 



    




    
