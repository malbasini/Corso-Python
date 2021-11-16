import pika
#THE CONNECTION PHASE IS THE SAME VIEW WITH THE PRODUCER
print('Collegamento a RabbitMQ......')
params = pika.ConnectionParameters(host='localhost')
connections=pika.BlockingConnection(params)
channel = connections.channel()
channel.queue_declare(queue='worker_queue')

print('Eseguito......')
#WE MUST INDICATE TO RABBIT THROUGH PIKA WHAT WE MUST DO EVERY
#TIME WE RECEIVE A MESSAGE. TO DO THIS WE WRITE A FUNCTION
#DI CALLBACK THAT WILL BE PERFORMED EVERY TIME A
#MESSAGE FROM THE TAIL.
def callback(channel,method,properties,body):
    print(f'Ricevuto messaggio {body}')
    
channel.basic_consume(queue='worker_queue',on_message_callback=callback,auto_ack=False)
#start_consuming() CAUSES THE ARREST OF THE WORKER WHICH WILL
#WAITING FOR THE PUBLICATION OF MESSAGES FROM THE PRODUCER.
channel.start_consuming()
    