import pika

print('Collegamento a RabbitMQ......')
params = pika.ConnectionParameters(host='localhost')
connections=pika.BlockingConnection(params)
channel = connections.channel()
channel.queue_declare(queue='worker_queue')

print('Eseguito......')

def callback(channel,method,properties,body):
    print(f'Ricevuto messaggio {body}')
    
channel.basic_consume(queue='worker_queue',on_message_callback=callback,auto_ack=False)
channel.start_consuming()
    