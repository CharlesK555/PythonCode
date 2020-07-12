import vehicles

def main():
    
    #create an object of the Automobiles class
    current_auto = vehicles.Automobile('Toyota', '4Runner', 5500.00)
    
    #display the data
    print('\n')
    print('Make:', current_auto.get_make())
    print('Model:', current_auto.get_model())
    print('Price:', current_auto.get_price())
    print('\n')
    
    #prompt user to enter a different make
    new_make = input("Please enter a different make:  ")

    #if something was entered, then call the mutator method to update it
    if len(new_make) > 0:
        current_auto.set_make(new_make)
 
    #display the data
    print('\n')
    print('Make:', current_auto.get_make())
    print('Model:', current_auto.get_model())
    print('Price:', current_auto.get_price())
    print('\n')

    #prompt user to enter a different model
    new_model = input("Please enter a different model:  ")
    
    #if something was entered, then call the mutator method to update it
    if len(new_model) > 0:
        current_auto.set_model(new_model)
 
    print('\n')
    print('Make:', current_auto.get_make())
    print('Model:', current_auto.get_model())
    print('Price:', current_auto.get_price())
    print('\n')

    #prompt user to enter a different price
    new_price = float(input("Please enter a different price (numeric):  "))
    
    #if something was entered, then call the mutator method to update it
    current_auto.set_price(new_price)   
 
    print('\n')
    print('Make:', current_auto.get_make())
    print('Model:', current_auto.get_model())
    print('Price:', current_auto.get_price())
    print('\n')

    #call our handy function to get a human readable representation of the data
    #print(current_auto.get_class_data())
    
#end main()

#Call main
main()


    