# producer

# 1 connection with RabbitMQ server.
import pika
# jika machine nya berupa ip maka ganti kata 'localhost' dibawh ini
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


# 2 buat queue dg nama hello (queue hello akan mengirimkan pesan), selain buat queue juga make sure that queue is exist jika tdk ada maka message akan dihapus oleh rabbitmq
channel.queue_declare(queue='hello')

# 3 kirim message 
# setiap message akan dikirim melalui exchange (cara mengirimkan message). disini exchange yg kita gunakan adlh default
# message yg dikirim hrs melalui routing_key berupa queue dlm hal ini pesan ini hanya dapat dikirim dan diterima melalui queue yg bernama 'hello'.
# data yg dikirim adlh string 'Hello WOrld!'
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Pesan ini dikirim dari bahasa python')
# print(" [x] Sent 'Hello World!'")

# 4 tutup koneksi rabbitmq
connection.close()


"""
router_key ibaratnya sprti jalur yg dipilih untuk mencapai ketujuan (misalnya jalur selatan, jalur utara ketika ingin ke cirebon)
queue ibaratnya alamat yg dituju (misalnya ingin ke cirebon)
exchange ibaratnya cara mengirim pesan (misal ke cirebon caranya dg keluarga/sendiri/kelompok)
body adlh data yg ingin dikirimkan
"""