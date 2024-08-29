from django.contrib import admin
from posts.models import Post,FavoritePost
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError

class FavoritePostInlineFormset(BaseInlineFormSet):
    def clean(self):
        super().clean()
        uniqie_users = set()
        valid_forms = [x for x in self.cleaned_data if not x['DELETE']]
        for form in valid_forms:
            uniqie_users.add(form['user'])
        if len(uniqie_users) != len(valid_forms):
            raise ValidationError('Нельзя добавить в избранное одному пользователю два раза один и тотже пост!')


class FavoritePostInline(admin.TabularInline):
    model = FavoritePost
    extra = 0
    formset = FavoritePostInlineFormset
    fields = ('user','post','created_at')
    readonly_fields = ['created_at']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','author','__str__', 'created_at', 'updated_at']
    list_filter = ['created_at','updated_at']
    #поиск можно искать или по тексту или по имени автора из другой таблицы.
    search_fields = ['text','author__username']
    inlines = [FavoritePostInline]

@admin.register(FavoritePost)
class FavoritePostAdmin(admin.ModelAdmin):
    list_display =['id', 'user','post', 'created_at']
    list_filter = ['created_at']