# FILE Ini berperan sebagai consumer
import pika
import sys

# koneksi ke rabbitmq
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# deklarasi queue dg nama task_queue
channel.queue_declare(queue='task_queue', durable=True)

# pesan yg dikirim diambil dari inputan di terminal oleh user
message = ' '.join(sys.argv[1:]) or "Hello World!"
# publish queue task_queue yg tlh dibuat sblmnya, properties adlh
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    # ?
    properties=pika.BasicProperties(
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
    ))
print(" [x] Sent %r" % message)
connection.close()