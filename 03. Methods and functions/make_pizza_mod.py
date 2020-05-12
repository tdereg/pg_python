def make_pizza(size, *toppings):
    """
        Summarize the pizza we are about to make.
    """
    print(f"\nMMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")