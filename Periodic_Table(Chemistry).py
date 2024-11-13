import periodictable 
def get_element_info(symbol):
    if not periodictable.elements.symbol(symbol):
        print('Invalid Symbol')
        return
    element = periodictable.elements.symbol(symbol)
    print(f"Element : {element.name}")
    print(f"Symbol : {element.symbol}")
    print(f"Atomic Number : {element.number}")
    print(f"Atomic Weight : {element.mass}")
    print(f"Density : {element.density}")
    
element_symbol = input("Enter the Element Symbol :")
get_element_info(element_symbol)