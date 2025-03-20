

if [ "$translation" = true ]; then
    model_admin=TranslationAdmin
    import="from modeltranslation.admin import TranslationAdmin, TranslationStackedInline"
fi

if [ "$translation" != true ]; then
    model_admin=admin.ModelAdmin
    import=""
fi

create_admin() {
    cat <<EOF
from django.contrib import admin
$import
from $app_name.models import  $app_name_class


@admin.register($app_name_class)
class ${app_name_class}Admin($model_admin):
    pass
EOF
}
