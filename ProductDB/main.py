from connection import session
from models import Product


products = session.query(Product).all()
for product in products:
    print(product.id, product.name, product.price, product.in_stock)

product = session.query(Product).filter_by(name="Kiwi").first()
if product:
    product.price = 1.9
    session.commit()

product_to_delete = session.query(Product).filter_by(name="Orange").first()
if product_to_delete:
    session.delete(product_to_delete)
    session.commit()