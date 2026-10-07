class Panitia:
    nama_kegiatan = "MIT-WEEK 2025"
    total_panitia = 0
    status_kegiatan = "Persiapan"

    def __init__(self, nama, jabatan, divisi):
        self.nama = nama
        self.jabatan = jabatan
        self.divisi = divisi
        self._kode_anggota = f"PAN-{Panitia.total_panitia + 1:03d}"
        self.__status = "Aktif"
        Panitia.total_panitia += 1

    def tampilkan_info(self):
        print("Kode    :", self._kode_anggota)
        print("Nama    :", self.nama)
        print("Jabatan:", self.jabatan)
        print("Divisi :", self.divisi)
        print("Status  :", self.__status)

    def koordinasikan_acara(self, acara):
        print(f"{self.nama} mengoordinasikan acara {acara.nama_acara}.")

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


class KetuaPanitia(Panitia):
    def __init__(self, nama, divisi, mandat):
        super().__init__(nama, "Ketua Panitia", divisi)
        self.mandat = mandat


class KoordinatorPanitia(Panitia):
    def __init__(self, nama, divisi, target_anggota):
        super().__init__(nama, "Koordinator", divisi)
        self._kode_anggota = f"{self._kode_anggota}-KOOR"
        self.target_anggota = target_anggota

    def tampilkan_info(self):
        super().tampilkan_info()
        print("Target Anggota :", self.target_anggota)


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
        print("Divisi         :", self.nama_divisi)
        print("Koordinator:", self.koordinator)
        print("Jumlah Anggota :", self.__jumlah_anggota)

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


class Rundown:
    def __init__(self, waktu, kegiatan):
        self.waktu = waktu
        self.kegiatan = kegiatan

    def __str__(self):
        return f"{self.waktu} - {self.kegiatan}"


class Acara:
    total_acara = 0
    status_default = "Direncanakan"
    format_acara = "Offline"

    def __init__(self, nama_acara, tanggal, penanggung_jawab):
        self.nama_acara = nama_acara
        self.tanggal = tanggal
        self.penanggung_jawab = penanggung_jawab
        self.__status = Acara.status_default
        self._divisi = []
        self.__rundown = []
        Acara.total_acara += 1

    def tambah_divisi(self, divisi):
        if isinstance(divisi, Divisi) and divisi not in self._divisi:
            self._divisi.append(divisi)
            print(f"Divisi {divisi.nama_divisi} ditambahkan ke {self.nama_acara}.")

    def lepas_divisi(self, nama_divisi):
        self._divisi = [
            divisi for divisi in self._divisi
            if divisi.nama_divisi != nama_divisi
        ]

    def tambah_rundown(self, waktu, kegiatan):
        self.__rundown.append(Rundown(waktu, kegiatan))

    def tampilkan_info(self):
        print("Nama Acara         :", self.nama_acara)
        print("Tanggal:", self.tanggal)
        print("Penanggung Jawab :", self.penanggung_jawab)
        print("Status             :", self.__status)
        print("Divisi Terlibat    :", ", ".join(
            divisi.nama_divisi for divisi in self._divisi
        ))
        print("Rundown            :")
        for rundown in self.__rundown:
            print(" -", rundown)

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


print("=" * 60)
print(" SISTEM MANAJEMEN KEPANITIAAN DAN PELAKSANAAN MIT-WEEK 2025")
print("=" * 60)

print()
print("--- INHERITANCE PANITIA ---")
ketua = KetuaPanitia("Riva", "Inti", "Mengatur seluruh kepanitiaan")
koor_acara = KoordinatorPanitia("Ajiva", "Acara", 10)
koor_lomba = KoordinatorPanitia("Rasyid", "Lomba", 8)

ketua.tampilkan_info()
print()
koor_acara.tampilkan_info()
print()
print("Cek inheritance:")
print("koor_acara adalah Panitia :", isinstance(koor_acara, Panitia))
print("Koordinator turunan Panitia:", issubclass(KoordinatorPanitia, Panitia))

print()
print("--- CLASS DAN STATIC METHOD PANITIA ---")
print("Status sebelum diubah      :", Panitia.status_kegiatan)
Panitia.ubah_status_kegiatan("Berlangsung")
print("Status setelah diubah      :", Panitia.status_kegiatan)
print("Validasi nama Riva         :", Panitia.validasi_nama("Riva"))
print("Validasi nama kosong       :", Panitia.validasi_nama(""))

print()
print("--- GETTER, SETTER, PROTECTED, DAN PRIVATE ---")
print("Status ketua               :", ketua.status)
ketua.status = "Tidak Aktif"
print("Status ketua setelah diubah:", ketua.status)
ketua.status = ""
print("Kode protected koordinator:", koor_acara._kode_anggota)

print()
print("--- AGREGASI DIVISI ---")
divisi_acara = Divisi("Acara", koor_acara.nama)
divisi_lomba = Divisi("Lomba", koor_lomba.nama)
divisi_acara.jumlah_anggota = 10
divisi_lomba.jumlah_anggota = 8
divisi_acara.tampilkan_info()
print()
divisi_lomba.tampilkan_info()

print()
print("--- DATA ACARA, ASOSIASI, DAN KOMPOSISI ---")
acara1 = Acara("Seminar AI", "29 Oktober 2025", "Divisi Acara")
acara2 = Acara("Lomba", "29 Oktober 2025", "Divisi Acara")

acara1.tambah_divisi(divisi_acara)
acara1.tambah_divisi(divisi_lomba)
acara2.tambah_divisi(divisi_lomba)
acara1.tambah_rundown("08.00", "Pembukaan")
acara1.tambah_rundown("09.00", "Seminar AI")
acara2.tambah_rundown("10.00", "Babak Penyisihan Lomba")

ketua.koordinasikan_acara(acara1)
acara1.tampilkan_info()
print()
print("Divisi tetap ada setelah referensi dilepas dari acara2:")
acara2.lepas_divisi("Lomba")
divisi_lomba.tampilkan_info()

print()
print("--- CLASS, STATIC METHOD, DAN PROPERTY ACARA ---")
print("Format acara               :", Acara.format_acara)
Acara.ubah_format_acara("Offline")
print("Format setelah diubah      :", Acara.format_acara)
print("Nama acara valid           :", Acara.validasi_nama_acara("Seminar AI"))
print("Nama acara kosong          :", Acara.validasi_nama_acara(""))
print("Status acara awal          :", acara1.status)
acara1.status = "Berlangsung"
print("Status acara setelah diubah:", acara1.status)
acara1.status = ""

print()
print("--- VALIDASI DIVISI ---")
print("Jumlah 10 valid            :", Divisi.validasi_jumlah(10))
print("Jumlah -5 valid            :", Divisi.validasi_jumlah(-5))
divisi_acara.jumlah_anggota = -5
print("Jumlah anggota tetap       :", divisi_acara.jumlah_anggota)

print()
print("--- REKAP DATA ---")
print("Total Panitia              :", Panitia.total_panitia)
print("Total Divisi               :", Divisi.total_divisi)
print("Total Acara                :", Acara.total_acara)
print("Komposisi Rundown         : dibuat internal oleh setiap Acara")
print()
print("Program selesai.")
