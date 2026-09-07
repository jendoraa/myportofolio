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
`https://chatgpt.com/share/6a9b9861-0128-83ec-918f-ff826a59564c`