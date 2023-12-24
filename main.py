import sys
def encry(filename, key):
	try:
		with open(filename, "r") as file:
			text = file.read()
			if len(text) >= 1:
				text = "+"+text
			else:
				text = "+ "
			print("content loaded.")
		newtext = ""
		for h, h2 in zip(text, range(len(text))):
			newtext += chr((ord(h)+key)%1114111)
			y = (h2/len(text))*100
			print(f"converting content... {y:.3f} %")
		print("writing encrypted content...")
		with open(filename, "w") as file:
			file.write(newtext[::-1])
		print("sucessfuly.")
	except Exception as e:
		print(f"error: {e}")
def decry(filename, key):
	try:
		with open(filename, "r") as file:
			text = file.read()[::-1]
			print("content loaded.")
		newtext = ""
		for h, h2 in zip(text, range(len(text))):
			newtext += chr((ord(h)-key)%1114111)
			y = (h2/len(text))*100
			print(f"converting content... {y:.3f} %")
		if newtext[0] == "+":
			print("sucessfuly decrypted <+>")
			print("writing decrypted content...")
			with open(filename, "w") as file:
				file.write(newtext[1:])
			print("sucessfuly.")
		else:
			print("key is not true <->")
	except Exception as e:
		print(f"error: {e}")
if len(sys.argv) >= 3:
	filename = sys.argv[2]
	print(f"selected filename>{filename}")
	if len(sys.argv) >= 4:
		try:
			key = int(sys.argv[3])
			print(f"selected key>{key}")
		except:
			key = 8888
			print("selected key>8888")
	else:
		key = 8888
	if sys.argv[1] == "en":
		encry(filename, key)
	elif sys.argv[1] == "de":
		decry(filename, key)
	else:
		print("unknow option error.")
elif len(sys.argv) >= 2:
	print("unknow using error.")
else:
	print("How to use EnSFile Encrypter (v1.0.0 Unicode Scroll):")
	print(" Options:\n  en=Encrypt\n  de=Decrypt\n How use with command:\n  command <option> <filename> <customKey(Optional)>\n Example Using:\n  command en text.txt\n  command de text.txt\n  command en text.txt 12345\n  command de text.txt 12345")
	quest = input("\nUse Manual? (Y/n): ").lower()
	try:
		if quest[0] == "y":
			option = input(f"Enter Option (en/de): ")
			filename = input(f"Enter Filename: ")
			quest2 = input(f"Use Custom Key? (Y/n): ").lower()
			try:
				if quest2[0] == "y":
					key = int(input("Enter Key (e.g. 12345): "))
				else:
					key = 8888
			except:
				key = 8888
				print(f"key set to 8888.")
			if option == "en":
				encry(filename, key)
			elif option == "de":
				decry(filename, key)
	except:
		pass
