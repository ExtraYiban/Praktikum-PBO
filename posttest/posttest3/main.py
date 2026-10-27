from abc import ABC, abstractmethod

class Panitia(ABC):
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

    @abstractmethod
    def deskripsi_tugas(self):
        """Wajib diimplementasikan oleh setiap subclass Panitia."""
        pass

    @abstractmethod
    def wewenang_khusus(self):
        """Wajib diimplementasikan oleh setiap subclass Panitia."""
        pass

    def jalankan_tugas(self):
        """Method konkret yang mengeksekusi alur kerja panitia secara polimorfis."""
        print(f"[{self._kode_anggota}] {self.nama} ({self.jabatan} - Divisi {self.divisi})")
        print(f"  -> Tugas   : {self.deskripsi_tugas()}")
        print(f"  -> Wewenang: {self.wewenang_khusus()}")

    def tampilkan_info(self):
        print("Kode    :", self._kode_anggota)
        print("Nama    :", self.nama)
        print("Jabatan :", self.jabatan)
        print("Divisi  :", self.divisi)
        print("Status  :", self.__status)

    def koordinasikan_acara(self, acara):
        print(f"{self.nama} ({self.jabatan}) sedang mengoordinasikan acara '{acara.nama_acara}'.")

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
        self._kode_anggota = f"{self._kode_anggota}-KETUA"
        self.mandat = mandat

    def deskripsi_tugas(self):
        return f"Memimpin kepanitiaan berdasarkan mandat: {self.mandat}"

    def wewenang_khusus(self):
        return "Menyetujui proposal, anggaran, dan keputusan strategis MIT-WEEK"

    def tampilkan_info(self):
        super().tampilkan_info()
        print("Mandat  :", self.mandat)


class KoordinatorPanitia(Panitia):
    def __init__(self, nama, divisi, target_anggota):
        super().__init__(nama, "Koordinator", divisi)
        self._kode_anggota = f"{self._kode_anggota}-KOOR"
        self.target_anggota = target_anggota

    def deskripsi_tugas(self):
        return f"Mengawasi operasional Divisi {self.divisi} dengan {self.target_anggota} anggota"

    def wewenang_khusus(self):
        return f"Membagi jobdesk teknis di dalam Divisi {self.divisi}"

    def tampilkan_info(self):
        super().tampilkan_info()
        print("Target Anggota :", self.target_anggota)


class AnggotaPanitia(Panitia):
    def __init__(self, nama, divisi, tugas_lapangan):
        super().__init__(nama, "Anggota", divisi)
        self._kode_anggota = f"{self._kode_anggota}-ANG"
        self.tugas_lapangan = tugas_lapangan

    def deskripsi_tugas(self):
        return f"Melaksanakan teknis lapangan: {self.tugas_lapangan}"

    def wewenang_khusus(self):
        return "Mengeksekusi instruksi koordinator divisi di lapangan"

    def tampilkan_info(self):
        super().tampilkan_info()
        print("Tugas Lapangan :", self.tugas_lapangan)


class Divisi:
    total_divisi = 0
    lokasi_utama = "Universitas Mulawarman"
    maksimal_anggota = 20

    def __init__(self, nama_divisi, koordinator, jumlah_anggota=0):
        self.nama_divisi = nama_divisi
        self.koordinator = koordinator
        self.__jumlah_anggota = 0
        self.jumlah_anggota = jumlah_anggota
        Divisi.total_divisi += 1

    def tampilkan_info(self):
        print("Divisi         :", self.nama_divisi)
        print("Koordinator    :", self.koordinator)
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

    def __add__(self, divisi_lain):
        if isinstance(divisi_lain, Divisi):
            total = self.__jumlah_anggota + divisi_lain.jumlah_anggota
            return f"Total gabungan anggota Divisi {self.nama_divisi} & {divisi_lain.nama_divisi}: {total} orang"
        return NotImplemented

    # Operator Overloading: membandingkan jumlah anggota antar Divisi (>)
    def __gt__(self, divisi_lain):
        if isinstance(divisi_lain, Divisi):
            return self.__jumlah_anggota > divisi_lain.jumlah_anggota
        return NotImplemented

    def __str__(self):
        return f"Divisi {self.nama_divisi} ({self.__jumlah_anggota} anggota)"


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

    def __init__(self, nama_acara, tanggal, penanggung_jawab, kanal_publikasi=None):
        self.nama_acara = nama_acara
        self.tanggal = tanggal
        self.penanggung_jawab = penanggung_jawab
        self.__status = Acara.status_default
        self._divisi = []        # Agregasi: menyimpan referensi objek Divisi dari luar
        self.__rundown = []      # Komposisi: objek Rundown dibuat di dalam Acara
        self.kanal_publikasi = kanal_publikasi
        Acara.total_acara += 1

    def tambah_divisi(self, divisi):
        if isinstance(divisi, Divisi) and divisi not in self._divisi:
            self._divisi.append(divisi)
            print(f"[+] Divisi {divisi.nama_divisi} ditambahkan ke acara '{self.nama_acara}'.")

    def lepas_divisi(self, nama_divisi):
        self._divisi = [d for d in self._divisi if d.nama_divisi != nama_divisi]

    def tambah_rundown(self, waktu, kegiatan):
        self.__rundown.append(Rundown(waktu, kegiatan))

    def umumkan_acara(self):
        if self.kanal_publikasi is not None:
            pesan = f"Acara '{self.nama_acara}' pada {self.tanggal} berstatus: {self.__status}."
            self.kanal_publikasi.kirim_pengumuman(pesan)

    def tampilkan_info(self):
        print("Nama Acara       :", self.nama_acara)
        print("Tanggal          :", self.tanggal)
        print("Penanggung Jawab :", self.penanggung_jawab)
        print("Status           :", self.__status)
        print("Divisi Terlibat  :", ", ".join(d.nama_divisi for d in self._divisi))
        print(f"Rundown ({len(self)} sesi) :")
        for r in self.__rundown:
            print(" -", r)

    def __len__(self):
        return len(self.__rundown)

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status_baru):
        if status_baru == "":
            print("Status acara tidak boleh kosong.")
        else:
            self.__status = status_baru


class NotifikasiEmail:
    def __init__(self, alamat_email):
        self.alamat_email = alamat_email

    def kirim_pengumuman(self, pesan):
        print(f"[EMAIL -> {self.alamat_email}] {pesan}")


class NotifikasiWhatsApp:
    def __init__(self, nomor_grup):
        self.nomor_grup = nomor_grup

    def kirim_pengumuman(self, pesan):
        print(f"[WHATSAPP -> {self.nomor_grup}] {pesan}")


def sebarkan_pengumuman_panitia(daftar_kanal, pesan):
    for kanal in daftar_kanal:
        kanal.kirim_pengumuman(pesan)


if __name__ == "__main__":
    print("=" * 65)
    print(" SISTEM MANAJEMEN KEPANITIAAN DAN PELAKSANAAN MIT-WEEK 2025")
    print("=" * 65)


    print("\n--- 1. BUKTI ABSTRAKSI (INSTANSIASI ABSTRACT CLASS) ---")
    try:
        panitia_abstrak = Panitia("Budi", "Staf", "Acara")
    except TypeError as e:
        print(f"Berhasil menangkap TypeError: {e}")

    print("\n--- 2. POLIMORFISME VIA PEWARISAN (DYNAMIC DISPATCH) ---")
    ketua = KetuaPanitia("Riva", "Inti", "SK Dekan FT Unmul No. 01/2025")
    koor_acara = KoordinatorPanitia("Ajiva", "Acara", 10)
    koor_lomba = KoordinatorPanitia("Rasyid", "Lomba", 8)
    anggota_perlengkapan = AnggotaPanitia("Daffa", "Perlengkapan", "Menyiapkan sound system & proyektor")

    daftar_panitia = [ketua, koor_acara, koor_lomba, anggota_perlengkapan]

    print("Eksekusi method konkret jalankan_tugas() dalam satu loop:")
    for personel in daftar_panitia:
        personel.jalankan_tugas()

    print("\nEksekusi method override tampilkan_info() dalam satu loop:")
    for personel in daftar_panitia:
        personel.tampilkan_info()
        print("-" * 40)

    print("\n--- 3. RELASI UML (ASOSIASI, AGREGASI, KOMPOSISI) ---")
    divisi_acara = Divisi("Acara", koor_acara.nama, 10)
    divisi_lomba = Divisi("Lomba", koor_lomba.nama, 8)

    wa_grup = NotifikasiWhatsApp("Grup-Inti-MIT-WEEK")
    acara1 = Acara("Seminar AI", "29 Oktober 2025", "Divisi Acara", kanal_publikasi=wa_grup)
    acara2 = Acara("Lomba Coding", "30 Oktober 2025", "Divisi Lomba")


    acara1.tambah_divisi(divisi_acara)
    acara1.tambah_divisi(divisi_lomba)
    acara2.tambah_divisi(divisi_lomba)

  
    acara1.tambah_rundown("08.00", "Registrasi & Pembukaan")
    acara1.tambah_rundown("09.00", "Pemaparan Materi Seminar AI")
    acara1.tambah_rundown("11.00", "Tanya Jawab & Penutupan")
    acara2.tambah_rundown("10.00", "Babak Penyisihan Lomba")


    ketua.koordinasikan_acara(acara1)
    print()
    acara1.tampilkan_info()

    print("\nBukti Agregasi (Divisi Lomba tetap ada meski dilepas dari acara2):")
    acara2.lepas_divisi("Lomba")
    divisi_lomba.tampilkan_info()


    print("\n--- 4. DUCK TYPING & SOLID (DIP) ---")
    email_kampus = NotifikasiEmail("mitweek@unmul.ac.id")
    kanal_siaran = [email_kampus, wa_grup]

    sebarkan_pengumuman_panitia(kanal_siaran, "Rapat Pleno MIT-WEEK dimulai pukul 16.00 WITA.")
    print("Pengumuman langsung dari objek Acara (via Dependency Injection):")
    acara1.umumkan_acara()

    print("\n--- 5. OPERATOR OVERLOADING ---")
    print(divisi_acara + divisi_lomba) 
    print(f"Apakah anggota Divisi Acara > Divisi Lomba? {divisi_acara > divisi_lomba}")  # Memanggil __gt__
    print(f"Jumlah sesi rundown pada '{acara1.nama_acara}' (via len()): {len(acara1)} sesi")  # Memanggil __len__