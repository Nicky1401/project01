from os import system
import sys

def print_menu():
	system("cls")
	print("PENDAFTARAN SISWA BARU")
	menu_tampilan = """
	----------------------
	PENDAFTARAN SISWA BARU
	----------------------
	[A]. Penambahan Siswa
	[B]. Lihat Seluruh daftar siswa
	[C]. Cari Siswa
	[D]. Siswa Yang Keluar Dari Sekolah
	[E]. Edit Data Siswa
	[F]. Tentang Sekolah
	[G]. Keluar Dari Pengecekan
	"""
	print(menu_tampilan)

def penambahan_siswa():
	system("cls")
	print("Menambahkan Siswa Baru\nInformasi Siswa")
	nama = input("Nama\t:")
	telp = input("Telp\t:")
	email = input("email\t:")
	alamat = input("Alamat\t:")
	nama_orangtua = input("Nama Orangtua\t:")
	asal_sekolah = input("Asal Sekolah\t:")
	hasi_ujian_sekolah = input("Hasil Ujian Sekolah\t:")
	respon = input(f"Yakin ingin menyimpan data siswa ini {nama} ? (Y/N) ")
	if respon.upper() == "Y":
		datas[nama] = {
		"telp" : telp,
		"email" : email,
		"alamat" : alamat,
		"nama orangtua" : nama_orangtua,
		"asal sekolah" : asal_sekolah,
		"hasil ujian sekolah" : hasi_ujian_sekolah
	}
		print("Data Siswa Tersimpan.")
	else:
		print("Batal menyimpan.")
	input("Tekan ENTER untuk kembali ke MENU")

def lihat_seluruh_daftar_siswa():
	system("cls")
	print("Daftar Siswa Yang Telah Disimpan")
	if len(datas) == 0:
		print("Belum ada data yg disimpan saat ini.")
	else:
		print("NAMA\tNOMOR TELEPON\tEMAIL\tALAMAT\tNAMA ORANGTUA\tASAL SEKOLAH\tHASIL UJIAN SEKOLAH")
		for data in datas:
			print(data, datas[data]['telp'], datas[data]['email'], datas[data]['nama orangtua'], datas[data]['asal sekolah'], datas[data]['hasil ujian sekolah'])
	input("Tekan ENTER untuk kembali ke MENU")

def cari_siswa(data):
	if data in datas:
		print("- RESULT -")
		print("Nama :",data)
		print("Telp :",datas[data]["telp"])
		print("email :",datas[data]["email"])
		print("alamat :",datas[data]["alamat"])
		print("Nama OrangTua :",datas[data]["nama orangtua"])
		print("Asal Sekolah :",datas[data]["asal sekolah"])
		print("Hasil Ujian Sekolah :",datas[data]["hasil ujian sekolah"])
		return True
	else:
		print("Data tidak ditemukan")
		return False

def tampilan_cari_siswa():
	system("cls")
	print("Pencarian Siswa")
	nama = input("Nama Siswa yang dicari : ")
	cari_siswa(nama)
	input("Tekan ENTER untuk kembali ke MENU")

def siswa_yang_keluar_dari_sekolah():
	system("cls")
	print("Menghapus Siswa Dari Data")
	nama = input("Nama Siswa yang dicari : ")
	result = cari_siswa(nama)
	if result:
		respon = input("Yakin dihapus (Y/N) : ")
		if respon.upper() == "Y":
			del datas[nama]
			print(f"Siswa {nama} telah dihapus.")
		else:
			print(f"Batal menghapus Siswa {nama}")
		input("Tekan ENTER untuk kembali ke MENU")

def edit_telp_kontak(data):
	print("INFORMASI YANG AKAN DIPERBAHARUI")
	print("DATA LAMA")
	print(f"Telp\t:{datas[data]['telp']}")
	new_telp = input("Masukkan Nomor Telp Baru : ")
	datas[data]["telp"] = new_telp
	print("Data berhasil diperbarui.")
	cari_siswa(data)

def edit_email_siswa(data):
	print("EMAIL YANG AKAN DIGANTI")
	print("EMAIL LAMA")
	print(f"email\t:{datas[data]}['email']")
	new_email = input("Masukkan email yang baru : ")
	datas[data]["email"] = new_email
	print("email berhasil diperbarui.")
	cari_nama(data)

def edit_alamat_siswa(data):
	print("ALAMAT YANG AKAN DIGANTI")
	print("ALAMAT LAMA")
	print(f"alamat\t:{datas[data]}['alamat']")
	new_hobi = input("Masukkan alamat yang baru : ")
	datas[data]["alamat"] = new_alamat
	print("alamat berhasil diperbarui.")
	cari_siswa(data)

def edit_nama_orangtua_siswa_kontak(data):
	print("NAMA ORANGTUA YANG AKAN DIGANTI")
	print("NAMA ORANGTUA YANG SALAH")
	print(f"nama orangtua\t:{datas[data]['nama orangtua']}")
	new_nama_orangtua = input("Masukkan nama orangtua yang baru : ")
	datas[data]["nama orangtua"] = new_nama_orangtua
	print("nama orangtua berhasil diperbarui.")
	cari_siswa(data)

def edit_asal_sekolah_kontak(data):
	print("ASAL SEKOLAH YANG AKAN DIGANTI")
	print("ASAL SEKOLAH YANG LAMA")
	print(f"asal sekolah\t:{datas[data]['asal sekolah']}")
	new_asal_sekolah = input("Masukkan asal sekolah yang baru : ")
	datas[data]["asal sekolah"] = new_asal_sekolah
	print("asal sekolah berhasil diperbarui.")
	cari_siswa(data)

def edit_hasil_ujian_sekolah_kontak(data):
	print("HASIL UJIAN YANG AKAN DIGANTI")
	print("HASIL UJIAN YANG LAMA")
	print(f"hasil ujian sekolah\t:{datas[data]['hasil ujian sekolah']}")
	new_hasil_ujian_sekolah = input("Masukkan hasil ujian sekolah yang baru : ")
	datas[data]["hasil ujian sekolah"] = new_hasil_ujian_sekolah
	print("hasil ujian sekolah berhasil diperbarui.")
	cari_siswa(data)

def edit_nama_kontak(data):
	print("INFORMASI YANG AKAN DIPERBAHARUI")
	print("DATA LAMA")
	print(f"Nama\t:{data}")
	new_nama = input("Masukkan Nama Baru : ")
	#copy data lama ke kontak baru, yang lama di hapus.
	datas[new_nama] = datas[data]
	del datas[data]
	print("Data berhasil dihapus")
	cari_siswa(new_nama)

def edit_info():
	system("cls")
	print("EDIT INFO KONTAK")
	nama = input("Nama Siswa yang akan di edit infonya : ")
	result = cari_siswa(nama)
	if result:
		print("EDIT [1]NAMA, [2]TELP [3]EMAIL, [4]ALAMAT, [5]NAMA ORANGTUA, [6]ASAL SEKOLAH, [7]HASIL UJIAN SEKOLAH")
		respon = input("Pilihan Informasi yg akan diedit (1/2/3/4/5/6/7) : ")
		if respon == "1":
			edit_nama_kontak(nama)
		elif respon == "2":
			edit_telp_kontak(nama)
		elif respon == "3":
			edit_email_kontak(nama)
		elif respon == "4":
			edit_alamat_kontak(nama)
		elif respon == "5":
			edit_nama_orangtua_siswa_kontak(nama)
		elif respon == "6":
			edit_asal_sekolah_kontak(nama)
		elif respon == "7":
			edit_hasil_ujian_sekolah_kontak(nama)
	input("Tekan ENTER untuk kembali ke MENU")

def cek_respon_siswa(char):
	if char == "A":
		penambahan_siswa()
	elif char == "B":
		lihat_seluruh_daftar_siswa()
	elif char == "C":
		tampilan_cari_siswa()
	elif char == "D":
		siswa_yang_keluar_dari_sekolah()
	elif char == "E":
		edit_info()
	elif char == "F":
		tentang_sekolah()
	else:
		print("INVALID RESPON")
		input("Enter to Back ... ")

def tentang_sekolah():
	system("cls")
	print("Nama Yang Membuat Sekolah Ignatius Global School")
	respon = input("Kamu Tahu Yang Punya Sekolah Siapa ? (Y/N) ")
	if respon.upper() == "Y":
		print("Ko Djony")
		print("Beliau Adalah Orang Yang Hebat Dan Cerdas loh ")
	else:
		print("Yah Jadi Gak Tahu Deh Siapa Yang Punya Sekolah.")
	input("Tekan ENTER untuk kembali ke MENU")

datas = {
	'Nicky' : {
		'telp' : '082285900099',
		'email' : 'allonzo.nicky@gmail.com',
		'alamat' : 'Soak Simpur',
		'nama orangtua' : 'popopop',
		'asal sekolah' : 'Ipeka',
		'hasil ujian sekolah' : 'bagus'
	},
	'Yohannes' : {
		'telp' : '081278199236',
		'email' : 'kamen.rider@gmail.com',
		'alamat' : 'Pasar Kuto',
		'nama orangtua' : 'kokko',
		'asal sekolah' : 'pppp',
		'hasil ujian sekolah' : 'bagus'
	}
}
user_respon = ""
while user_respon != "G":
	print_menu()
	user_respon = input("RESPON : ").upper()
	cek_respon_siswa(user_respon)


else:
	#sys.exit()
	system("cls")
	print("Sampai Jumpa Bro di Lain Hari Thxx ;)....")

#nambah nanya nama ortu dan asal sklh dan nilai rata" ujian sklh
