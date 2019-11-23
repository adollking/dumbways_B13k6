diskon1 = 20000
diskon2 = 40000


a =  "anda mendapat diskon DumbWaysAsik : 20000"
b = "anda mendapat diskon DumbWAysMantap : 40000"
input = int(input ("masukan uang anda : "))
print ("yang anda masukan" , input) 
msk =input 
if input < 20000:
	print ("anda tidak mendapatkan diskon")
else:
	if input >= 50000:
		diskon = input * 0.30
		if diskon <= 40000:
			hasil = msk - diskon
			print (" anda mendapat diskon DumbWAysMantap : " , diskon)
		else :
			hasil = msk - diskon2
			print (b)	
		print (" uang yang harus dibayar : " , hasil)
	elif input >= 20000 :  
		diskon = input *0.50
		if diskon <= 20000:
			hasil = msk - diskon 
			print ("anda mendapat diskon DumbWaysAsik : ", diskon)
		else : 
			hasil = msk - diskon1,print (a)
		print (" uang yang harus dibayar : " , hasil)
	else :
		print ("anda tidak mendapatkan diskon")
	
