from django.contrib import admin
from polls.models import Poll
from polls.models import Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 5

class PollAdmin(admin.ModelAdmin):
	fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
	inlines = [ChoiceInline]
	list_display = ('question', 'pub_date', 'was_published_recently')
	search_fields = ['question']
	list_filter = ['pub_date', 'question']

admin.site.register(Poll, PollAdmin)