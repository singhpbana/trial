from polls.models import Poll, Choice
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    
class PollAdmin(admin.ModelAdmin):
    #fieldsets = [
    #        (None,               {'fields':['questions']}),
    #        ('Date information', {'fields':['pub_date']}),    
    #]
    inlines = [ChoiceInline]
     
    list_display = ('questions','pub_date','was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['questions']
    date_hierarchy = 'pub_date'
    
admin.site.register(Poll, PollAdmin)
# admin.site.register(Choice)