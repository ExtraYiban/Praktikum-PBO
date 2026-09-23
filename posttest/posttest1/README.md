# Sistem Manajemen Kepanitiaan dan Pelaksanaan MIT-WEEK 2025

> **Nama:** Muhammad Zidane Abdul Kadir 
> **NIM:** 2509106021
> **Mata Kuliah:** Pemrograman Berorientasi Objek  

---

## Daftar Isi

1. [Deskripsi Proyek](#deskripsi-proyek)
2. [Struktur Proyek](#struktur-proyek)
3. [Arsitektur dan Desain OOP](#arsitektur-dan-desain-oop)
4. [Penjelasan Kelas](#penjelasan-kelas)
5. [Fitur Program](#fitur-program)
6. [Alur Program](#alur-program)
7. [Cara Menjalankan](#cara-menjalankan)
8. [Pengujian OOP](#pengujian-oop)
9. [Implementasi Pengujian](#implementasi-pengujian)
10. [Kesimpulan](#kesimpulan)

---

## Deskripsi Proyek

**Sistem Manajemen Kepanitiaan dan Pelaksanaan MIT-WEEK 2025** adalah program berbasis Command Line Interface (CLI) yang dibuat menggunakan Python. Program ini digunakan untuk merepresentasikan data panitia, divisi, dan acara dalam pelaksanaan MIT-WEEK 2025.

Program dibuat berdasarkan materi Pemrograman Berorientasi Objek yang telah dipelajari sampai Modul 3, yaitu:

- Modul 1: Class dan Object
- Modul 2: Atribut dan Method
- Modul 3: Encapsulation dan Property

Fitur utama program meliputi:

- Menyimpan data panitia.
- Menyimpan jabatan dan divisi panitia.
- Menyimpan data divisi dan koordinator divisi.
- Menyimpan jumlah anggota divisi.
- Menyimpan data acara.
- Menampilkan informasi object.
- Menggunakan atribut kelas dan atribut instance.
- Menggunakan instance method, class method, dan static method.
- Menggunakan private attribute.
- Menggunakan getter dan setter dengan `@property`.
- Melakukan validasi pada setter.
- Menguji data valid dan tidak valid.

---

## Struktur Proyek

```text
mit-week-oop/
│
├── main.py
└── README.md
```

### Keterangan

| File | Keterangan |
|---|---|
| `main.py` | File utama yang berisi seluruh class, object, method, dan pengujian program |
| `README.md` | Dokumentasi program |

Program tidak menggunakan library tambahan sehingga tidak membutuhkan `requirements.txt`.

---

## Arsitektur dan Desain OOP

Program memiliki tiga class utama:

```text
                    MIT-WEEK
                       │
        ┌──────────────┼──────────────┐
        │              │              │
        ▼              ▼              ▼
    Panitia          Divisi         Acara
        │              │              │
        ▼              ▼              ▼
   Data orang     Data divisi    Data kegiatan
```

### `Panitia`

Class `Panitia` digunakan untuk menyimpan data orang yang terlibat dalam kepanitiaan.

Object yang dibuat meliputi:

- Ketua Panitia
- Sekretaris
- Bendahara
- Koordinator Divisi

### `Divisi`

Class `Divisi` digunakan untuk menyimpan data bagian kerja dalam kepanitiaan.

Divisi yang digunakan:

- Acara
- Lomba
- Kestari
- Media
- Humas
- Konsumsi
- Keamanan
- Perlengkapan

### `Acara`

Class `Acara` digunakan untuk menyimpan data kegiatan yang dilaksanakan.

Contoh acara yang digunakan:

- Seminar AI
- Lomba

Ketiga class dibuat berdiri sendiri dan tidak menggunakan inheritance karena posttest tidak mewajibkan pewarisan.

---

## Penjelasan Kelas

### 1. `Panitia`

Class `Panitia` digunakan untuk menyimpan informasi anggota kepanitiaan.

#### Atribut Kelas

| Attribute | Keterangan |
|---|---|
| `nama_kegiatan` | Nama kegiatan |
| `total_panitia` | Jumlah object panitia yang telah dibuat |
| `status_kegiatan` | Status kegiatan |

#### Atribut Instance

| Attribute | Keterangan |
|---|---|
| `nama` | Nama panitia |
| `jabatan` | Jabatan panitia |
| `divisi` | Divisi panitia |
| `__status` | Status panitia, bersifat private |

#### Method

- `tampilkan_info()` sebagai instance method.
- `ubah_status_kegiatan()` sebagai class method.
- `validasi_nama()` sebagai static method.
- `status` sebagai getter dan setter.

Contoh object:

```python
ketua = Panitia(
    "Riva",
    "Ketua Panitia",
    "Inti"
)

sekretaris = Panitia(
    "Mayasha",
    "Sekretaris",
    "Inti"
)
```

---

### 2. `Divisi`

Class `Divisi` digunakan untuk menyimpan data divisi dan koordinatornya.

#### Atribut Kelas

| Attribute | Keterangan |
|---|---|
| `total_divisi` | Jumlah object divisi |
| `lokasi_utama` | Lokasi utama kegiatan |
| `maksimal_anggota` | Batas jumlah anggota divisi |

#### Atribut Instance

| Attribute | Keterangan |
|---|---|
| `nama_divisi` | Nama divisi |
| `koordinator` | Nama koordinator divisi |
| `__jumlah_anggota` | Jumlah anggota divisi, bersifat private |

#### Method

- `tampilkan_info()` sebagai instance method.
- `ubah_lokasi_utama()` sebagai class method.
- `validasi_jumlah()` sebagai static method.
- `jumlah_anggota` sebagai getter dan setter.

Contoh object:

```python
divisi_acara = Divisi(
    "Acara",
    "Ajiva"
)

divisi_lomba = Divisi(
    "Lomba",
    "Rasyid"
)
```

---

### 3. `Acara`

Class `Acara` digunakan untuk menyimpan informasi kegiatan.

#### Atribut Kelas

| Attribute | Keterangan |
|---|---|
| `total_acara` | Jumlah object acara |
| `status_default` | Status awal acara |
| `format_acara` | Format pelaksanaan acara |

#### Atribut Instance

| Attribute | Keterangan |
|---|---|
| `nama_acara` | Nama acara |
| `tanggal` | Tanggal acara |
| `penanggung_jawab` | Penanggung jawab acara |
| `__status` | Status acara, bersifat private |

#### Method

- `tampilkan_info()` sebagai instance method.
- `ubah_format_acara()` sebagai class method.
- `validasi_nama_acara()` sebagai static method.
- `status` sebagai getter dan setter.

Contoh object:

```python
acara1 = Acara(
   "Seminar AI",
   "29 Oktober 2025",
    "Divisi Acara"
)

acara2 = Acara(
   "Lomba",
   "29 Oktober 2025",
    "Divisi Acara"
)
```

---

## Fitur Program

| No | Fitur | Keterangan |
|---:|---|---|
| 1 | Data Panitia | Menyimpan data nama, jabatan, dan divisi |
| 2 | Data Divisi | Menyimpan nama divisi dan koordinator |
| 3 | Data Anggota Divisi | Menyimpan jumlah anggota divisi |
| 4 | Data Acara | Menyimpan nama acara, tanggal, dan penanggung jawab |
| 5 | Instance Method | Menampilkan data object |
| 6 | Class Method | Mengubah data yang digunakan bersama oleh class |
| 7 | Static Method | Melakukan validasi sederhana |
| 8 | Getter | Membaca private attribute |
| 9 | Setter | Mengubah private attribute |
| 10 | Validasi | Menolak input kosong atau jumlah negatif |
| 11 | Rekap | Menampilkan total panitia, divisi, dan acara |

---

## Alur Program

```text
[Start]
   |
   v
[Menampilkan Judul Program]
   |
   v
[Membuat Object Panitia]
   |
   v
[Menampilkan Data Panitia]
   |
   v
[Uji Instance Method Panitia]
   |
   v
[Uji Class Method Panitia]
   |
   v
[Uji Static Method Panitia]
   |
   v
[Uji Getter & Setter Panitia]
   |
   v
[Membuat Object Divisi]
   |
   v
[Menampilkan Data Divisi]
   |
   v
[Uji Class Method Divisi]
   |
   v
[Uji Static Method Divisi]
   |
   v
[Uji Getter & Setter Divisi]
   |
   v
[Membuat Object Acara]
   |
   v
[Menampilkan Data Acara]
   |
   v
[Uji Class Method Acara]
   |
   v
[Uji Static Method Acara]
   |
   v
[Uji Getter & Setter Acara]
   |
   v
[Menampilkan Rekap Data]
   |
   v
[End]
```

---

## Cara Menjalankan

### Prasyarat

- Python 3 telah terinstal.
- Terminal atau Command Prompt dapat digunakan.

Cek versi Python:

```bash
python --version
```

### Menjalankan Program

Masuk ke folder project kemudian jalankan:

```bash
python main.py
```

Program tidak memerlukan library tambahan.

---

## Pengujian OOP

Seluruh pengujian dilakukan pada bagian bawah `main.py`.

### 1. Pengujian Object

Program membuat lebih dari dua object untuk `Panitia` dan `Divisi`, serta dua object untuk `Acara`.

Contoh:

```python
ketua = Panitia(...)
sekretaris = Panitia(...)

divisi_acara = Divisi(...)
divisi_lomba = Divisi(...)

acara1 = Acara(...)
acara2 = Acara(...)
```

### 2. Pengujian Instance Method

Instance method dipanggil melalui object.

```python
ketua.tampilkan_info()
koor_acara.tampilkan_info()
divisi_acara.tampilkan_info()
acara1.tampilkan_info()
```

### 3. Pengujian Class Method

Class method dipanggil menggunakan nama class.

```python
Panitia.ubah_status_kegiatan("Berlangsung")
Divisi.ubah_lokasi_utama("Gedung Hexagon")
Acara.ubah_format_acara("Offline")
```

### 4. Pengujian Static Method

Static method dipanggil menggunakan nama class.

```python
Panitia.validasi_nama("Riva")
Panitia.validasi_nama("")

Divisi.validasi_jumlah(10)
Divisi.validasi_jumlah(-5)

Acara.validasi_nama_acara("Seminar AI")
Acara.validasi_nama_acara("")
```

### 5. Pengujian Getter dan Setter Panitia

Getter digunakan untuk membaca private attribute:

```python
print(ketua.status)
```

Setter digunakan untuk mengubah nilai:

```python
ketua.status = "Tidak Aktif"
```

Kemudian diuji dengan data tidak valid:

```python
ketua.status = ""
```

Input kosong ditolak oleh setter.

### 6. Pengujian Getter dan Setter Divisi

Setter diuji dengan jumlah anggota yang valid:

```python
divisi_acara.jumlah_anggota = 15
```

Kemudian diuji dengan jumlah negatif:

```python
divisi_acara.jumlah_anggota = -5
```

Input negatif ditolak karena jumlah anggota tidak boleh negatif.

### 7. Pengujian Getter dan Setter Acara

Setter diuji dengan data valid:

```python
acara1.status = "Berlangsung"
```

Kemudian diuji dengan data kosong:

```python
acara1.status = ""
```

Input kosong ditolak oleh setter.

---

## Implementasi Pengujian

### Instance Method

```python
print("--- INSTANCE METHOD PANITIA ---")

koor_acara.tampilkan_info()
koor_lomba.tampilkan_info()
```

Method `tampilkan_info()` menerima `self` dan digunakan untuk menampilkan data dari object.

### Class Method

```python
print("--- CLASS METHOD PANITIA ---")

print("Status sebelum diubah :", Panitia.status_kegiatan)

Panitia.ubah_status_kegiatan("Berlangsung")

print("Status setelah diubah :", Panitia.status_kegiatan)
```

Class method menggunakan `cls` sehingga dapat mengubah class attribute `status_kegiatan`.

### Static Method

```python
print("--- STATIC METHOD PANITIA ---")

print(
    "Validasi nama Riva :",
    Panitia.validasi_nama("Riva")
)

print(
    "Validasi nama kosong :",
    Panitia.validasi_nama("")
)
```

Static method tidak menggunakan `self` maupun `cls` dan digunakan sebagai fungsi bantuan.

### Getter dan Setter

```python
print("--- GETTER & SETTER PANITIA ---")

print("Status ketua :", ketua.status)

ketua.status = "Tidak Aktif"

print("Status ketua setelah diubah :", ketua.status)

ketua.status = ""
```

Bagian tersebut menguji getter, setter, private attribute, dan validasi.

---

## Rekap Pemenuhan Ketentuan Posttest

| Ketentuan | Implementasi |
|---|---|
| Minimal 3 class | `Panitia`, `Divisi`, `Acara` |
| Minimal 3 atribut kelas | Dipenuhi pada setiap class |
| Atribut instance | Dibuat melalui `__init__()` |
| Public attribute | `nama`, `jabatan`, `divisi`, dan lainnya |
| Private attribute | `__status`, `__jumlah_anggota` |
| Instance method | `tampilkan_info()` |
| Class method | `ubah_status_kegiatan()`, `ubah_lokasi_utama()`, `ubah_format_acara()` |
| Static method | `validasi_nama()`, `validasi_jumlah()`, `validasi_nama_acara()` |
| Getter | `@property` |
| Setter | `@nama_property.setter` |
| Validasi setter | Status kosong dan jumlah anggota negatif ditolak |
| Minimal 2 object/class | Dipenuhi pada bagian main code |
| Pengujian method | Dilakukan pada bagian main code |

---

## Kesimpulan

**Sistem Manajemen Kepanitiaan dan Pelaksanaan MIT-WEEK 2025** merupakan program Python sederhana yang menerapkan konsep Pemrograman Berorientasi Objek berdasarkan materi yang telah dipelajari sampai Modul 3.

Program memiliki tiga class utama:

- `Panitia`
- `Divisi`
- `Acara`

Konsep yang diterapkan meliputi:

- Class dan Object
- Atribut Kelas
- Atribut Instance
- Public Attribute
- Private Attribute
- Instance Method
- Class Method
- Static Method
- Encapsulation
- Getter
- Setter
- Validasi Data

Program dibuat sederhana dan disesuaikan dengan materi yang telah dipelajari sehingga setiap bagian program dapat dijelaskan dan diuji melalui `main.py`.

