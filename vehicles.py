#The Automobile class holds general data about an 
#auto in inventory at a dealership

class Automobile:
    
    #define the initialization method
    def __init__(self, make, model, price):
        self.__make = make
        self.__model = model
        self.__price = price
        
    #define the mutator methods for the data attributes 
    #(these are called setters)
    
    def set_make(self, make):
        self.__make = make
        
    def set_model(self, model):
        self.__model = model
        
    def set_price(self, price):
        self.__price = price

    #define the accessor methods for the data attributes 
    #(these are called getters)
    
    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_price(self):
        return self.__price    
    
    #define an accessor to return a string of the classes data
    def get_class_data(self):
        return "An instance of class Automobile with state: \n Make = %s \n Model = %s \n Price = %f \n" % (self.__make, self.__model, self.__price)    
    
#end class Automobile        

#class Truck(Automobile):
    
    #TODO
    #Page 557
    #add init function
    #add attributes(variables) drive_type and bed_length
    #add mutator and accessor methods for new attributes
    #add get_class_data accessor    
    
#end class Truck()
    