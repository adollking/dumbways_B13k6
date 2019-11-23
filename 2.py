 """ adollking(azzam)"""
def uangKembalian(harga,uang):
	kembalian = uang - harga
	kembalian1 = kembalian
	stokUang = [50000,20000,10000,5000,2000,1000,500]
	kembali = []
	for coin in stokUang:
		tahan = kembalian
		kembalian = kembalian//coin
		kembali.append(kembalian)
		kembalian = tahan %coin
	print('Uang kembalian adalah',kembalian1)
	print('pecahan uang  :')
	for i in range(len(stokUang)):
		if kembali[i] == 0:
			pass
		else:
			print(kembali[i],'x',stokUang[i])

uangKembalian(5000,100000)