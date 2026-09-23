
class Panitia:

    nama_kegiatan = "MIT-WEEK 2025"
    total_panitia = 0
    status_kegiatan = "Persiapan"

    def __init__(self, nama, jabatan, divisi):
        self.nama = nama
        self.jabatan = jabatan
        self.divisi = divisi

        self.__status = "Aktif"

        Panitia.total_panitia += 1

    def tampilkan_info(self):
        print("Nama    :", self.nama)
        print("Jabatan :", self.jabatan)
        print("Divisi  :", self.divisi)
        print("Status  :", self.__status)

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status_baru):
        if status_baru == "":
            print("Status tidak boleh kosong.")
        else:
            self.__status = status_baru

    @classmethod
    def ubah_status_kegiatan(cls, status_baru):
        if status_baru == "":
            print("Status kegiatan tidak boleh kosong.")
        else:
            cls.status_kegiatan = status_baru

    @staticmethod
    def validasi_nama(nama):
        return nama != ""


class Divisi:

    total_divisi = 0
    lokasi_utama = "Universitas Mulawarman"
    maksimal_anggota = 20

    def __init__(self, nama_divisi, koordinator):
        self.nama_divisi = nama_divisi
        self.koordinator = koordinator

        self.__jumlah_anggota = 0

        Divisi.total_divisi += 1

    def tampilkan_info(self):
        print("Divisi          :", self.nama_divisi)
        print("Koordinator     :", self.koordinator)
        print("Jumlah Anggota  :", self.__jumlah_anggota)

    @property
    def jumlah_anggota(self):
        return self.__jumlah_anggota

    @jumlah_anggota.setter
    def jumlah_anggota(self, jumlah):
        if jumlah < 0:
            print("Jumlah anggota tidak boleh negatif.")
        elif jumlah > Divisi.maksimal_anggota:
            print("Jumlah anggota melebihi batas.")
        else:
            self.__jumlah_anggota = jumlah

    @classmethod
    def ubah_lokasi_utama(cls, lokasi_baru):
        if lokasi_baru == "":
            print("Lokasi tidak boleh kosong.")
        else:
            cls.lokasi_utama = lokasi_baru

    @staticmethod
    def validasi_jumlah(jumlah):
        return jumlah >= 0



class Acara:

    total_acara = 0
    status_default = "Direncanakan"
    format_acara = "Offline"

    def __init__(self, nama_acara, tanggal, penanggung_jawab):
        self.nama_acara = nama_acara
        self.tanggal = tanggal
        self.penanggung_jawab = penanggung_jawab

        self.__status = "Direncanakan"

        Acara.total_acara += 1

    def tampilkan_info(self):
        print("Nama Acara         :", self.nama_acara)
        print("Tanggal            :", self.tanggal)
        print("Penanggung Jawab   :", self.penanggung_jawab)
        print("Status             :", self.__status)

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status_baru):
        if status_baru == "":
            print("Status acara tidak boleh kosong.")
        else:
            self.__status = status_baru

    @classmethod
    def ubah_format_acara(cls, format_baru):
        if format_baru == "":
            print("Format acara tidak boleh kosong.")
        else:
            cls.format_acara = format_baru

    @staticmethod
    def validasi_nama_acara(nama):
        return nama != ""



print("=" * 55)
print(" SISTEM MANAJEMEN KEPANITIAAN DAN PELAKSANAAN MIT-WEEK 2025")
print("=" * 55)



print()
print("--- DATA PANITIA ---")

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

bendahara = Panitia(
    "Mazu",
    "Bendahara",
    "Inti"
)

koor_acara = Panitia(
    "Ajiva",
    "Koordinator",
    "Acara"
)

koor_lomba = Panitia(
    "Rasyid",
    "Koordinator",
    "Lomba"
)

koor_kestari = Panitia(
    "Indi",
    "Koordinator",
    "Kestari"
)

koor_media = Panitia(
    "Nayul",
    "Koordinator",
    "Media"
)

koor_humas = Panitia(
    "Ridho",
    "Koordinator",
    "Humas"
)

koor_konsumsi = Panitia(
    "Wahyu",
    "Koordinator",
    "Konsumsi"
)

koor_keamanan = Panitia(
    "Naufal",
    "Koordinator",
    "Keamanan"
)

koor_perlengkapan = Panitia(
    "Melki",
    "Koordinator",
    "Perlengkapan"
)

ketua.tampilkan_info()

print()

sekretaris.tampilkan_info()


print()
print("--- INSTANCE METHOD PANITIA ---")

koor_acara.tampilkan_info()
print()
koor_lomba.tampilkan_info()



print()
print("--- CLASS METHOD PANITIA ---")

print("Status sebelum diubah :", Panitia.status_kegiatan)

Panitia.ubah_status_kegiatan("Berlangsung")

print("Status setelah diubah :", Panitia.status_kegiatan)


print()
print("--- STATIC METHOD PANITIA ---")

print(
    "Validasi nama Riva :",
    Panitia.validasi_nama("Riva")
)

print(
    "Validasi nama kosong :",
    Panitia.validasi_nama("")
)



print()
print("--- GETTER & SETTER PANITIA ---")

print("Status ketua :", ketua.status)

ketua.status = "Tidak Aktif"

print("Status ketua setelah diubah :", ketua.status)

ketua.status = ""

print("Status ketua setelah input salah :", ketua.status)



print()
print("--- DATA DIVISI ---")

divisi_acara = Divisi(
    "Acara",
    "Ajiva"
)

divisi_lomba = Divisi(
    "Lomba",
    "Rasyid"
)

divisi_kestari = Divisi(
    "Kestari",
    "Indi"
)

divisi_media = Divisi(
    "Media",
    "Nayul"
)

divisi_humas = Divisi(
    "Humas",
    "Ridho"
)

divisi_konsumsi = Divisi(
    "Konsumsi",
    "Wahyu"
)

divisi_keamanan = Divisi(
    "Keamanan",
    "Naufal"
)

divisi_perlengkapan = Divisi(
    "Perlengkapan",
    "Melki"
)

divisi_acara.jumlah_anggota = 10
divisi_lomba.jumlah_anggota = 8

divisi_acara.tampilkan_info()

print()

divisi_lomba.tampilkan_info()


print()
print("--- CLASS METHOD DIVISI ---")

print("Lokasi utama :", Divisi.lokasi_utama)

Divisi.ubah_lokasi_utama("Gedung Hexagon")

print("Lokasi setelah diubah :", Divisi.lokasi_utama)


print()
print("--- STATIC METHOD DIVISI ---")

print(
    "Jumlah 10 valid :",
    Divisi.validasi_jumlah(10)
)

print(
    "Jumlah -5 valid :",
    Divisi.validasi_jumlah(-5)
)



print()
print("--- GETTER & SETTER DIVISI ---")

print("Jumlah anggota awal :", divisi_acara.jumlah_anggota)

divisi_acara.jumlah_anggota = 15

print(
    "Jumlah anggota setelah diubah :",
    divisi_acara.jumlah_anggota
)

divisi_acara.jumlah_anggota = -5

print(
    "Jumlah anggota setelah input salah :",
    divisi_acara.jumlah_anggota
)



print()
print("--- DATA ACARA ---")

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

acara1.tampilkan_info()

print()

acara2.tampilkan_info()


print()
print("--- CLASS METHOD ACARA ---")

print("Format acara :", Acara.format_acara)

Acara.ubah_format_acara("Offline")

print("Format setelah diubah :", Acara.format_acara)



print()
print("--- STATIC METHOD ACARA ---")

print(
    "Nama acara valid :",
    Acara.validasi_nama_acara("Seminar AI")
)

print(
    "Nama acara kosong :",
    Acara.validasi_nama_acara("")
)



print()
print("--- GETTER & SETTER ACARA ---")

print("Status acara awal :", acara1.status)

acara1.status = "Berlangsung"

print(
    "Status acara setelah diubah :",
    acara1.status
)

acara1.status = ""

print(
    "Status acara setelah input salah :",
    acara1.status
)



print()
print("--- REKAP DATA ---")

print("Total Panitia :", Panitia.total_panitia)
print("Total Divisi  :", Divisi.total_divisi)
print("Total Acara   :", Acara.total_acara)

print()
print("Program selesai.")