from django.core.management.base import BaseCommand
from curriculum.models import Category, SubCategory


CATEGORIES = {
    "Administração": [
        "Gestão Pública",
        "Processos Administrativos",
        "Compras e Licitações",
        "Planejamento Estratégico",
    ],
    "Saúde": [
        "Enfermagem",
        "Fisioterapia",
        "Saúde Mental",
        "Atenção Básica",
    ],
    "Assistência Social": [
        "CRAS",
        "CREAS",
        "Proteção Social Básica",
        "Proteção Social Especial",
    ],
    "Educação": [
        "Educação Infantil",
        "Ensino Fundamental",
        "Pedagogia",
        "Educação Especial",
    ],
    "Tecnologia": [
        "Programação",
        "Desenvolvimento Web",
        "Redes de Computadores",
        "Segurança da Informação",
        "Banco de Dados",
    ],
    "Meio Ambiente": [
        "Sustentabilidade",
        "Licenciamento Ambiental",
        "Gestão de Resíduos",
    ],
    "Finanças": [
        "Contabilidade",
        "Finanças Públicas",
        "Nota Fiscal e Tributos",
    ],

    # 💬 NOVA CATEGORIA ADICIONADA
    "Comunicação": [
        "Comunicação Institucional",
        "Marketing",
        "Produção de Conteúdo",
        "Design Gráfico",
        "Mídias Sociais",
        "Assessoria de Imprensa",
        "Fotografia e Vídeo",
        "Retórica",
    ],
}


class Command(BaseCommand):
    help = "Cria categorias e subcategorias padrão"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("Iniciando cadastro de categorias..."))

        for category_name, subcategories in CATEGORIES.items():
            category, created = Category.objects.get_or_create(name=category_name)

            if created:
                self.stdout.write(self.style.SUCCESS(f"Categoria criada: {category_name}"))
            else:
                self.stdout.write(f"Categoria já existe: {category_name}")

            for subcat_name in subcategories:
                subcat, sub_created = SubCategory.objects.get_or_create(
                    category=category,
                    name=subcat_name
                )
                if sub_created:
                    self.stdout.write(self.style.SUCCESS(f"  Subcategoria criada: {subcat_name}"))
                else:
                    self.stdout.write(f"  Subcategoria já existe: {subcat_name}")

        self.stdout.write(self.style.SUCCESS("Processo concluído com sucesso!"))
