# نقوم ب اخذ رقم من المستخدم 
number = int(input("قم بكتابة رقم "))

# تقوم بعمل قائمة فيها عدة ارقام عشوائية و فيها الرقم الخاص ب المستخدم
numbers = [73, 13, 9, 22, number]

# الان نقوم بعمل شرط يتاكد من ان كان اكبر رقم يساوي الرقم اللذي كتبه المستخدم

if max(numbers) == number:
# سنقوم بطباعة ان المستخدم قام بكتابة اكبر رقم في القائمة
    print("لقد قمت باختيار اكبر رقم في القائمة")

# نقوم بعمل شرط else، ان كان المستخدم لم يقم بكتابة اكبر قيمة في القائمة
else:
    print("رقمك ليس الاكبر في القائمة")

# المخرجات
#>> قم بكتابة رقم
# سوف نقوم بكتابة 10 في اول مرة 
#>> رقمك ليس الاكبر في القائمة
# الان سوف نجرب بكتابة 105 في تاني مرة
#>> لقد قمت ب اختيار اكبر رقم في القائمة