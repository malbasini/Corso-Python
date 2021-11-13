import pika
#LA FASE DI CONNESSIONE E' LA STESSA VISTA CON IL PRODUCER
print('Collegamento a RabbitMQ......')
params = pika.ConnectionParameters(host='localhost')
connections=pika.BlockingConnection(params)
channel = connections.channel()
channel.queue_declare(queue='worker_queue')

print('Eseguito......')
#DOBBIAMO INDICARE A RABBIT TRAMITE PIKA COSA DOBBIAMO FARE OGNI
#VOLTA CHE RICEVIAMO UN MESSAGGIO. PER FARE CIO' SCRIVIAMO UNA FUNZIONE
#DI CALLBACK CHE VERRA' ESEGUITA OGNI VOLTA CHE ARRIVA UN
#MESSAGGIO DALLA CODA.
def callback(channel,method,properties,body):
    print(f'Ricevuto messaggio {body}')
    
channel.basic_consume(queue='worker_queue',on_message_callback=callback,auto_ack=False)
#start_consuming() PROVOCA L'ARRESTO DEL WORKER CHE SI METTERA'
#IN ATTESA DELLA PUBBLICAZIONE DI MESSAGGI DAL PRODUCER.
channel.start_consuming()
    