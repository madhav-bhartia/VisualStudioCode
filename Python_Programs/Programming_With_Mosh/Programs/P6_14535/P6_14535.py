def checkout():
    cart = [10, 20, 30]
    total_cost = 0
    for cost in cart:
        total_cost += cost
    print(f"Total cost: {total_cost}")


checkout()
