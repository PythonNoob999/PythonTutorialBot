# اولا نقوم باخذ عمر المستخدم
age = int(input("قم بكتابة عمرك: "))

# سنقوم بعمل دالة مجهولة تاخد المعطي number، و تقوم بإرجاع المعطي number بزيادة 5
func = lambda number: number+5

# اخيرا نقوم بطباعة النتيجه للمستخدم
print("عمرك بعد 5 سنين هو ", func(age))

# المخرجات:
#>> قم بإدخال عمرك: 
# سنقوم بادخال 18 للتجربة
#>> عمرك بعد 5 سنين هو 23
