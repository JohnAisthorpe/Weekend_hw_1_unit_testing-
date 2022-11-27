# WRITE YOUR FUNCTIONS HERE

#1
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

#2
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

#3
def add_or_remove_cash(pet_shop, cash_added):
    pet_shop["admin"]["total_cash"] += cash_added
    return get_total_cash(pet_shop)

#4
def add_remove_cash(pet_shop, cash_removed):
    pet_shop["admin"]["total_cash"] = get_total_cash(pet_shop) - cash_removed
    return pet_shop["admin"]["total_cash"]

#5
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

#6
def increase_pets_sold(pet_shop, pets_added):
    pet_shop["admin"]["pets_sold"] = get_pets_sold(pet_shop) + pets_added
    return pet_shop["admin"]["pets_sold"]

#7
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

#8
def get_pets_by_breed(pet_shop, breed):
    pet = []
    for list in pet_shop["pets"]:
        if list["breed"] == breed:
            pet.append(list)
    return pet

#9
def gets_pets_by_breed(pet_shop, breed):
    pet = []
    for list in pet_shop["pets"]:
        if list["breed"] == breed:
            pet.append(list)
    return pet

#10
def find_pet_by_name(pet_shop, pet_name):
    named_pet = {}
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            named_pet["pet"] = pet
    return named_pet


#11
def find_pet_by_name(pet_shop, name):
    for list in pet_shop["pets"]:
        if list["name"] == name:
            return list
    return None

#12
def remove_pet_by_name(pet_shop, name):
    pet = find_pet_by_name(pet_shop, name)
    pet_shop["pets"].remove(pet)

#13
def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

#14
def get_customer_cash(customers):
    return (customers["cash"])

#15
def remove_customer_cash(customer, amount):
     customer["cash"] -= amount

#16
def get_customer_pet_count(customer):
    pet_count = len(customer["pets"])
    return pet_count

#17
def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)
    
#18
def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    
#19
def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    else:
        return False
    
#20
def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    else:
        return False
    
#21
def sell_pet_to_customer(pet_shop, pet, customer):
    num_of_pets = len([pet])
    add_or_remove_cash(pet_shop, pet["price"])
    add_pet_to_customer(customer, pet["name"])
    remove_pet_by_name(pet_shop, pet["name"])
    increase_pets_sold(pet_shop, num_of_pets)
    remove_customer_cash(customer, pet["price"])
    get_customer_pet_count(customer)
    get_pets_sold(pet_shop)
    get_customer_cash(customer)
    get_total_cash(pet_shop)

#22
def sell_pet_to_customer(pet_shop, pet, customer):
    for pet_profile in pet_shop["pets"]:
        if pet_profile == pet:
            num_of_pets = len([pet])
            add_or_remove_cash(pet_shop, pet["price"])
            add_pet_to_customer(customer, pet["name"])
            remove_pet_by_name(pet_shop, pet["name"])
            increase_pets_sold(pet_shop, num_of_pets)
            remove_customer_cash(customer, pet["price"])
            get_customer_pet_count(customer)
            get_pets_sold(pet_shop)
            get_customer_cash(customer)
            get_total_cash(pet_shop)
        else:
            get_customer_pet_count(customer)
            get_pets_sold(pet_shop)
            get_customer_cash(customer)
            get_total_cash(pet_shop)

#23
def sell_pet_to_customer(pet_shop, pet, customer):
    for pet_profile in pet_shop["pets"]:
        if pet_profile == pet and customer["cash"] >= pet_profile["price"]:
            num_of_pets = len([pet])
            add_or_remove_cash(pet_shop, pet["price"])
            add_pet_to_customer(customer, pet["name"])
            remove_pet_by_name(pet_shop, pet["name"])
            increase_pets_sold(pet_shop, num_of_pets)
            remove_customer_cash(customer, pet["price"])
            get_customer_pet_count(customer)
            get_pets_sold(pet_shop)
            get_customer_cash(customer)
            get_total_cash(pet_shop)
        else:
            get_customer_pet_count(customer)
            get_pets_sold(pet_shop)
            get_customer_cash(customer)
            get_total_cash(pet_shop)
