from django.contrib import admin
from django.utils import timezone

from main.models import Degree, StudyingArea, UniversityBuilding, Exam


@admin.register(Degree)
class DegreeAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight')
    search_fields = ('name',)


@admin.register(StudyingArea)
class StudyingAreaAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'degree')
    list_display_links = ('code', 'name', )
    search_fields = ('code', 'name')
    list_filter = ('degree',)


@admin.register(UniversityBuilding)
class UniversityBuildingAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name', 'address')


class IsExpiredFilter(admin.SimpleListFilter):
    title = 'Чи відбувся'
    parameter_name = 'is_expired'

    def lookups(self, request, model_admin):
        return (
            ('expired', 'Відбувся'),
            ('not_expired', 'Не відбувся'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'expired':
            return queryset.filter(time__lt=timezone.now())
        elif self.value() == 'not_expired':
            return queryset.filter(time__gt=timezone.now())


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('subject', 'target', 'type', 'audience', 'time', 'is_expired')
    list_display_links = ('subject', 'target',)
    list_filter = (IsExpiredFilter, 'building', 'target')
    search_fields = ('subject', 'audience')
    readonly_fields = ('is_expired',)
    date_hierarchy = "time"

    def is_expired(self, obj):
        return obj.is_expired
    
    is_expired.boolean = True
    is_expired.short_description = 'Чи відбувся'