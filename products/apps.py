from django.apps import AppConfig
from django.db.utils import OperationalError, ProgrammingError


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'

    def ready(self):
        from products.models import Category, Product

        try:
            # Evita duplicar dados
            if Category.objects.exists():
                return

            # Criar categorias
            cat_elec = Category.objects.create(
                name="Eletrônicos",
                description="Produtos eletrônicos em geral"
            )

            cat_moveis = Category.objects.create(
                name="Móveis",
                description="Itens de mobília"
            )

            cat_vest = Category.objects.create(
                name="Vestuário",
                description="Roupas e acessórios"
            )

            # Criar produtos
            Product.objects.create(
                name="Smartphone X100",
                price=1999.90,
                description="Celular com câmera de 108MP",
                stock=15,
                category=cat_elec
            )

            Product.objects.create(
                name="Sofá 3 lugares",
                price=1599.00,
                description="Sofá confortável em suede",
                stock=4,
                category=cat_moveis
            )

            Product.objects.create(
                name="Camiseta Algodão",
                price=49.90,
                description="Camiseta 100% algodão premium",
                stock=30,
                category=cat_vest
            )

            print(">>> Dados iniciais inseridos com sucesso!")

        except (OperationalError, ProgrammingError):
            # Banco ainda não está pronto (ex: antes das migrações)
            pass
