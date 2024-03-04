def calculate_discount(price, discount_percent):
    if discount_percent > 20:
        return price * (1 - discount_percent / 100)
    else:
        return price

original_price = int(input("Enter the original price of the item: "))
discount_percent = int(input("Enter the discount percentage: "))

print("The final price is: ", calculate_discount(original_price, discount_percent))