class Cart(object):
    cartNo = 1
    inventory = ("bread", "eggs", "milk", "salmon", "wine")

    def __init__(self,cust_name):
        self.cartNo = Cart.cartNo
        Cart.cartNo += 1
        self.cust_name = cust_name
        self.cart = []
    
    def addGroc(self, item):
        if(item.name in Cart.inventory):
            self.cart.append(item)
        else:
            print("Could not add",item.name)
    
    def showCart(self):
        for i in self.cart:
            print(i)
    
    def __str__(self):
        return "Cart #" + str(self.cartNo) + "\ncustomer " + self.cust_name
    

class Grocery():
    def __init__(self,name):
        self.name = name
    
    def __str__(self):
        return self.name

g1 = Grocery("milk")
c1 = Cart("Jean-Louis")
c1.addGroc(g1)
c1.addGroc(Grocery("beer"))
c1.showCart()
