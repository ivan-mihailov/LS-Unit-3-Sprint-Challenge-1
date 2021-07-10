from math import prod
import random
from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num_products=30):
    """ 
    Function to generate a given number of products (default 30), \
    randomly, and return them as a list.
    """
    products = []
    
    for i in range(0, num_products):
        prod = Product(
            name=f'{random.sample(ADJECTIVES, 1)} {random.sample(NOUNS, 1)}',
            identifier=random.randint(1000000, 9999999),
            price=random.randint(5, 100),
            weight=random.randint(5, 100),
            flammability=random.uniform(0.0, 2.5)
            )
        products.append([prod.name, prod.price, prod.weight, \
            prod.flammability])
    return products

def inventory_report(products):
    s = set()
    p = 0
    w = 0
    f = 0
    for j in range(0, len(products)):
        s.add(products[j][0])
        p += products[j][1]
        w += products[j][2]
        f += products[j][3]
    
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f'Unique product names: {len(s)}')
    print(f'Average price: {p / len(products)}')
    print(f'Average weight: {w / len(products)}')
    print(f'Average flammability: {f / len(products)}')

if __name__ == '__main__':
    inventory_report(generate_products())