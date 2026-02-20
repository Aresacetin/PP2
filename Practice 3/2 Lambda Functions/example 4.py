# sorted function is used to sort lists and tuples
# it can take function into keyword argument key to modify sorting

shop = {# key is name value is price in Dcoins
    "Fine black tea": 1500,
    "Fine green tea": 1500,
    "Teapot": 3990,
    "Puer tea": 150,
    "Basilur Tea": 9990,
    "Cup": 800,
    "Yorkshire Tea": 9990
}

shop_items = tuple(shop.items())

# Sorts items at the top items with high price, if prices of two items are same then sorts it alphabetically
shop_items = tuple(sorted(shop_items, key=lambda x: (-x[1], x[0])))

print(*[f"{k}: {v}" for k, v in shop_items], sep="\n")

