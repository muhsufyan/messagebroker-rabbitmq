import pika  
import json  

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))  
channel = connection.channel()
channel.queue_declare(queue='json_data') 

data = {  
    "id": 1,         
    "name": "My Name",         
    "description": "This is description about me"     
} 

message = json.dumps(data)  
channel.basic_publish(exchange='',
                    routing_key="json_data",
                    body=message
                    # properties=pika.BasicProperties(
                    #       delivery_mode = 2) # make message persistent
                    ) 

print(" [x] Sent data to RabbitMQ") 

connection.close()