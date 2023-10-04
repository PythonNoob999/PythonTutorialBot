# نقوم بعمل المتغييرين
password1 = 12345
password2 = 12344

# نقوم بعمل متغير فيه كلمة السر المطلوبة
password = 12345
# نقوم بعمل متغير فيه حالة الدخول الناجح
access = False

# نطابق المتغير الاول
if password1 == password:
    access = True

print(access) 
>> True

# نطابق المتغير التاني

if password2 == password:
    access = False

print(access)
