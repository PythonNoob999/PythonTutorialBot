# نقوم بعمل متغير فيه قائمة فارغة
numbers = []
# نقوم بعمل حلقة while 
while True:
# نقوم بسؤال المستخدم عن رقم معين
    number = input("قم بكتابة رقم ")
# نتاكد من ان معطي المستخدم لا يساوي exit, و ان كان صحيح سوف نزيد الرقم في القائمة

    if number != "exit":
        numbers.append(int(number))
# نقوم بعمل شرط else يتحقق ان كان الشرط if غير صحيح، و يقوم ب الخروج من الحلقة

    else:
        break

# بعد ان نخرج من الحلقة نقوم بطباعة القائمة و مجموع اعدادها
print(numbers)
print(sum(numbers))

# المخرجات
#>> قم بكتابة رقم 
# هنا سنقوم بكتابة الاعداد 5, 8, 10، 12
# بعدها سنقوم بكتابة كلمة exit
#>> [5, 8, 10, 12]
#>> 35
