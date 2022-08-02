from django.contrib import admin

from blog.models import Post


@admin.register(Post)  # декоратор, выполняет те же функции, что и admin.site.register
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')  # поля, отображаемые в списке статей
    list_filter = ('status', 'created', 'publish', 'author')  # по значениям каких полей можно фильтровать
    search_fields = ('title', 'body')  # по каким полям вести поиск
    prepopulated_fields = {'slug': ('title', )}  # поле slug генерируется автоматически из поля title
    raw_id_fields = ('author', )  # добавить поле поиска author в редактор
    date_hierarchy = 'publish'  # ссылки под поиском для навигации по датам
    ordering = ('status', 'publish')  # сортировка по умолчанию по полям status and publish
