#!/usr/bin/env python

refString  = "From a seed a mighty trunk may grow.\n"
refOffset = "01111101001000101000000111101001001011111110010011100111010011000010101101110110100001101011100101001110000000001101000110001011011010101001000000010010001100011001100011001011010101111011110110001100101100101000110011101111101101000110110010101001100100110100010101101111101111011001100011111101"


def revere_sub_400B5D(myString, ref):
	result = ""

	for i in range(0, len(myString)):
		
		#print "my: " + myString[i] + " ref[i]: " + ref[i]
		
		if (myString[i] == "1"):
			result = result + ref[i]
		elif (myString[i] == "0" and ref[i] == "1"):
			result = result + "0"
		elif (myString[i] == "0" and ref[i] == "0"):
			result = result + "1"
		else:
			print "ERREUR"
	
	return result


def bruteForce_sub_400C02(myString):
	finalString=""
	for j in myString:
		for i in range(0,256):
			
			result = sub_400C02(format(i, '08b'))

			if chr(result) == j:
				#print "Valeur teste: " + format(i, '08b') + " resultat: " + chr(result)
				finalString = finalString + format(i, '08b')

	return finalString


def sub_400C02(myString):
	char = 0;
	for j in range(0,8):
		#char = finalString + chr(j + result[8*i] + 2 * finalString) -48
		char = ord(myString[j]) + 2 * char - 48
	#print char
	return char	

def reverse_gmpz(val,length):
	finalString=""
	v16 = val
	for i in range(0,length):
		s = (v16 % 307)
		finalString = finalString + chr(s)
  		v16 = v16 - s;
  		v16 = v16 / 307;

  	finalString = finalString[::-1]
  	return finalString

def gmpz(myStr):
	result = 0
	for c in myStr:
		result = result * 307 
		result = result + ord(c)
  	#print format(result, 'b')
  	return format(result, 'b')

if __name__ == "__main__":

	print "\n\n\n"
	print "*********************************************************************************"
	print "** [SwissMadeSecurity] Write-up of interstellar reverese engineering challenge **"
	print "*********************************************************************************"
	print "\n"

	result_sub_400C02 = bruteForce_sub_400C02(refString)
	print "Result for bruteForce_sub_400C02:\n" + result_sub_400C02
	print "\n"
	result_sub_400B5D = revere_sub_400B5D(result_sub_400C02, refOffset)
	print "Result for reverse_sub_400B5D:\n" + result_sub_400B5D
	print "\n"
	result_reverse_gmpz = reverse_gmpz(int(result_sub_400B5D,2),len(result_sub_400B5D))
	print "Result for reverse_gmpz:\n" + result_reverse_gmpz
	print "\n"