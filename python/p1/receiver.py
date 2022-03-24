# file ini berperan sebagai consumer

import pika, sys, os

def main():
    # 1 koneksi ke rabbitmq
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # 2 buat queue dg nama hello (menerima pesan dari queue hell0), selain buat queue juga make sure that queue is exist jika tdk ada maka message akan dihapus oleh rabbitmq
    channel.queue_declare(queue='hello')

    # 3. fungsi ini akan subscribing(mengonsumsi/menerima/menggunakan pesan) dr queue hello lalu mencetak pesannya. fungsi ini logik pengolahan datanya mau dijdkan apa
    # kasus ini data ditampilkan saja
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
    # 4. fungsi callback akan mengonsumsi queue dr  queue hello yg telah dideklarasikan diatas
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
    # 5. enter a never-ending loop that waits for data and runs callbacks whenever necessary, and catch KeyboardInterrupt during program shutdown.
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)