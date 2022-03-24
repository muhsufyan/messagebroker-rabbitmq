import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

# logic
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    time.sleep(body.count(b'.'))
    print(" [x] Done")
# jika koneksi terputus agar pesan ketika koneksi tetap tersampaikan ke consumer maka gunakan acknowledge yaitu auto_act=true yg ditempatkan di basic_consume atau di message callback ch.basic_ack(delivery_tag=method.delivery_tag)
    ch.basic_ack(delivery_tag=method.delivery_tag)

# prefetch berfungsi agar tdk diarahkan hanya pd 1 queue, misal ada 2 consumer dimana pesan dikirim ke consumer 1 saja 
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()