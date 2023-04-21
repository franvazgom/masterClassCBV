from django.contrib import admin
from .models import Project, ProjectType

class ProjectTypeAdmin(admin.ModelAdmin):
    list_display = ('project_type', )

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','project_type','created',)

admin.site.register(ProjectType, ProjectTypeAdmin)
admin.site.register(Project, ProjectAdmin)

