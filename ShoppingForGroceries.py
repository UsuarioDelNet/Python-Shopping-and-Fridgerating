"""
Fun code I wrote for my EE 551 Class
"""
#______________________________________________________________________________________________________________________________________________________
"""
Part 1 (got inspired after going shopping):
"""

class produceAisle:
    """
    This is the base class (superclass) that creates a produce aisle in which vegetables are assigned names and prices!
    This is the first of 3 classes, and it demonstrates encapsulation (it privatizes attributes, meaning it can only change within the class itself)

    Attributes:
        veggie(str): the name of the vegetable
        price(int): the cost of the respective vegetable
        stock(int): the amount of vegetables left in stock (starts at 10) <-- this will be a private attribute

    Methods:
        markdown(discount): veggies are on sale! decrease the price of the object
        markup(surcharge): veggies are more expensive... increase the price of the object
        ringUp(quantity): purchases items (prints the quantity and the cost) and reduces the stock
        inventory(): returns the current number of items in the stock
        restock(): updates the stock back to 10
        priceChecker(cart): calculates the total cost for the items in the cart

    """
    def __init__(self, veggie, price):
        self.veggie = veggie
        self.price = price
        self.__stock = 10 # a private attribute, stock, set to 10, that cannot be changed by calling the class itself

    # markdown & markup technically could be fused into one function to both raise and lower the cost, but I felt like making it into 2
    def markdown(self, discount):
        if discount < 0:
            raise ValueError("You can't just give this away!")
        elif discount > self.price:
            raise ValueError("You can't raise prices with markdown... use markup intead!")
        self.price = discount
    
    def markup(self, surcharge):
        if surcharge < self.price:
            raise ValueError("You can't lower prices with markup... use markdown instead!")
        self.price = surcharge

    def ringUp(self, quantity):
        if quantity <= 0:
            raise ValueError("You must buy at least one veggie")
        elif self.__stock < quantity:
            raise ValueError("Out of stock! Please speak to the nearest team member (use restock())")
        reciept = quantity*self.price
        print(f"{quantity} {self.veggie}(s) comes out to ${reciept:,.2f}. Thank you for shopping with us!")
        self.__stock -= quantity

    def inventory(self):
        #initially forgot i needed a way to get the stock lool
        return self.__stock
    
    def restock(self):
        self.__stock = 10

    def priceChecker(self, cart):
        return round(cart*self.price, 2)
        # this is the basic price checker (rounded to 2 decimal places for cents)

class organicProduce(produceAisle):
    """
    This is the subclass of produce aisle
    as opposed to the produce aisle, the only veggies sold here are pesticide- and GMO-free
    of course, that means that the veggies here are much more expensive :/
    This is the second of 3 classes, and it demonstrates inheritance (uses the methods/attributes of its parent class)

    Attributes (only non-produceAisle Attributes):
        organicMarkup(int): the additional costs of organic produce (FIFTY THREE PERCENT BTW)
            -https://www.foodandwine.com/organic-fruits-vegetables-price-difference-11715998

    Methods (only non-produceAisle Methods):
        markdown(discount): veggies are on sale! decrease the price of the object
        markup(surcharge): veggies are more expensive... increase the price of the object

        #thanks to inheritance, the ringUp/priceChecker/inventory/restock methods can be referred to directly from produceAisle

    """
    def __init__(self, veggie, price, organicMarkup = 1.53): # !!!!!!
        self.organicMarkup = organicMarkup
        # super used for calling produceAisle
        super().__init__(veggie, (price*self.organicMarkup))

    def markdown(self, discount):
        if discount < 0:
            raise ValueError("You can't just give this away!")
        elif discount > self.price:
            raise ValueError("You can't raise prices with markdown... use markup intead!")
        self.price = discount*self.organicMarkup # don't forget to upcharge customers :D
    
    def markup(self, surcharge):
        if surcharge < self.price:
            raise ValueError("You can't lower prices with markup... use markdown instead!")
        self.price = surcharge*self.organicMarkup

class digitalCoupons(produceAisle):
    """
    This is another subclass of produce aisle
    thank GOODNESS for digital coupons when I go shopping ദ്ദി╥ ᴗ ╥)
    This is the third of 3 classes, and it demonstrates polymorphism (depending on the object, the values return differently)

    Attributes (only non-produceAisle Attributes):
        N/A

    Methods (only non-produceAisle Methods):
        ringUp(quantity): purchases items (prints the quantity and the cost) and reduces the stock. make sure to scan your coupons!!
        priceChecker(cart): calculates the total cost for the items in the cart + any deals the store is running
        
    """
    def __init__(self, veggie, price):
        super().__init__(veggie, price)
    
    def ringUp(self, quantity): 
        self.quantity = quantity
        if quantity <= 0:
            raise ValueError("You must buy at least one veggie")
        elif self._produceAisle__stock < quantity:
            raise ValueError("Out of stock! Please speak to the nearest team member (use restock())")
        elif self.veggie == "broccoli":
            print(f"Broccoli is on sale! 15% off!")
            reciept = quantity*self.price*0.85
        elif self.veggie == "corn":
            print(f"BOGO! Buy one ear of corn, get one free!")
            if quantity%2 == 0:
                reciept = quantity*self.price/2
            else:
                reciept = (quantity - 1)*self.price/2 + self.price
        elif self.veggie == "lettuce":
            print(f"For every 3 heads of lettuce you buy, you get 1 free!")
            if quantity%4 == 0:
                reciept = (quantity*self.price)*0.75
            elif quantity > 4:
                excess = 0
                lettuceQuantity = quantity
                while lettuceQuantity%4 != 0:
                    lettuceQuantity -= 1
                    excess += 1
                reciept = (lettuceQuantity*self.price)*0.75 + (excess*self.price)
            else:
                reciept = quantity*self.price
        else:
            reciept = quantity*self.price
        print(f"{quantity} {self.veggie}(s) comes out to ${reciept:,.2f}. Thank you for shopping with us!")
        self._produceAisle__stock -= quantity # because __stock doesn't exist in digitalCoupon, I have to call it w/ _class__attribute
                                              # source consulted: https://www.geeksforgeeks.org/python/underscore-_-python/
    
    def priceChecker(self, cart):
        # literally the same exact logic as ringUp but w/no printed flavor text
        if self.veggie == "broccoli":
            print(f"Broccoli is on sale! 15% off!")
            return round(cart*self.price*0.85, 2)
        elif self.veggie == "corn":
            print(f"BOGO! Buy one ear of corn, get one free!")
            if cart%2 == 0:
                return round(cart*self.price/2, 2)
            else:
                return round((cart - 1)*self.price/2 + self.price, 2)
        elif self.veggie == "lettuce":
            print(f"For every 3 heads of lettuce you buy, you get 1 free!")
            if cart%4 == 0:
                return round((cart*self.price)*0.75, 2)
            elif cart > 4:
                excess = 0
                lettuceCart = cart
                while lettuceCart%4 != 0:
                    lettuceCart -= 1
                    excess += 1
                return round((lettuceCart*self.price)*0.75 + (excess*self.price), 2)
            else:
                return round(cart*self.price, 2)
        else:
            return round(cart*self.price, 2)

#Tests_________________________________________________________________________________________________________________________________________________

# here's some veggies!
# source consulted: https://www.walmart.com/browse/fresh-produce/fresh-vegetables/976759_976793_8910423
carrots = produceAisle("carrot", 0.50)
broccoliCrowns = produceAisle("broccoli", 3.00) 
lettuceHeads = produceAisle("lettuce", 2.50)
earoOCorn = produceAisle("corn", 0.75)
cucumbers = produceAisle("cucumber", 1.00)

# testing produceAisle:
# stock + sale tests 
print(f"There are {carrots.inventory()} carrots in stock")
# now buy 4 carrots ^^
carrots.ringUp(4)
print(f"There are {carrots.inventory()} carrots in stock")
carrots.restock()
print(f"Carrots have restocked! Now there are {carrots.inventory()} carrots in stock\n")

# markup/markdown + price check tests
print("The cucumber salad trend is back, so we're selling them at a premium!") #how unethical
cucumbers.markup(1.50)
print(f"Now, buying 1 cucumber is ${cucumbers.priceChecker(1)}")
print("People started protesting, so now cucumbers are on sale...") #thank goodness!
cucumbers.markdown(0.75)
print(f"Now, buying 1 cucumber is ${cucumbers.priceChecker(1)}\n")

# testing organicProduce
freshCarrots = organicProduce("carrot", 0)
print("Buy some organic carrots instead! They're healthy, and we're setting the price at $0.50! [organic upcharge not included]")
#sure, why not?
freshCarrots.markup(0.50)
print(f"Buying 1 organic carrot is ${freshCarrots.priceChecker(1)}\n") # a surcharge of 27 cents??? that's daylight robbery!

# testing digitalCoupons
# i'm done spending tons of money on veggies! i've come with my coupons!
bogoCorn = digitalCoupons("corn", 0.75)
print(f"Buying 1 ear of corn is ${bogoCorn.priceChecker(1)}") #bogo? what a great deal!
bogoCorn.ringUp(6)
# that was a great deal! i should buy more!
bogoCorn.ringUp(10) # intentionally throws the error :P

#______________________________________________________________________________________________________________________________________________________
"""
Part 2: 
"""
"""

Now that you've bought veggies you need a fridge/freezer to store them in!
"""

class fridgeDrawer():

    """
    This class creates a fridge drawer object (the thing inside the fridge that stores different sets of food/produce/canned goods)
    with it you can store food based on different categories, and regulate the temperature per drawer 
    Source for reference: https://www.bosch-home.com/us/en/c/spotlight/blte7002e95bd180ee1/what-should-a-refrigerator-and-freezer-temperature-be

    Attributes:
        drawer(str): technically the name of the drawer (top shelf/middle shelf/door bins/freezer/meat shelf/dairy drawer/etc)
        temp(int): the temperature of the respective drawer
        fridgeLight(bool): the light inside the fridge. if you open the door and don't close it, the light will stay on and drain battery!!! <-- private attribute
        food(list): what the drawer contains inside, in the form of a list

    Methods:
        open(): opens the fridge door! it turns the fridge light on (fridgeLight = True) and warns if left open too long
        close(): closes the fridge door. it turns the fridge light off (fridgeLight = False) 
        tempDial(newTemp): change the drawer's temperature
        store(grocery): stores a food item in the drawer (you need to open the door first though!)
        remove(ingredient): takes a food item out of the drawer
        status(): check the name of the drawer, its current temperature, and what is stored inside

    """

    __fridgeLight = False   # the fridgeLight is a class attribute that gets shared over all the different fridge drawer objects
                                 # it's also private, because how are you going to turn it on and off without opening the door?
                                 
    def __init__(self, drawer, temp = 37): #apparently the ideal temperature for a fridge according to Bosch
        self.drawer = drawer
        self.temp = temp
        self.food = [] # buy some groceries!!!

    def open(self):
        fridgeDrawer.__fridgeLight = True
        print("The fridge is open... don't forget to close it when you're done!")

    def close(self):
        fridgeDrawer.__fridgeLight = False
        print("The fridge is closed")

    def tempDial(self, newTemp):
        if fridgeDrawer.__fridgeLight == True: #only works if the door has been opened
            self.temp = newTemp
            print(f"The {self.drawer} is now {self.temp} degrees F")
        else:
            print("Open the fridge door! How are you going to turn the dial if you can't see it?")

    def store(self, grocery):
        if fridgeDrawer.__fridgeLight == True:
            self.food.append(grocery)
            print(f"Your {grocery} is stored in the {self.drawer}")
        else:
            print("Open the fridge door!")

    def remove(self, ingredient):
        if fridgeDrawer.__fridgeLight == True:
            if ingredient not in self.food:
                raise ValueError(f"Check again... {ingredient} isn't in the {self.drawer}!")
            self.food.remove(ingredient)
            print(f"You've taken {ingredient} out of the {self.drawer}.")
        else:
            print("Open the fridge door!")

    def status(self):
        if fridgeDrawer.__fridgeLight == True:
            print(f"You've opened the {self.drawer}... \nTemperature: {self.temp}\nCurrent Contents: {self.food}\nThe fridge light is still on! Make sure to close the door when you're done!")
        else:
            print("Unfortunately, your x-ray glasses come next week. Open the fridge door!")

class crisperDrawer(fridgeDrawer):

    """
    This class is a subclass of the fridgeDrawer, creating a crisper drawer 
    the crisper drawer in a fridge is a humidity-controlled drawer specifically used to store fresh produce
    otherwise, it functions the same as a regular drawer
    Sources for reference: https://www.epicurious.com/expert-advice/how-to-use-your-refrigerators-crisper-drawer-article
                           https://www.whirlpool.com/blog/kitchen/crisper-drawer-settings.html

    Attributes (only non-fridgeDrawer Attributes):
        humidity(str): according to epicurious, there are two states of humidity for a crisper drawer to be in, and the humidity str is one of the two:
            -High humidity: good for wilt-prone produce (broccoli/lettuce/sweet potato/cucumber) --> "high"
            -Low humidity: good for rot-prone produce (apple/melon/avocado/fig) --> "low"
        
    Methods (only non-fridgeDrawer Methods): 
        humidityVent(newHumidity): change the crisper drawer's humidity via controlling the airflow w/the vent
        store(grocery): now will warn you if you put in food that is marked as either wilt or rot when the humidity settings are the opposite
        status(): still checks the name of the drawer, its current temperature, and what is stored inside, but now also checks humidity

    """

    def __init__(self, drawer, temp=37, humidity="low"):
        # the vent starts open (low humidity) and acts as a regular drawer
        super().__init__(drawer, temp) #because most of the modes remain the same from fridge to crisper drawer, only one additional attribute is needed
        self.humidity = humidity.lower()

    def humidityVent(self, newHumidity):
        if fridgeDrawer._fridgeDrawer__fridgeLight == True: # to access fridgeLight from fridgeDrawer
            if newHumidity == "low":
                self.humidity = newHumidity
                print(f"The {self.drawer} is now set to {self.humidity} humidity")
            elif newHumidity == "high":
                self.humidity = newHumidity
                print(f"The {self.drawer} is now set to {self.humidity} humidity")
            else:
                print("That's not a humidity level... please either input 'low' or 'high'!")
        else:
            print("Open the fridge door! You can't access the crisper drawer from the outside!")

    def store(self, grocery):
        wiltProduce = ["asparagus", "broccoli", "cauliflower", "citrus", "cucumber", "eggplant", "green bean", "greens", "lettuce", "parsley", "pepper", "raspberry", "squash", "strawberry", "sweet potato"]
        rotProduce = ["apple", "apricot", "avocado", "banana", "cantaloupe", "fig", "honeydew melon", "kiwi", "nectarine", "papaya", "peach", "pear", "plum"] # sourced frmo the epicurious link
        if fridgeDrawer._fridgeDrawer__fridgeLight == True:
            if self.humidity == "low":
                if grocery in wiltProduce:
                    print(f"Your {grocery} is a wilt-prone produce that needs high humidity in the crisper drawer!")
                else:
                    self.food.append(grocery)
                    print(f"Your {grocery} is stored in the {self.drawer}")
            elif self.humidity == "high":
                if grocery in rotProduce:
                    print(f"Your {grocery} is a rot-prone produce that needs low humidity in the crisper drawer!")
                else:
                    self.food.append(grocery)
                    print(f"Your {grocery} is stored in the {self.drawer}")
        else:
            print("Open the fridge door!")

    def status(self):
        if fridgeDrawer._fridgeDrawer__fridgeLight == True:
            print(f"You've opened the {self.drawer}... \nTemperature: {self.temp}\nCurrent Contents: {self.food}\nHumidity Settings: {self.humidity} humidity\nThe fridge light is still on! Make sure to close the door when you're done!")
        else:
            print("Unfortunately, your x-ray glasses come next week. Open the fridge door!")

#Tests_________________________________________________________________________________________________________________________________________________

# setting up the fridge:
# source consulted: https://smallstuffcounts.com/fridge-organization/
topShelf = fridgeDrawer("Top Shelf")
middleShelf = fridgeDrawer("Middle Shelf")
meatShelf = fridgeDrawer("Meat Shelf")
dairyDrawer = fridgeDrawer("Dairy Drawer")
doorRacks = fridgeDrawer("Door Racks")

doorRacks.open() #let's open the fridge!

print("")
# lower the temperature a bit in the meat shelf to keep stuff fresh!
meatShelf.tempDial(32)
# and now add some groceries!

print("")
meatShelf.store("beef short rib")
meatShelf.store("prosciutto")
meatShelf.store("salmon filet")
meatShelf.status()

print("")
#actually, i'll make the salmon for dinner
meatShelf.remove("salmon filet")
meatShelf.status()

print("")
dairyDrawer.close() # all fridge.open() are connected 

# now to set up the crisper drawer:
crisper = crisperDrawer("Crisper Drawer")
topShelf.open()

print("")
crisper.humidityVent("low")
# let's add our groceries!
crisper.store("apple")
crisper.store("fig")
crisper.store("broccoli") #oops
print("")
crisper.status()

print("")
middleShelf.close()