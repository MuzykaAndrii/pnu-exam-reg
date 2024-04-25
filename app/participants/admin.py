from django.contrib import admin
from django.utils import timezone

from participants.models import Participant


class CandidateForExpiredFilter(admin.SimpleListFilter):
    title = 'Статус екзаменів'
    parameter_name = 'candidate_for_expired'

    def lookups(self, request, model_admin):
        return (
            ('yes', 'Закінчились'),
            ('no', 'Не закінчились'),
        )

    def queryset(self, request, queryset):
        current_datetime = timezone.now()
        if self.value() == 'yes':
            return queryset.filter(candidate_for__exams__time__lte=current_datetime).distinct()
        elif self.value() == 'no':
            return queryset.exclude(candidate_for__exams__time__lte=current_datetime)



@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'candidate_for', 'email', 'phone')
    search_fields = ('firstname', 'lastname', 'surname', 'email')
    list_filter = (CandidateForExpiredFilter, 'candidate_for',)

    def fullname(self, obj):
        return obj.fullname
    
    fullname.short_description = 'ПІБ'