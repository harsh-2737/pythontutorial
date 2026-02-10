from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):   # compact table view
    model = Choice
    extra = 2   # number of empty choice boxes


class QuestionAdmin(admin.ModelAdmin):
    # Field layout in admin form
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]

    # Inline choices inside Question page
    inlines = [ChoiceInline]

    # Change list page (question list)
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)
