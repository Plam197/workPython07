#--------- List คือ ข้อมูลหลายข้อมูล คนละชนิด ซ้ำกันได้ และมีลำดับ อีกทั้งแก้ไขได้ด้วย --------
                                    #  0     1   
         #   0   1   2     3    4        5
my_listl = [10, 20, True, 10, 'SAU', [20, 'IoT']]
         #   6   5    4    3    2         1       ติด - 

#การเช้าถึงข้อมูลใน List เพื่อเอาข้อมูลมาใช้ หรือแก้ไขคำข้อมูลให้มันใหม่
#เข้าถึงทีละข้อมูล
print(my_listl[4])  #SAU
print(my_listl[-2]) # SAU
print(my_listl[5]) # [20, 'IoT']
print(my_listl[-1]) # [20, 'IoT']
print(my_listl[5][1]) # IoT
print(my_listl[-1][-1]) # IoT

#เช้าถึงทีละหลายข้อมูล เราเรียกการ Slicing ผลลัพธ์จะเป็น List 
print(my_listl[1:4]) # 20, True, 10
print(my_listl[3:]) #10, 'SAU', [20, 'IoT']
print(my_listl[:3]) #10, 20, True

#เข้าถึงข้อมูล
for info in my_listl :
    print(info, end=',')

print()

print(my_listl)
my_listl[4] = 'Thailand'
print(my_listl)

# List Method
my_listl2 = [10, 20, True, 10, 'SAU', [20, 'IoT']]
my_listl2.append('Wow')
print(my_listl2)
my_listl2.append([111,222,333])
print(my_listl2)
my_listl2.extend([444,555])
print(my_listl2)
my_listl2.remove(10) #remove เอาออกตัวเดียวตัวเเรกที่เจอ
my_listl2.remove('SAU')
my_listl2.remove([111,222,333])
print(my_listl2)
my_listl2.pop()
my_listl2.pop()
my_listl2.pop()
print(my_listl2)
my_listl2.pop(2) # 2 คือ index
print(my_listl2)

# List Function -> len ( ), min( ), max( )
my_listl3 = [10, 20, 30, True]
print(len(my_listl3))
print(min(my_listl3))
print(max(my_listl3))
