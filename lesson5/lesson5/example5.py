def print_info(name='unknown objekt', color='white', price=0):
    print('Object:', name, sep="\t")
    print('Color:', color, sep="\t")
    print('Price:', price, sep="\t")
    print()

print_info("pen", "blue", 1)
print_info(name='pen',
           color='blue',
           price=1)
print_info(price=5, name='cup', color='orange')

print_info('pen', 'blue')