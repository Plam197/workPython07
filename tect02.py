# character in string has index number
       #01234567890123
infoA = 'Hello SAU 2003'
       #43240987654321 ติด -

print(infoA[6])
print(infoA[-8])

#เข้าถึงตัวอักษรหลายๆ ตัวใน String เราจะใฃ้วิธี Slicing ด้วย index number
# SAU
print(infoA[6:9])
print(infoA[-8:-5])

# o SAU 20 
print(infoA[4:12])

# String Nethod
print( infoA.upper() )
print( infoA.lower() )
print( infoA.capitalize() )
print( infoA.count('1'))
print( infoA.isdigit() )
print( infoA.islower() )
infoB = infoA.replace('SAU', 'Iot')
print(infoA)
print(infoB)
print(infoB.replace('Hello', 'Hi....'))
print(infoB.replace('hell', 'Hi...'))

# String String
print(len(infoA))

print('SAU',35,end='') # SAU 35
print('SAU'+str(35)) #SAU35
print('SAU',35,sep='') #SAU35
print('20','02','2023',sep='/') 
print(20,'มกราคม',2023,sep='-') 