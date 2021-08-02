from django.contrib import admin

from portfolio.models import Projects, Skills


class SkillsAdmin(admin.ModelAdmin):
    pass


class ProjectsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Skills, SkillsAdmin)
admin.site.register(Projects, ProjectsAdmin)
