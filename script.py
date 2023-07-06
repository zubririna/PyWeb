import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

django.setup()

from store.models import Product, Category

if __name__ == '__main__':
    category = Category.objects.get(name='Vegetables')
    obj = Product(name='Carrots', description='Сладкая морковка', price=120,
                  image='static/products/product-7.jpg', category=category)
    obj.save()

    obj = Product.objects.create(name='Fruit Juice',
                                 description='Мультифрукт',
                                 price=120,
                                 image='static/product/product-8.jpg',
                                 category=Category.objects.get(name='Juice'))

    data = ({'name': 'Onion',
             'price': 120.00,
             'description': "Лук-вырви глаз",
             'image': 'static/products/product-9.jpg',
             'category': 'Vegetables'},
            {'name': 'Apple',
             'price': 120.00,
             'description': "Яблочко наливное",
             'image': 'static/products/product-10.jpg',
             'category': 'Fruits'},
            {'name': 'Garlic',
             'price': 120.00,
             'description': "Чеснок, он и в Африке чеснок",
             'image': 'static/products/product-11.jpg',
             'category': 'Vegetables'},
            )

    categ = {'Fruits': Category.objects.get(name='Fruits'),
             'Vegetables': Category.objects.get(name='Vegetables'),
             }

    objects_to_create = [Product(name=val['name'], description=val['description'],
                                 price=val['price'], image=val['image'],
                                 category=categ[val['category']]) for val in data
                         ]

    Product.objects.bulk_create(objects_to_create)