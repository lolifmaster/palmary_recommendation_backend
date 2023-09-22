import csv
from products.models import Product, Category, Type

with open(r"C:\Users\chare\PycharmProjects\palmary_recommendation\static\products.csv", 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader, None)
    for _, category, real_name, name, type, image in reader:
        current_category, _ = Category.objects.get_or_create(
            name=category,
            defaults={
                'name': category
            }
        )
        current_type, _ = Type.objects.get_or_create(
            name=type,
            defaults={
                'name': type
            }
        )
        product= Product.objects.create(
            name=name,
            category=current_category,
            type=current_type,
            image=image
        )
        print(f'Product {product} created')
