from django.db import models
from ckeditor.fields import RichTextField


class SkillLevel(models.IntegerChoices):
    ROBOTIC = 0, "Robótico"
    BASIC = 1, "Básico"
    INTERMEDIATE = 2, "Intermediário"
    ADVANCED = 3, "Avançado"
    EXPERT = 4, "Especialista"

    @property
    def description(self):
        descriptions = {
            self.ROBOTIC: (
                "Executa tarefas estritamente repetitivas, seguindo "
                "instruções diretas e previamente definidas, sem autonomia "
                "para tomada de decisão. Atua sob supervisão constante, não "
                "realizando análises, adaptações ou melhorias nos processos."
            ),
            self.BASIC: (
                "Possui conhecimentos iniciais da atividade ou ferramenta. "
                "Executa tarefas simples com orientação frequente, "
                "compreendendo procedimentos padrão, porém ainda com "
                "limitações para resolver problemas ou atuar de forma "
                "independente."
            ),
            self.INTERMEDIATE: (
                "Executa atividades com autonomia parcial, compreendendo "
                "fluxos e regras do processo. Consegue resolver problemas "
                "comuns, adaptar procedimentos conforme a necessidade e "
                "prestar apoio técnico em demandas rotineiras."
            ),
            self.ADVANCED: (
                "Domina a atividade ou ferramenta, atuando com alta autonomia "
                "e segurança técnica. Analisa cenários, propõe melhorias, "
                "corrige falhas e orienta outros servidores."
            ),
            self.EXPERT: (
                "Possui domínio pleno e aprofundado da área de atuação. Atua "
                "como referência técnica, define padrões, metodologias e "
                "boas práticas, participa de decisões estratégicas e resolve "
                "problemas críticos ou inéditos."
            ),
        }
        return descriptions.get(self, "")


class SkillType(models.TextChoices):
    HARD = "hard", "Hard Skill"
    SOFT = "soft", "Soft Skill"


class Skill(models.Model):
    created_at = models.DateTimeField("Criação", auto_now_add=True)
    active = models.BooleanField("Ativo", default=True,)
    name = models.CharField(max_length=100)
    skill_type = models.CharField(max_length=10, choices=SkillType.choices,)

    class Meta:
        unique_together = ("name", "skill_type")
        verbose_name = "Habilidade"
        verbose_name_plural = "Habilidades"

    def __str__(self):
        return f"{self.name} ({self.get_skill_type_display()})"


class System(models.Model):
    created_at = models.DateTimeField("Criação", auto_now_add=True)
    active = models.BooleanField("Ativo", default=True,)
    name = models.CharField("Nome do Sistema", max_length=150, unique=True,)
    description = models.TextField("Descrição", blank=True,)

    class Meta:
        verbose_name = "Sistema"
        verbose_name_plural = "Sistemas"
        ordering = ("name",)

    def __str__(self):
        return f"{self.name}"


class Function(models.Model):

    class EducationLevel(models.TextChoices):
        FUNDAMENTAL = "FUNDAMENTAL", "Ensino Fundamental"
        MEDIO = "MEDIO", "Ensino Médio"
        TECNICO = "TECNICO", "Ensino Técnico"
        SUPERIOR = "SUPERIOR", "Ensino Superior"

    created_at = models.DateTimeField("Criação", auto_now_add=True)
    active = models.BooleanField("Ativo", default=True,)
    name = models.CharField(max_length=100, verbose_name='Nome do Cargo', unique=True)
    description = RichTextField(max_length=10000, verbose_name='Atribuições Basicas')
    workload = models.PositiveSmallIntegerField("Carga Horária (horas/semana)", help_text="Informe a carga horária semanal",)
    education_level = models.CharField("Nível de Escolaridade", max_length=20, choices=EducationLevel.choices,)
    link = models.URLField("Legislação", blank=True, null=True, help_text="Link para a lei ou documento oficial que regulamenta o cargo",)

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"
        ordering = ["name"]

    def __str__(self):
        return self.name
