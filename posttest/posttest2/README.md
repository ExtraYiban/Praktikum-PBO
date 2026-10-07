# Sistem Manajemen Kepanitiaan dan Pelaksanaan MIT-WEEK 2025

| Informasi | Detail |
|---|---|
| Nama | Muhammad Zidane Abdul Kadir |
| NIM | 2509106021 |
| Mata Kuliah | Pemrograman Berorientasi Objek |

## Deskripsi

Program CLI ini mengelola panitia, divisi, acara, dan rundown kegiatan MIT-WEEK 2025. Program menerapkan tiga relasi UML yang dipelajari, yaitu asosiasi, agregasi, dan komposisi. Program juga menerapkan inheritance dengan superclass `Panitia` dan dua subclass, yaitu `KetuaPanitia` serta `KoordinatorPanitia`.

## Struktur Proyek

```text
Praktikum-PBO/
└── posttest/
    └── posttest2/
        ├── main.py
        └── README.md
```

## Daftar Kelas

### `Panitia`

`Panitia` adalah superclass untuk anggota kepanitiaan. Kelas ini memiliki atribut `nama`, `jabatan`, `divisi`, atribut protected `_kode_anggota`, dan atribut private `__status`. Method yang tersedia meliputi `tampilkan_info()`, `koordinasikan_acara()`, property `status`, class method, dan static method.

### `KetuaPanitia`

`KetuaPanitia(Panitia)` adalah subclass yang memanggil `super().__init__()` dan menambahkan atribut unik `mandat`.

### `KoordinatorPanitia`

`KoordinatorPanitia(Panitia)` adalah subclass yang memanggil `super().__init__()` dan menambahkan atribut unik `target_anggota`. Method `tampilkan_info()` dioverride untuk menampilkan target anggota, kemudian memanggil method superclass menggunakan `super()`.

### `Divisi`

`Divisi` merupakan objek mandiri yang dibuat di luar `Acara`. Objek ini berisi nama divisi, koordinator, dan jumlah anggota.

### `Acara`

`Acara` menyimpan data kegiatan, referensi divisi, serta rundown kegiatan. `Acara` menggunakan `Divisi` melalui agregasi dan membuat `Rundown` secara internal melalui komposisi.

### `Rundown`

`Rundown` adalah bagian acara yang dibuat langsung oleh `Acara`. Objek ini tidak dibuat secara mandiri pada program sehingga siklus hidupnya bergantung pada `Acara`.

## Penerapan Relasi UML

### 1. Asosiasi

Asosiasi berarti objek hanya menggunakan objek lain melalui parameter method tanpa menyimpan kepemilikan permanen.

Pada program, `Panitia.koordinasikan_acara(acara)` menerima objek `Acara` sebagai parameter. `Panitia` tidak menyimpan acara tersebut sebagai atribut.

```python
ketua.koordinasikan_acara(acara1)
```

### 2. Agregasi

Agregasi berarti objek induk menampung objek bagian yang dibuat dari luar, tetapi objek bagian tetap dapat hidup mandiri.

Objek `Divisi` dibuat terlebih dahulu, kemudian didaftarkan ke `Acara` melalui `tambah_divisi()`. Method `lepas_divisi()` hanya melepas referensi dari acara, bukan menghapus objek `Divisi`.

```python
divisi_lomba = Divisi("Lomba", koor_lomba.nama)
acara2.tambah_divisi(divisi_lomba)
acara2.lepas_divisi("Lomba")
divisi_lomba.tampilkan_info()
```

### 3. Komposisi

Komposisi berarti objek bagian dibuat langsung oleh objek induk dan dimiliki secara eksklusif oleh induknya.

`Acara.tambah_rundown()` membuat objek `Rundown` langsung di dalam method tersebut dan menyimpannya di atribut private `__rundown`.

```python
acara1.tambah_rundown("08.00", "Pembukaan")
acara1.tambah_rundown("09.00", "Seminar AI")
```

## Penerapan Inheritance

### Superclass dan subclass

```text
Panitia
├── KetuaPanitia
└── KoordinatorPanitia
```

- `Panitia` merupakan superclass.
- `KetuaPanitia` merupakan subclass dengan atribut `mandat`.
- `KoordinatorPanitia` merupakan subclass dengan atribut `target_anggota`.

### Penggunaan `super()`

Kedua subclass memanggil konstruktor superclass:

```python
super().__init__(nama, "Ketua Panitia", divisi)
super().__init__(nama, "Koordinator", divisi)
```

`KoordinatorPanitia` juga memanggil method superclass saat melakukan overriding:

```python
super().tampilkan_info()
```

### Method overriding

`KoordinatorPanitia` mendefinisikan ulang `tampilkan_info()` dari `Panitia`. Selain menampilkan informasi umum, subclass tersebut menampilkan `target_anggota`.

### Protected dan private

- `_kode_anggota` adalah atribut protected pada `Panitia` yang dapat digunakan oleh subclass.
- `__status` adalah atribut private pada `Panitia` yang hanya diakses melalui property `status`.
- `__rundown` adalah atribut private pada `Acara` untuk menyembunyikan detail objek komposisi.

## Fitur Program

- Class dan object.
- Atribut kelas dan atribut instance.
- Instance method, class method, dan static method.
- Getter dan setter dengan validasi.
- Asosiasi, agregasi, dan komposisi.
- Superclass dan minimal dua subclass.
- Pemanggilan `super().__init__()`.
- Atribut unik pada setiap subclass.
- Method overriding.
- Protected attribute dan private attribute.
- Pemeriksaan inheritance menggunakan `isinstance()` dan `issubclass()`.

## Cara Menjalankan

Pastikan Python 3 sudah terpasang, lalu jalankan perintah berikut dari folder `Praktikum-PBO`:

```bash
python posttest/posttest2/main.py
```

Program tidak menggunakan library tambahan.

## Pengujian yang Ditampilkan

Program menguji hal-hal berikut:

1. Informasi `KetuaPanitia` dan `KoordinatorPanitia`.
2. Pengecekan `isinstance()` dan `issubclass()`.
3. Method overriding pada `KoordinatorPanitia`.
4. Penggunaan atribut protected `_kode_anggota`.
5. Validasi atribut private melalui property `status`.
6. Asosiasi panitia dengan acara.
7. Agregasi acara dengan divisi.
8. Komposisi acara dengan rundown.
9. Validasi jumlah anggota divisi dan status acara.
10. Rekap total panitia, divisi, dan acara.

## Kesimpulan

Program MIT-WEEK 2025 telah menerapkan seluruh ketentuan posttest: asosiasi, agregasi, komposisi, superclass, dua subclass, `super()`, atribut tambahan pada setiap subclass, method overriding, serta penggunaan atribut protected dan private.
