import os
from celery import Celery
from services.generator import Generator
from services.output import dump_report, dump_result

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'amqp://rabbitmq:rabbitmq@rabbit:5672/'),
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'rpc://')

TWO_MB = 2097152
celery = Celery('worker', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

@celery.task()
def generate_object_background():
    generator = Generator()
    object_string = str(generator.get_object())
    
    while len(object_string.encode('utf-8')) <= TWO_MB:
        object_string += ', ' + str(generator.get_object())
        
    dump_report(generator.make_report())
    dump_result(object_string)
    return generator.make_report()