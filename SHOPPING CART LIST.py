print('------------SHOPPING CART LIST------------')
foods = []
prices = []
total = 0
while True:
    food = input('Enter a food to buy(enter q for exit): ')
    if food.lower() == 'q':
        break
    else:
        price = float(input(f'Enter the food price {food}(enter q for exit): $'))
        foods.append(food)
        prices.append(price)

for food in foods:
    print(food, end=' ')
    
for price in prices:
    total += price
prints()
print(f'Total price  is {total}:$ ')