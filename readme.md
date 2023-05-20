# Task Management System

Aplikasi ini merupakan aplikasi management tugas sederhana yang mendukung *RESTful API*. Aplikasi ini dibuat menggunakan framework **django** dan menggunakan library khusus django yaitu **django rest framework**.

## Deployment Aplikasi

Beberapa tahap berikut dilakukan untuk melakukan deploy aplikasi:

1. Membuat python virtual environment
```
python -m virtualenv env
```

2. Mengaktifkan virtual environment

Windows
```
env\Scripts\activate
```

Linux
```
source env/bin/activate
```

3. Install library python yang diperlukan
```
python -m pip install -r requirements.py
```

4. Masuk ke directory task_management
```
cd task_management
```

5. Mengeksekusi beberapa command dan melakukan prompt password admin
```
python generate_security_key.py
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --username admin --email admin@admin.com
```

6. Menjalankan django webservice
```
python manage.py runserver
```

## Menggunakan aplikasi

### Melalui browser

1. Melihat semua tugas dan membuat tugas baru

masukkan url berikut pada browser
```
localhost:8000/tasks/api
```
Pada halaman ini kita dapat mengakses fungsi untuk melihat semua tugas dan membuat tugas baru.

Untuk membuat tugas dapat baru bisa dengan memasukkan contoh JSON berikut pada input content:
```
{
	"title": "Tugas dari ibu",
	"description": "Menyapu halaman rumah"
}
```
setelah itu kita cukup menekan tombol post untuk membuat data tugas baru.

Tombol get juga dapat digunakan untuk melakukan list ulang semua tugas.

2. Melihat detail tugas, mengupdate dan menghapus tugas

masukkan url berikut pada browser
```
localhost:8000/tasks/api/task_id
```
task_id bisa diubah dengan id yang dimiliki oleh tugas, misalkan 1

Pada halaman ini kita dapat mengakses fungsi untuk melihat detail tugas, mengupdate tugas maupun menghapus tugas.

Untuk mengupdate tugas dapat dilakukan dengan memasukan contoh JSON berikut pada input content:
```
{
	"title": "Tugas dari ibu",
	"description": "Menyapu halaman rumah"
	"is_complete": true,
}
```
Pada contoh ini kita mengupdate bahwa tugas dari ibu telah selasai kita laksanakan

Untuk refresh data atau memastikan bahwa data telah terupdate cukup dengan menekan tombol get.

Adapun untuk menghapus data cukup dengan menekan tombol delete.

### Melalui contoh script
Melalui script ini kita bisa melakukan CRUD menggunakan REST yang telah kita buat dengan lebih mudah dan lebih cepat. Script dapat dijalankan dengan menjalankan command berikut pada terminal:
```
python example_script.py
```

Pada tahap pertama script akan melakukan proses POST dan GET pada bagian add several data dan list data. Pada tahap ini script akan menambah beberapa tugas dan baru dan menampilkan hasil tugas-tugas yang ditambahkan pada display terminal.

Selanjutnya tahap selanjutnya script akan melakukan proses GET dan UPDATE pada bagian update data dan detail data. Pada tahap ini script akan mengupdate beberapa dan menampilkan hasil perubahan data berupa detail di terminal.

Proses terakhir script akan melakukan proses DELETE dan GET pada bagian delete data. Pada tahap ini script akan menghapus salah satu data dan menampilkan list data setelah adanya data yang dihapus.


### Melalui admin panel
Buka alamat berikut pada browser:
```
localhost:8000/admin
```
Maka kita akan masuk ke halaman login admin. Masukkan username admin dan password yang telah dibuat pada tahap deploy. Setelah itu kita buka menu tasks yang berada di sebelah kiri halaman, maka akan muncul daftar tugas yang telah dibuat. Halaman ini akan membantu kita untuk melihat hasil perubahan data yang telah dilakukan baik menggunakan browser maupun script.