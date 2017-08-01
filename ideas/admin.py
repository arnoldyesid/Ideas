from django.contrib import admin

# Register your models here.
from ideas.models import Ideas


class IdeaAdmin(admin.ModelAdmin):
    class Meta:
        model = Ideas

admin.site.register(Ideas, IdeaAdmin)
