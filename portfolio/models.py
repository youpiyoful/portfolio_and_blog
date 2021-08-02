from django.db import models


class Skills(models.Model):
    """all my developper skills"""

    name = models.CharField(max_length=150, null=False, blank=False)
    level_experience = models.CharField(max_length=150, null=True, blank=True)
    year_of_experience = models.DateField()

    def __str__(self) -> str:
        return self.name


class Projects(models.Model):
    """All my developper projects"""

    title = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    technology = models.CharField(max_length=300, null=False, blank=False)
    image = models.ImageField(upload_to="projects")

    def __str__(self) -> str:
        return self.title
