import pika

print('Collegamento a RabbitMQ......')
params = pika.ConnectionParameters(host='localhost')#PARAMETERS TO PASS TO THE CONNECTION
connections=pika.BlockingConnection(params)#CONNECTION TO RABBITMQ
channel = connections.channel() #GET THE CHANNEL
channel.queue_declare(queue='worker_queue')#CODA THAT CONSUMERS OR WORKERS WILL USE

print('Eseguito......')
#WE SEND TO THE BROKER 100,000 MESSAGES IN QUICK SEUQENCE
i=0
while True:
    message = str(i)
    i+=1
     #WE MUST PUBLISH THE MESSAGE ON THE EXCHANGE
     #THE routing_key IS THE DEFINITION OF BINDING
     #WE ASK THE EXCHANGE TO PUBLISH ALL THAT
     #THE ALREADY DEFINED worker_queue ARRIVES ON A QUEUE
    channel.basic_publish(exchange='',routing_key='worker_queue',body=message)
    print(f'Inviato messaggio {message}')
    if i > 100_000:
        break
#CLOSING THE CONNECTION TO RABBITMQ
connections.close()