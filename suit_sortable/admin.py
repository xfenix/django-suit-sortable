from django.contrib import admin


class SortableAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/jquery.sortable.min.js',
              'js/sortable.changelist.js', )


class SortableTabularInline(admin.TabularInline):
    class Media:
        js = ('js/jquery.sortable.min.js',
              'js/sortable.tabular.inline.js', )


class SortableStackedInline(admin.StackedInline):
    class Media:
        js = ('js/jquery.sortable.min.js',
              'js/sortable.stacked.inline.js', )
