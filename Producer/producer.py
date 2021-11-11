import pika

print('Collegamento a RabbitMQ......')
params = pika.ConnectionParameters(host='localhost')
connections=pika.BlockingConnection(params)
channel = connections.channel()
channel.queue_declare(queue='worker_queue')

print('Eseguito......')

i=0
while True:
    message = str(i)
    i+=1
    channel.basic_publish(exchange='',routing_key='worker_queue',body=message)
    print('Inviato messaggio %s',message)
    if i > 100_000:
        break
    
connections.close()