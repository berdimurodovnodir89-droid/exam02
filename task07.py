def calculate_cart(cart: dict) -> int:
    result = 0
    for i in cart.values():
        result += i['price'] * i['quantity']
    return result

        
        


    return result

cart = {
  'non': {'price': 3000, 'quantity': 2},
  'sut': {'price': 8000, 'quantity': 1},
  'olma': {'price': 5000, 'quantity': 5}
}

print(calculate_cart(cart))