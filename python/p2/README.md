new_task jd producer,run dlm 1 terminal perintahnya <b>python new_task.py data ini akan ditampilkan di worker ......</b><br>
buka 3 terminal yg run dg perintah <b>python worker.py</b> <br>
ketika kita menjlnkan new task 1 kali dg data yg ingin dikirim disertai tanda titik sebanyak n maka data yg ingin dikirim<br>
& ditampilkan di worker secara bergiliran pd setiap terminal worker lalu setiap tanda . artinya akan sleep sebanyak jumlah dari . <br>
misal . nya ada 4 maka akan sleep dulu sblm done (pd worker) selama 4 detik sehingga jika ada . sebanyak n maka sleep dulu selama n detik <br>
kasus realnya sprti resize gambar, convert pdf, chatting dll tp blm maksimal karena worker berjln scra bergiliran (bergantian) sehingga untuk chatting <br>
tdk bisa dilakukan sprti itu, dibagian exchange hrs diubah<br>
https://www.rabbitmq.com/tutorials/tutorial-two-python.html link tsb untuk materi bagian 2 tp blm terlalu jelas
