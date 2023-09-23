import csv
from products.models import Product, Category, Type

Category.objects.all().delete()
Type.objects.all().delete()

with open(r"scripts\data\products_new.csv", 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader, None)
    for id, category, real_name, type, image, name in reader:
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
        product = Product.objects.create(
            id=id,
            name=name,
            real_name=real_name,
            category=current_category,
            type=current_type,
            image=image
        )
        print(f'Product {product} created')
