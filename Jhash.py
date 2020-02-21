"""
Version 1.2.3

Changelog:
	convertFromColor() now works on all 6-character color codes


Last modified 08:36 14/02/2020

Created by Jaide Evans
"""

from random import randint

def encrypt(package,key): #Encrypts package using key
    """
    Returns a list of numbers based on the given key
    
    Inputs must only contain ASCII characters and is case-sensitive
    """
    keyAscii = []
    for char in key: #Converts key into ascii for encryption
        keyAscii.append(int(ord(char)))

    packageAscii = []
    for char in package: #Converts package into ascii for encryption
        packageAscii.append(int(ord(char)))
    
    encryptPackage = []
    num = 0
    for i in range(len(packageAscii)): #Mashes key and package together and spits out the encrypted data
        if num >= len(keyAscii):
            num = 0
        encryptPackage.append(packageAscii[i]+keyAscii[num])
        num += 1
    return encryptPackage

def decrypt(package,key):
    """
    Returns a decoded string based on given key
    
    Package MUST be a list; can be generated with Jhash.encrypt()
    """
    keyAscii = []
    for char in key: #Converts key into ascii for decryption
        keyAscii.append(int(ord(char)))

    decryptPackage = ""
    halfStep = []
    num = 0
    for i in range(len(package)): #Combs the encryption out of the data
        if num >= len(keyAscii):
            num = 0
        halfStep.append(package[i]-keyAscii[num])
        num += 1
    for i in halfStep: #Converts the data from ascii to text
        decryptPackage += chr(i)
    return decryptPackage

def randKey(length):
    """
    Returns a random series of characters as a string
    
    Length should be greater than 0
    
    Output is case sensitive!
    """
    randStr = ""
    for i in range(length):
        randStr += chr(randint(33,126)) #Generates a random typeable ascii character
    return randStr

def encryptKeyless(package):
    """
    Encrypts the package using the package as a key
    
    !! NOT SECURE !!
    """
    keyAscii = []
    for char in package: #Converts key into ascii for encryption
        keyAscii.append(int(ord(char)))

    packageAscii = []
    for char in package: #Converts package into ascii for encryption
        packageAscii.append(int(ord(char)))
    
    encryptPackage = []
    num = 0
    for i in range(len(packageAscii)): #Mashes key and package together and spits out the encrypted data
        if num >= len(keyAscii):
            num = 0
        encryptPackage.append(packageAscii[i]+keyAscii[num])
        num += 1
    return encryptPackage

def decryptKeyless(package):
    """
    Decrypts a keyless package
    
    Does not work on packages with custom keys
    """
    packageAscii = []
    for num in package:
        packageAscii.append(num/2)

    decryptPackage = ""
    for i in packageAscii: #Converts the data from ascii to text
        decryptPackage += chr(int(i))
    return decryptPackage

def convertColor(package,prefix="#",capital=False):
    """
    Converts encrypted list to #ffffff hex color format
    
    Prefix is added to the begining of each color code, default #

    List length does not need to be divisible by 3
    """
    convertPackage = []     #
    if len(package)%3 != 0: #
        package.append(255) #Makes the list of values divisible by 3
    if len(package)%3 != 0: #
        package.append(255) #
    
    for i in range(0, len(package), 3):         #Converts from ASCII to base 16
        hex1 = prefix+str(hex(package[i]))[2:]  #(the highest ASCII value is less than FF so color codes are safe)
        hex2 = str(hex(package[i+1]))[2:]       #
        hex3 = str(hex(package[i+2]))[2:]       #
        
        if capital:
            convertPackage.append(hex1.capitalize + hex2.capitalize + hex3.capitalize)
        else:
            convertPackage.append(hex1 + hex2 + hex3)

    return convertPackage

def convertFromColor(package):
    """
    Converts hex color codes to ASCII

    Prefixes are automatically removed

    package MUST be a list ['#ffffff', 'ffffff']
    """
    
    prefixless = []
    for i in package:   #Removes the prefix from each index
        if len(i) > 6:  #Prefix can be any length
            prefixless.append(i[-6:])
        else:
            prefixless.append(i)
    
    split = []
    for i in prefixless:    #Stores the base-10 values as variables to check their length
        value1 = int(i[0:2], base=16)
        value2 = int(i[2:4], base=16)
        value3 = int(i[4:6], base=16)

        if value1 < 62:             #Subtracts value
            value1 = 255 - value1   #from 255
        if value2 < 62:             #if it's
            value2 = 255 - value2   #lower than
        if value3 < 62:             #62 for
            value3 = 255 - value3   #compatability
        
        split.append(value1)    #appending each
        split.append(value2)    #value to
        split.append(value3)    #a list
    return split