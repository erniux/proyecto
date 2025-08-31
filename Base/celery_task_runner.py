import subprocess
import logging

logging.basicConfig(
     level=logging.INFO,
     format="%(asctime)s - %(levelname)s - %(message)s",
     handlers=[logging.StreamHandler()]
 )

def run_celery_task(task_name, *args):
    logging.info(f"ya estoy en el celery run y mi task es:::: {task_name} |||| {args}" )

    try:
        flattened_args = []
        for arg in args:
            if isinstance(arg, list):  # Si es una lista
                flattened_args.extend(map(str, arg))  #desempaqueta los elementos
            else:
                flattened_args.append(str(arg))
        
        # Convierte los argumentos en una cadena separada por espacios
        args_str = " ".join(flattened_args)
        
        docker_compose_file = r"C:\Users\ErnaTerceroRodriguez\Documents\jazz\piano\docker-compose.yaml"
            
        command = f"docker-compose -f {docker_compose_file} exec web python manage.py {task_name} {args_str}"
        logging.info(f"comando {command}")                      
        result = subprocess.run(command, shell=True, check=True)
        logging.info(f"Tarea {task_name} ejecutada {result} con argumentos args_str: {args_str}")
        
    except subprocess.CalledProcessError as e:
        logging.error(f"Error al ejecutar la tarea {task_name}: {e}")
        raise

