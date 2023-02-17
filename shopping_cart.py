# SHOPPING CART

# cart lists price
cart = [15, 42, 120, 9, 5, 380]

# get the discount amount
discount = int(input())

# set a variable total
total = 0

# for each price in cart
for price in cart:
    # add it to total per iteration
    total += price

# after the loop or once completed adding the amount of cart
# do the calculation
print(total - (total * discount / 100))

