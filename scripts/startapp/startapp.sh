#!/bin/bash

source ./scripts/startapp/_optargs.sh
source ./scripts/_utils.sh

source ./scripts/startapp/admin/_create_admin.sh
source ./scripts/startapp/admin/_admin_init.sh

source ./scripts/startapp/models/_create_model.sh
source ./scripts/startapp/models/_model_init.sh

source ./scripts/startapp/serializers/_create_serializer.sh
source ./scripts/startapp/serializers/_serializer_init.sh

source ./scripts/startapp/urls/_create_urls.sh

source ./scripts/startapp/views/_create_view.sh
source ./scripts/startapp/views/_view_init.sh

source ./scripts/startapp/translation/_create_translation.sh
source ./scripts/startapp/translation/_translation_init.sh

export app_name=$1
export app_name_class=$(classify "$app_name")

python manage.py startapp $1
cd "$1" || exit

rm admin.py models.py tests.py views.py

mkdir admin
admin_init >admin/__init__.py
create_admin >admin/"$app_name"_admin.py

mkdir models
model_init >models/__init__.py
create_model >models/"$app_name"_models.py

mkdir urls
touch urls/__init__.py
create_urls >urls/"$app_name"_urls.py

mkdir serializers
serializer_init >serializers/__init__.py
create_serializer >serializers/"$app_name"_serializers.py

mkdir views
view_init >views/__init__.py
create_view >views/"$app_name"_views.py

if [ "$translation" ]; then
  mkdir translation
  translation_init >translation/__init__.py
  create_translation >translation/"$app_name"_translations.py

fi

mkdir services
touch services/__init__.py
touch services/"$app_name"_services.py

