import pytest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS

def test_default_product_price():
    """Test default product price being 10."""
    prod = Product('Test Product')
    assert prod.price == 10

def test_default_product_weight():
    """ Test default product weight being 20. """
    prod1 = Product('Test Product 1')
    assert prod1.weight == 20

def test_product_methods():
    """ 
    Test that class Product methods correctly identify
    stealability and explosiveness
    """
    prod2 = Product(
        name = 'Test Product 3',
        price = 50,
        weight = 33,
        flammability = 1.2
        )
    assert prod2.stealability() == 'Very stealable!'
    assert prod2.explode() == '...boom!'

def test_default_num_products():
    """ Test that the default number of products is 30. """
    assert len(generate_products()) == 30

def test_legal_names():
    pass