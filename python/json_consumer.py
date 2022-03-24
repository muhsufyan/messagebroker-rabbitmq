import pika  
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))  
channel = connection.channel()
channel.queue_declare(queue="json_data") 

print(' [*] Waiting for messages. To exit press CTRL+C') 

def callback(ch, method, properties, body):  
    print("Method: {}".format(method))     
    print("Properties: {}".format(properties)) 
    data = json.loads(body)
    print("data receive %r"% json.loads(body))   
    print("ID: {}".format(data['id']))     
    print("Name: {}".format(data['name']))      
    print('Description: {}'.format(data['description']))


# kegunaan auto_act=True agar pesan yg disampaikan tersampaikan (diterima) oleh consumer sehingga ketika producer mengirim pesan dulu(dijlnkan pertama kali) kemudian consumer blm (dijlnkan stlh producer) maka pesan akan tetap terkirim/tersampaikan ke consumer
channel.basic_consume(on_message_callback=callback, queue="json_data", auto_ack=False)  
channel.start_consuming()