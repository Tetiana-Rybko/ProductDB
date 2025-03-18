from connection import session
from models import Product,Category


def add_sample_data():
    category_fruits = Category(name="Fruits", description="All types of fruits")
    category_légumes = Category(name="Légumes", description="Fresh Légumes")

    product_pomme = Product(name="Pomme", price=1.2, in_stock=True, category=category_fruits)
    product_banana = Product(name="Banana", price=0.8, in_stock=True, category=category_fruits)
    product_kiwi = Product(name="Kiwi", price=1.5, in_stock=True, category=category_fruits)
    product_carrot = Product(name="Carrot", price=0.6, in_stock=True, category=category_légumes)
    product_potato = Product(name="Potato", price=0.4, in_stock=True, category=category_légumes)

    session.add(category_fruits)
    session.add(category_légumes)
    session.add(product_pomme)
    session.add(product_banana)
    session.add(product_kiwi)
    session.add(product_carrot)
    session.add(product_potato)

    session.commit()

if __name__ == "__main__":
    add_sample_data()
    print("Exemples de données ajoutées à la base de données.")