import pika

print('Collegamento a RabbitMQ......')
params = pika.ConnectionParameters(host='localhost')#PARAMETRI DA PASSARE ALLA CONNESSIONE
connections=pika.BlockingConnection(params)#CONNESSIONE A RABBITMQ
channel = connections.channel() #OTTENGO IL CANALE 
channel.queue_declare(queue='worker_queue')#CODA CHE USERANNO I CONSUMER O WORKER

print('Eseguito......')
#INVIAMO AL BROKER 100.000 MESSAGGI IN RAPIDA SEUQENZA
i=0
while True:
    message = str(i)
    i+=1
    #DOBBIAMO PUBBLICARE IL MESSAGGIO SULLA EXCHANGE
    #LA routing_key E' LA DEFINIZIONE DEL BINDING
    #CHIEDIAMO ALL'EXCHANGE DI PUBBLICARE TUTTO QUELLO CHE 
    #ARRIVA SU UNA CODA LA worker_queue GIA' DEFINITA
    channel.basic_publish(exchange='',routing_key='worker_queue',body=message)
    print(f'Inviato messaggio {message}')
    if i > 100_000:
        break
#CHIUSURA DELLA CONNESSIONE A RABBITMQ 
connections.close()