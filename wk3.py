def calculate_discount(price, discount_percentage):
    final_price = price - price * discount_percentage / 100
    if discount_percentage >= 20:
        return final_price
    else:
        return price

def main():
    price, discount_percentage = map(float, input('Enter price and discount percentage separated by a space: ').split())
    
    final_price = calculate_discount(price, discount_percentage)
    
    print("Final price after discount:", final_price)

if __name__ == "__main__":
    main()