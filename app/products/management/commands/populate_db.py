# products/management/commands/populate_db.py
from django.core.management.base import BaseCommand
from faker import Faker
from products.models import Category, Product
import random

fake = Faker()

class Command(BaseCommand):
    help = 'Заполнение базы данных случайными данными'

    def handle(self, *args, **kwargs):
        # Создание случайных категорий
        categories = ['Electronics', 'Clothing', 'Toys', 'Books', 'Groceries']
        for category_name in categories:
            category, created = Category.objects.get_or_create(name=category_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Категория "{category_name}" была создана'))

        # Создание случайных товаров
        for _ in range(20):  # Создать 20 случайных товаров
            category = random.choice(Category.objects.all())
            product_name = fake.word().capitalize()
            price = random.randint(5, 200)
            stock = random.randint(10, 200)
            Product.objects.create(
                name=product_name,
                category=category,
                price=price,
                stock=stock,
                photo=fake.image_url(),  # Если модель Product имеет поле image
            )
            self.stdout.write(self.style.SUCCESS(f'Товар "{product_name}" был создан'))
