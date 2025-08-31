## Previous steps:
# a.- Rebuild all the Docker Containers. (docker-compose down --remove-orphans)
# b.- Create containers
     docker-compose up --build
     the aplication will be accesible at http://localhost:8080/
# c.- Import zipcodes and card types
    docker-compose exec piano-web //venv/bin/python manage.py import_zipcodes US USMIL CA
    docker-compose exec piano-web //venv/bin/python manage.py loaddata payment_type carrier
## Para distroless:
    docker compose exec piano-web //venv/bin/python manage.py payment_type
    docker compose exec piano-web //venv/bin/python manage.py import_zipcodes US USMIL CA
    docker compose exec piano-web //venv/bin/python manage.py migrate
# d.- Conectar a la base de datos desde docker:
    docker-compose exec piano-postgres psql -U jazz piano ó
    docker-compose exec piano-web python manage.py dbshell
# e.- Facility Tenant and FacilityFull should be both active and allow Allocation and generate PCTL

# f.- Business Type should maintain_inventory

# 1.- activate virtual env
     source venv/Scripts/activate
# 2.- install requirements.txt
    pip install -r requirements.txt
# 3.- install playwright browsers:
    playwright install

# 4.- Run tests:
    pytest -v -k 'initial'

# 5.- To run and view failed steps:
    pytest --gherkin-terminal-reporter -vv -k 'orders'

# 6.- Run the test with debugger:
    PWDEBUG=1 pytest -v -k 'initial'

## Special notes.
If the inventory is not refreshed, you must run the task, with the total records in 
from product.tasks import consume_inventory_summary_queue
for i in range(120):
    consume_inventory_summary_queue(57)

# Add - 
~~~
    "allocation,batches,cache,default,download,integration,inventory,invata,order,pickgen,system,upload,inventory-queue" 
~~~
to the docker-compose.yaml in piano


# Run pytest with more information:
~~~
pytest -v --maxfail=1 --disable-warnings
~~~

## Para eliminar la base de datos:
1. Reinicializar PostgreSQL dentro del contenedor
Si no quieres eliminar el volumen pero deseas limpiar los datos directamente en PostgreSQL:

Acceder al contenedor de PostgreSQL
Primero, accede al contenedor:
docker exec -it <nombre_contenedor_postgres> psql -U <usuario> -d <nombre_base_datos>
Por ejemplo:
docker exec -it postgres psql -U jazz -d piano

Eliminar todas las tablas
Ejecuta las siguientes consultas SQL para limpiar las tablas en la base de datos:
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO public;
Esto eliminará todas las tablas y recreará el esquema public.

## Para purgar los container y empezar desde cero: ##

1. Limpia los Contenedores y Redes Existentes
Para y Elimina los Contenedores Existentes: Detén y elimina todos los contenedores que puedan estar en conflicto:
docker-compose down --remove-orphans

Elimina Redes No Usadas: Elimina las redes de Docker que no están en uso:
docker network prune -f

Verifica que No Quedan Contenedores: Lista todos los contenedores en ejecución y detenidos:
docker ps -a

Si ves contenedores relacionados con tu proyecto, elimínalos manualmente:
docker rm <container_id>

2. Limpia las Imágenes y Volúmenes
Eliminar Imágenes Relacionadas: Borra las imágenes creadas por Docker Compose:
docker images

Busca imágenes relacionadas con tu proyecto y elimínalas:
docker rmi <image_id>

Eliminar Volúmenes Antiguos: Los volúmenes pueden quedar en un estado corrupto. Límpialos:
docker volume prune -f

Eliminar Directorios Montados: Si estás usando volúmenes montados localmente (e.g., ./data/db:/var/lib/postgresql/data), asegúrate de que no haya problemas con esos directorios. Por ejemplo:
rm -rf  ./services/postgres

3. Reconstruye Todo el Proyecto

Reconstruye las Imágenes: Vuelve a construir las imágenes desde cero para evitar conflictos:
docker-compose build --no-cache

Levanta los Contenedores: Levanta los servicios asegurándote de que las configuraciones sean las correctas:
docker-compose up