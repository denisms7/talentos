from django.core.management.base import BaseCommand
from curriculum.models import Skill, SkillType


class Command(BaseCommand):
    help = "Cria skills administrativas padrões no sistema."

    def handle(self, *args, **options):


        skills = [
            # Pacote Microsoft
            ("Microsoft Excel", SkillType.HARD),
            ("Microsoft Word", SkillType.HARD),
            ("Microsoft PowerPoint", SkillType.HARD),
            ("Microsoft Outlook", SkillType.HARD),
            ("Microsoft Access", SkillType.HARD),

            # Design e engenharia
            ("AutoCAD", SkillType.HARD),
            ("Revit", SkillType.HARD),
            ("Photoshop", SkillType.HARD),
            ("Illustrator", SkillType.HARD),
            ("CorelDRAW", SkillType.HARD),
            ("Design Gráfico", SkillType.HARD),
            ("Fotografia e Vídeo", SkillType.HARD),

            # Tecnologia da informação
            ("Programação", SkillType.HARD),
            ("Redes de Computadores", SkillType.HARD),
            ("Segurança da Informação", SkillType.HARD),
            ("Banco de Dados", SkillType.HARD),
            ("Análise de Dados", SkillType.HARD),
            ("Big Data", SkillType.HARD),

            # Administração pública e gestão
            ("Gestão Administrativa", SkillType.HARD),
            ("Processos Administrativos", SkillType.HARD),
            ("Compras e Licitações", SkillType.HARD),
            ("Planejamento Estratégico", SkillType.HARD),
            ("Finanças Públicas", SkillType.HARD),
            ("Nota Fiscal e Tributos", SkillType.HARD),
            ("Organização de Documentos", SkillType.SOFT),
            ("Redação Oficial", SkillType.HARD),
            ("Elaboração de Relatórios", SkillType.HARD),
            ("Arquivologia", SkillType.HARD),

            # Sustentabilidade
            ("Sustentabilidade", SkillType.HARD),
            ("Gestão de Resíduos", SkillType.HARD),
            ("Gestão Hídrica", SkillType.HARD),

            # Comunicação e marketing institucional
            ("Comunicação Institucional", SkillType.HARD),
            ("Marketing", SkillType.HARD),
            ("Produção de Conteúdo", SkillType.HARD),
            ("Mídias Sociais", SkillType.HARD),
            ("Assessoria de Imprensa", SkillType.HARD),
            ("Retórica", SkillType.SOFT),

            # Competências comportamentais
            ("Conduta Profissional", SkillType.SOFT),
            ("Flexibilidade e Adaptação", SkillType.SOFT),
            ("Liderança", SkillType.SOFT),
            ("Resiliência", SkillType.SOFT),
            ("Comunicação", SkillType.SOFT),
            ("Gestão de Pessoas", SkillType.SOFT),
            ("Gestão do Tempo", SkillType.SOFT),
            ("Atendimento ao Público", SkillType.SOFT),
        ]

        criadas = 0

        for name, skill_type in skills:
            _, created = Skill.objects.get_or_create(
                name=name,
                defaults={"skill_type": skill_type},
            )

            if created:
                criadas += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"{criadas} skills administrativas criadas com sucesso."
            )
        )