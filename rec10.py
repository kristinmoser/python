#!C:\python27\python.exe
'''
Programmer: Kristin Moser
username: km3322
file_name= rec10.py

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


PRINT_CHOICE = "1"
REMOVE_CHOICE = "2"
ADD_CHOICE = "3"
ADD_SHOP_CHOICE = "4"
QUIT_CHOICE = "5"
QUIT_LETTER_CHOICE = "Q"
QUIT_UP_CHOICE = "QUIT"
QUIT_CHOICES = [ "quit" ,"QUIT" , "q"]

VALID_CHOICES = [ \
    QUIT_CHOICE, \
    QUIT_UP_CHOICE, \
    QUIT_LETTER_CHOICE, \
    PRINT_CHOICE, \
    REMOVE_CHOICE, \
    ADD_CHOICE, \
    ADD_SHOP_CHOICE, \
    ]    

def getMenuChoice():
    displayMenu()
    choice = raw_input ("Enter your choice:").upper()
    return choice

def displayMenu():
    print ("       MENU")
    print (PRINT_CHOICE + '.Print grocery store contents')
    print (REMOVE_CHOICE + '.Remove an item from my won\'t buy list' )
    print (ADD_CHOICE + '.Add an item to my won\'t buy list' )
    print (ADD_SHOP_CHOICE + '.Add to the shopping list')
    print (QUIT_CHOICE + '.Quit')
    
def handle_menu_choice(nameDict):
    name = raw_input ("What is your name?")
    while True:
        choice = getMenuChoice()
        if choice == PRINT_CHOICE:
            print (GROCERY_STORE)
        elif choice == REMOVE_CHOICE:
            remove_this_food = raw_input ("What food would you like to remove?")
            nameDict[name].remove(remove_this_food)
            print nameDict[name]
        elif choice == ADD_CHOICE:
            food = raw_input ("What are you adding to your won't buy list?")
            nameDict[name].append(food)
            print nameDict[name]
        elif choice == ADD_SHOP_CHOICE:
            makeGroceryList(nameDict)
        else:
            exit()
            
def makeIWontBuyList(name):
    '''allows the designated shopper to create a list of items they will not buy
    and makes sure the food entered is in the grocery store'''
    wontBuyList = []
    print ("Hey %s. It's time to make your I Won't Buy List!When you're done, enter 'quit'" % (name))
    bad_food = raw_input ("Enter a food you won't buy:")
    while bad_food not in QUIT_CHOICES:
        bad_food.lower()
        if bad_food in GROCERY_STORE and bad_food not in wontBuyList:
            wontBuyList.append(bad_food)
        else:
            print ("That item is not correct! Try again.")
        bad_food = raw_input ("Enter a food you won't buy:")  
    return wontBuyList

def createDict():
    num_fam_members = int(raw_input ("How many members are in your family?"))
    nameDict = {}
    for i in range (num_fam_members):
        name = raw_input ("What is your name?")
        wontBuyList = makeIWontBuyList(name)
        nameDict [ name ] = wontBuyList
    print ("-----all the lists have been created-----")
    return nameDict, name

def displayDict(nameDict):
    print nameDict

def makeGroceryList(nameDict):
    '''allows the rest of the family to create a list of items they want the designated
    shopper to get from the grocery store. also makes sure that food item is actually
    at the grocery store and not in the won't buy list '''
    grocery_list = []
    name = raw_input ("Who's the lucky designated shopper?")
    print ("Now, let's make the shopping list! When you're done, enter 'quit'!")
    food = raw_input (" What do you want from the grocery store?")
    while food not in QUIT_CHOICES:
        food.lower()
        if food in GROCERY_STORE and food not in nameDict [name] :
            grocery_list.append(food)
        else:    
            print ("That item is not correct! Try again")
        food = raw_input (" What do you want from the grocery store?")
    print grocery_list
    return grocery_list

def displayGroceryList(grocery_list):
    '''displays the grocery list in one column'''
    print ("-- FAMILY SHOPPING  LIST --")
    for n in grocery_list:
        print(n)

def main():
    nameDict, name = createDict()
    displayDict(nameDict)
    handle_menu_choice(nameDict)
    
main()


 



    




    

