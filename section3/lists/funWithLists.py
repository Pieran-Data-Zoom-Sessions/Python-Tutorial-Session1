# Solve the problem with just variables

n_pizza = int(input("Hello sir, how many pizzas do you want?: "))
price_pizza = 2
price_burgers = 3
n_burgers = int(input("Hello sir, how many burgers do you want?: "))

# Get the total

total = n_pizza * price_pizza + price_burgers * n_burgers

print(total)

# Create an empty list

total = []

# Adding things to the list

product_pizza = n_pizza * price_pizza
product_burgers = n_burgers * price_burgers

total.append(product_pizza)
total.append(product_burgers)

# using the sum function
print(sum(total))

taxRates = {'california': 0.075, 'texas': 0.08, 'new york': 0.10, 'nevada': 0.095}
print(list(taxRates.keys()))

userInput = input("What state are you in?: ").lower().replace(" ", '')
if userInput in list(taxRates.keys()):
    newTotal = (1 + taxRates[userInput])*sum(total)
    print(round(newTotal, 2))
else:
    print("This restaurant is not in your area :D ")
