# Ini Portofolio saya
## Biodata
- Nama : Rajendra Akbar Mahdiansyah
- NPM : 2506596874
- Kelas : PBP C

## Cara Menjalankan

1. Clone repository dan masuk ke folder proyek.
2. Buat dan aktifkan virtual environment jika diperlukan.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Jalankan development server:

```bash
python manage.py runserver
```

5. Buka `http://127.0.0.1:8000/`

Website juga dapat diakses melalui deployment berikut:

`https://rajendra-akbar-myportofolio.pws.cs.ui.ac.id/`

## Tugas 1
### 1. Penggunaan elemen semantik HTML 5
Ya, saya menggunakan elemen semantik HTML5, yakni `<section>`. Setiap bagian utama website, seperti Hero, About, Skills, Experience, dan Contact, dipisahkan menggunakan `<section>` agar struktur HTML lebih terorganisir dan mudah dipahami.

Penggunaan elemen semantik ini membantu saya karena website portofolio memang terdiri dari beberapa bagian dengan fungsi yang berbeda. Selain membuat kode lebih rapi, struktur tersebut juga memudahkan saya ketika ingin mengatur CSS berdasarkan bagian tertentu. Misalnya, saya dapat memberikan styling khusus untuk bagian skill atau experience saja tanpa mencampurkan struktur antarbagian. Menurut saya, penggunaan `<section>` juga membuat struktur halaman lebih jelas dibandingkan jika seluruh halaman hanya menggunakan `<div>`.

Selain `<section>`, saya juga menggunakan elemen `<header>` dan `<footer>` sebagai pembeda antara navbar (saya ngikut template pake header), main, dan footer.

### 2. Tantangan dalam membuat CSS responsive
Tantangan terbesar yang saya temukan adalah menyesuaikan ukuran dan posisi elemen ketika layar berubah dari desktop ke tablet (karena keterbatasan waktu, saya tidak menerapkan versi mobile). Pada desktop, saya cenderung menggunakan layout horizontal, padding yang lebih besar, dan ukuran elemen yang lebih luas. Namun, ketika ukuran layar mengecil, beberapa elemen mulai rapat atau tidak lagi terlihat proporsional.

Contohnya pada bagian Skills, saya awalnya mengatur beberapa card dalam satu baris. Ketika dibuat responsive, saya perlu mempertimbangkan kembali jumlah card dalam satu baris, ukuran card, gap, serta padding pada container. Saya juga menemukan bahwa penggunaan max-width dan padding yang sama belum tentu menghasilkan tampilan yang sama pada setiap section karena struktur dan ukuran kontennya berbeda. Selain itu, card terasa tidak nyaman dilihat dalam mode tablet, sehingga saya menerapkan grid untuk versi tablet.

Untuk menentukan elemen mana yang harus diprioritaskan, saya melihat fungsi dan tingkat kepentingan informasi. Elemen yang paling penting seperti nama, deskripsi singkat, dan tombol utama harus tetap terlihat jelas. Setelah itu, saya menyesuaikan ukuran font, gambar, spacing, dan mengubah layoutnya sesuai mode tampilan. Saya juga mengevaluasi hasilnya dengan mencoba beberapa ukuran viewport (diseret manual dari 1440px -> 700px), bukan hanya melihat tampilan pada ukuran desktop atau tablet saja.

### 3. Batasan web static dan fungsionalitasnya
Karena website yang saya buat masih berupa static web, informasi di dalamnya masih harus diubah secara manual ke kode HTML. Hal ini cukup membatasi saya ketika ingin mengelola informasi portofolio yang mungkin bakal berubah kedepannya, seperti daftar experience, skills, atau informasi pribadi. Jika terdapat perubahan, saya harus mengubah source code dan melakukan deploy ulang.

Berdasarkan keterbatasan tersebut, saya melihat beberapa fungsionalitas yang dapat ditambahkan jika website dikembangkan menjadi dynamic web, seperti database untuk menyimpan experience dan skills. Dengan demikian, website tidak hanya berfungsi sebagai halaman informasi statis, tetapi juga dapat menjadi platform portofolio yang lebih interaktif dan mudah dikelola.


## Tugas 2
### 1. Alur Saat Membuka Halaman Portofolio Baru
Browser mengirim request HTTP GET ke URL tertentu (misal /projects/). urls.py projek menerima request tersebut dan meneruskannya ke urls.py aplikasi main. urls.py aplikasi mencocokkan path dengan fungsi view show_projects. View berinteraksi dengan Model Project untuk mengambil data dari database via Project.objects.all(). View memasukkan data tersebut ke dalam dictionary context lalu memanggil Template project_list.html. Template me-render data dinamis menjadi kode HTML utuh, lalu view mengembalikannya sebagai HTTP response ke browser pengguna.

### 2. Pentingnya Menyimpan Data di Model
Menambah atau memperbarui proyek cukup dilakukan melalui database tanpa perlu mengubah kode file HTML atau melakukan deploy ulang setiap ada revisi konten. Selain itu, data di model mempermudah operasi dinamis seperti penyaringan (filter), pengurutan, atau pembuatan API/fitur pencarian di kemudian hari.

### 3. Perbedaan makemigrations dan migrate
makemigrations berfungsi membaca definisi model pada models.py dan mencatat rencana perubahannya ke dalam bentuk berkas migrasi baru di folder migrations/. Perintah ini belum mengubah skema database.

Sedangkan migrate berfungsi mengeksekusi berkas-berkas migrasi yang belum dijalankan ke dalam basis data dan mengubah skema tabel secara langsung.

Contoh perubahan: Menambahkan atribut/field baru, misalnya tech_stack = models.CharField(max_length=255), pada model Project. Kamu harus menjalankan python manage.py makemigrations untuk membuat instruksi pembuatan kolom baru, lalu menjalankan python manage.py migrate agar kolom tersebut benar-benar dibuat pada tabel database.

## Tugas 3
### 1. Mengapa menggunakan ModelForm dan mengapa perlu {% csrf_token %}?
`ModelForm` digunakan karena dapat membuat form berdasarkan struktur Model yang sudah didefinisikan di Django. Dengan `ModelForm`, field pada form dapat disesuaikan secara otomatis dengan field yang terdapat pada model sehingga kode yang perlu ditulis menjadi lebih sedikit dan lebih mudah dikelola. Selain itu, `ModelForm` juga membantu melakukan validasi data sebelum data tersebut disimpan ke database. Jika membuat form HTML secara manual, developer harus menentukan sendiri setiap field dan melakukan proses validasi serta penyimpanan datanya.

`{% csrf_token %}` wajib ditambahkan pada form yang menggunakan metode POST karena berfungsi sebagai perlindungan terhadap serangan Cross-Site Request Forgery (CSRF). Token tersebut digunakan Django untuk memastikan bahwa request POST benar-benar berasal dari halaman website yang sah. Tanpa token CSRF yang valid, Django biasanya akan menolak request tersebut dengan respons 403 Forbidden.

### 2. Mengapa JSON lebih banyak digunakan dibandingkan XML dalam pengembangan aplikasi web modern?
JSON lebih banyak digunakan karena memiliki struktur yang sederhana, ringkas, dan mudah dibaca baik oleh manusia maupun program. JSON juga memiliki format yang sangat dekat dengan struktur data pada JavaScript, sehingga mudah digunakan dalam komunikasi antara frontend dan backend.

Dibandingkan XML, JSON umumnya membutuhkan lebih sedikit karakter untuk merepresentasikan data karena tidak memerlukan tag pembuka dan penutup untuk setiap elemen. Hal tersebut membuat ukuran data yang dikirim melalui jaringan dapat menjadi lebih kecil. JSON juga banyak didukung oleh berbagai bahasa pemrograman dan framework modern sehingga sering digunakan dalam REST API dan komunikasi antara aplikasi frontend dengan backend.

### 3. Bagaimana alur view mengembalikan data portofolio dalam bentuk JSON dan mengapa perlu serialization?

Ketika pengguna mengakses URL yang mengarah ke suatu fungsi view, Django menerima request tersebut dan menjalankan view yang sesuai. View kemudian mengambil data portofolio dari database menggunakan model Django, misalnya dengan Model.objects.all(). Data yang diperoleh masih berupa objek atau QuerySet Django sehingga belum dapat langsung dikembalikan dalam format JSON.

Oleh karena itu, dilakukan proses serialization, yaitu mengubah data dari model Django menjadi struktur data yang dapat direpresentasikan dalam format JSON. Setelah proses serialization selesai, hasilnya dapat diubah menjadi string JSON menggunakan json.dumps(). String JSON tersebut kemudian dikembalikan kepada client menggunakan HttpResponse dengan menentukan content_type="application/json".

# Pengungkapan Penggunaan AI
Dalam pengerjaan website portofolio ini, saya menggunakan ChatGPT (OpenAI) sebagai alat bantu dalam proses pembelajaran, perancangan, implementasi, dan evaluasi website. Penggunaan AI dilakukan sebagai pendukung proses pengerjaan, sedangkan keputusan akhir mengenai desain, struktur, kode, dan implementasi website tetap dilakukan dan diverifikasi oleh saya sendiri.

## 1. AI yang Digunakan
AI yang digunakan dalam pengerjaan proyek ini adalah ChatGPT (OpenAI). ChatGPT digunakan sebagai asisten untuk berdiskusi mengenai responsive web design, struktur website, debugging, serta evaluasi terhadap hasil implementasi.

## 2. Bagian yang Dibantu oleh AI
AI digunakan pada beberapa tahap pengerjaan website, antara lain:

### a. CSS dan Layout
ChatGPT digunakan untuk membantu memahami dan mengevaluasi penggunaan CSS, terutama terkait:
- positioning,
- hover effect,
- expanding pill (menggantikan *hover popup* statis), 
- responsive layout.

AI juga digunakan ketika terdapat perbedaan hasil tampilan antar-section meskipun menggunakan nilai CSS yang terlihat serupa. Diskusi dengan AI membantu mengidentifikasi pengaruh struktur parent element, ukuran konten, padding, dan batas lebar terhadap hasil akhir layout saat kartu melebar (*expand*).

### b. Responsive Design
AI digunakan sebagai bahan diskusi ketika menyesuaikan website agar dapat digunakan pada berbagai ukuran layar. Beberapa hal yang dibahas meliputi:
- perubahan layout dari horizontal menjadi vertikal,
- penyesuaian ukuran card,
- pengaturan jumlah card dalam satu baris,
- penyesuaian padding dan gap,
- penggunaan max-width,
- penyesuaian ukuran teks dan gambar,
- penentuan prioritas elemen pada ukuran layar yang lebih kecil.

AI membantu memberikan alternatif pendekatan, tetapi perubahan akhir pada CSS dilakukan dan disesuaikan berdasarkan hasil pengujian tampilan website.

### c. Interaktivitas JavaScript
AI digunakan untuk menyusun logika interaksi sederhana pada DOM:
- mengimplementasikan *event listener* `click` pada kartu skill,
- membuat logika *toggle* status aktif (`classList.toggle('active')`),
- memastikan interaksi bersifat eksklusif, di mana kartu lain otomatis menutup ketika salah satu kartu skill diklik.

### d. Debugging dan Pemecahan Masalah
ChatGPT digunakan untuk membantu menganalisis masalah pada kode HTML dan CSS. Kode yang bermasalah diberikan sebagai konteks untuk kemudian dianalisis penyebabnya. Contoh masalah yang dibahas antara lain:
- posisi elemen yang berubah ketika diberikan padding,
- ukuran container yang tidak sesuai dengan ekspektasi,
- perbedaan hasil max-width antar-section,
- perubahan posisi elemen ketika menggunakan hover,
- pengaturan tampilan link agar tidak memiliki underline,
- penyesuaian border pada gambar,
- serta permasalahan layout pada responsive design.

### e. Membantu membuat dan memperbaiki views, models, forms serta template HTMLS
AI digunakan untuk membantu memahami hubungan antara komponen Django dalam pengembangan website. Pada bagian models, AI membantu dalam menentukan struktur data yang diperlukan untuk menyimpan informasi seperti nama pengalaman, deskripsi, posisi, dan gambar. Pada bagian views, AI membantu membuat logika untuk mengambil data dari database serta menampilkan, menambahkan, mengubah, dan menghapus data. AI juga membantu dalam pembuatan dan perbaikan forms untuk menerima input dari pengguna. Selain itu, AI digunakan untuk membantu memperbaiki template HTML agar dapat menampilkan data dari database secara dinamis menggunakan Django Template Language.

### f. Membantu dalam implementasi fitur CRUD Experience.
AI digunakan sebagai bantuan dalam mengimplementasikan fitur CRUD (Create, Read, Update, Delete) pada halaman Experience. Pada tahap Create, AI membantu membuat mekanisme untuk menambahkan data pengalaman baru ke database, termasuk data gambar. Pada tahap Read, AI membantu menampilkan data Experience yang tersimpan di database ke halaman website secara dinamis. Pada tahap Update, AI membantu membuat fungsi untuk mengubah data Experience yang sudah tersimpan. Sedangkan pada tahap Delete, AI membantu membuat mekanisme untuk menghapus data Experience dari database. AI juga digunakan untuk membantu melakukan debugging ketika terdapat kendala dalam proses CRUD, seperti data yang tidak tampil atau gambar yang tidak berhasil tersimpan.

AI memberikan kemungkinan penyebab dan solusi, kemudian solusi tersebut diuji kembali pada website.

## 3. Modifikasi terhadap Output AI
Output yang diberikan oleh AI tidak digunakan secara langsung tanpa modifikasi. Setiap saran atau potongan kode yang diberikan ChatGPT dipelajari terlebih dahulu, kemudian disesuaikan dengan struktur project dan kebutuhan desain website.
Modifikasi yang dilakukan meliputi:
- menyesuaikan ukuran, spacing, dan layout,
- menyesuaikan warna dengan design system yang digunakan,
- menggabungkan beberapa tampilan dari CSS,
- melakukan pengujian kembali untuk memastikan hasil sesuai dengan desain yang diinginkan.

Dengan demikian, output AI digunakan sebagai referensi dan starting point, bukan sebagai hasil akhir yang langsung digunakan.

## 4. Integrasi AI dalam Pengerjaan
Integrasi AI dilakukan melalui proses iteratif:
Saya membuat atau mengubah struktur HTML/CSS berdasarkan desain yang telah dirancang. Ketika menemukan masalah atau membutuhkan masukan, saya memberikan kode dan konteks permasalahan kepada ChatGPT. ChatGPT memberikan alternatif solusi. Saya mempelajari dan memilih solusi yang sesuai dengan kebutuhan website saya. Solusi tersebut saya implementasikan. Hasil implementasi diuji kembali melalui browser.
Jika hasilnya belum sesuai, saya melakukan evaluasi dan kembali memperbaiki kode.

Dengan proses tersebut, AI berperan sebagai asisten diskusi dan debugging, sementara proses implementasi dan pengambilan keputusan tetap dilakukan oleh saya.

## 5. Batasan Penggunaan AI

AI tidak digunakan untuk menentukan keseluruhan konsep dan desain website secara otomatis. Struktur utama website, pemilihan tampilan, susunan section, pemilihan warna, serta keputusan akhir mengenai layout ditentukan berdasarkan rancangan yang telah saya buat.

AI juga tidak digunakan sebagai pengganti proses memahami kode. Setiap kode atau solusi yang diperoleh dari AI dipahami, dimodifikasi, dan diuji kembali sebelum digunakan.

## 6. Referensi Percakapan AI
Percakapan dengan ChatGPT yang digunakan sebagai salah satu referensi dalam proses pengerjaan dapat dilihat melalui: 
`https://chatgpt.com/share/6a9b9861-0128-83ec-918f-ff826a59564c`(2-7 September 2026)
`https://chatgpt.com/share/6ab1214d-a604-83ec-b46d-579898215cdc`(16-21 September 2026)