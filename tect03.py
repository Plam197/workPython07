#Primitive Data Typ
#Number , Boolean , String 

# Non-Primitive Data Type / Coollection / Data Structure 
# List , Tuple , Set , Dictionary 

# Data Type จะเอามาใช้กับการเขียนโปรแกรมในเรื่องของ ตัวแปร พารามิเตอร์ ฟังก์ เมธอี่ด

#--------- List คือ ข้อมูลหลายข้อมูล คนละชนิด ซ้ำกันได้ และมีลำดับ อีกทั้งแก้ไขได้ด้วย --------
         #   0   1   2     3    4        5
my_listl = [10, 20, True, 10, 'SAU', [20, 'IoT']]
         #   6   5    4    3    2         1       ติด - 

#--------- Tuple คือ ข้อมูลหลายข้อมูล คนละชนิด ซ้ำกันได้ และมีลำดับ แต่แก้ไขไม่ได้ --------
                 #   0   1   2     3    4        5
my_tuple1 = [10, 20, True, 10, 'SAU', [20, 'IoT']]
         #   6   5    4    3    2         1       ติด - 

#--------- Set คือ ข้อมูลหลายข้อมูล คนละชนิด ซ้ำกันไม่ได้ (ถ้าช้ำกันถือว่าเป็นตัวเดียวกัน) และไม่มีลำดับ และแก้ไขไม่ได้ แต่เพิ่ม ลบได้--------
my_Set1 = {10, 20, True, 10, 'SAU', (20, 'IoT')}

#--------- Dictionary คือ ข้อมูลหลายข้อมฃมูล ที่เป็น key:value แก้ไขได้ด้วย ไม่มีลำดับ ซ้ำได้ --------
# key เป็น String/Integer ส่วน value เป็นอะไรก็ได้
my_diction1 = {'name':'mod', 'age':30, 555:999, 'flag':True, 'wow':[10,20,30]}