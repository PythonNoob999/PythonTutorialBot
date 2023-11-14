from pyrogram.types import (
InlineKeyboardMarkup as Markup,
InlineKeyboardButton as Button,
ReplyKeyboardMarkup as RMarkup
)

BACK = Button("↩️Back", callback_data="back")

msg = {
"template-ar": '''
**••{}••**

**•تعريف بسيط💬•**
**{}**

**•طريقة الكتابة⌨️•**
`{}`

**•مثال للاستعمال❓•**
**{}**

**مثال📟:**
```python
{}
```
[GitHub](https://github.com/PythonNoob999/PythonTutorialBot/blob/master/examples/{})📒
''',
"template-en": '''
**••{}••**

**•Short Description 💬•**
**{}**

**•Syntax⌨️•**
`{}`

**•Usage Example❓•**
**{}**

**Example📟:**
```python
{}
```
[GitHub](https://github.com/PythonNoob999/PythonTutorialBot/blob/master/examples/{})📒
''',
"start-en": """
Welcome in your **Journey Helper** for learning python🗂

you can start exploring by pressing one of those **Buttons** under the message
""",
"start-ar": """
اهلا بك في **مساعدك في الرحلة** لتعلم البايثون

لتبدأ التعلم قم بضغط **زر** من الازرار الاتية
""",
"variables-en": '''
••**Variables📒**••

**•Short Description💬•**
**Variables serve as a container**, They can contain aka "store" values inside of them

**•Syntax⌨️•**
`variable_name = DataType`

**•Usage Example❓•**
**We can use variables to store values inside of them to use it later on**

**Example📟:**
```python
number = 5
print(number*2)
>> 10
```
[GitHub](https://github.com/PythonNoob999/PythonTutorialBot/blob/master/examples/variables_en.py)📒
''',
"variables-ar": '''
**••المتغيرات📒••**

**•تعريف بسيط💬•**
**المتغيرات تتصرف كحاويات**, تستطيع تخزين جميع انواع البيانات داخل المتغيرات

**•طريقة الكتابة⌨️•**
`# اسم المتغير = اي نوع بيانات
variable_name = DataType`

**•مثال للاستعمال❓•**
**نستطيع استخدام المتغيرات لتخزيين قيم بداخلها لاستخدامها في وقتآ لاحق**

**مثال📟:**
```python
# هنا نقوم بعمل متغير ب قيمة 5 و طباعته x 2
number = 5
print(number*2)
>> 10
```
[GitHub](https://github.com/PythonNoob999/PythonTutorialBot/blob/master/examples/variables_ar.py)📒''',
"data_types-ar": "قم بأختيار نوع البيانات",
"data_types-en": "Choose DataType",
"data_types-str-ar": '''
**••البيانات النصية str••**

**•تعريف بسيط💬•**
**نوع البيانات str هو نوع البيانات "النصية" تستخدم في عمليات كثيرة و اغلب استخدامتها للتواصل مع المستخدم**

•طريقة الكتابة⌨️•
`# هنا نقوم بطباعة جملة Hello World! في الشاشة باستخدام امر الطباعة

print("Hello World!")
`

**•مثال للاستعمال❓•**
**البيانات النصية تدخل في كثير من الاستخدامات، مثل طباعة كلمات في الشاشة، تخزين معلومات مستخدم ك الاسم و الباسورد**

**مثال📟:**
```python
user_name = "Ahmed"
password = "12345abc"
```
[GitHub](https://github.com/PythonNoob999/PythonTutorialBot/blob/master/examples/data_types_str_all.py)📒
''',
"data_types-str-en": '''
**••String data type••**

**•Short description💬•**
**String can be used to refer to a "text" value**

**•Syntax⌨️•**
`print("Hello World!")`

**•Usage Example❓•**
**We can use strings to store a user name and password**

**Example📟:**
```python
user_name = "Jack"
password = "12345abc"
```
[GitHub](https://github.com/PythonNoob999/PythonTutorialBot/blob/master/examples/data_types_str_all.py)📒
''',
"data_types-int-ar": '''
**••البيانات الرقمية Int••**

**•تعريف بسيط💬•**
**البيانات الرقمية int تستخدم في اغلب الاوقات، ف تخزين بيانات/اجراء عمليات حسابية/انشاء خورازميات التشفير**

**•طريقة الكتابة⌨️•**
`intvar = 10`

**•مثال للاستعمال❓•**
**يمكن استخدام البيانات الرقمية لمعرفة زاوية ناقصة في مثلث**

**مثال📟:**
```python
# نقوم بعمل متغيرين فيهم اول زاويتين
Angle1 = 70
Angle2 = 80
# نقوم بجمع المتغيرين و نطرحهم من 180
print("Third angle is ", (Angle1+Angle2)-180, " Degrees°")
>> Third angle is 30 Degrees°
```
[GitHub](https://github.com/PythonNoob999/PythonTutorialBot/blob/master/examples/data_types_int_ar.py)📒
''',
"data_types-int-en": '''
**••Int Data Type••**

**•Short Description 💬•**
**Int refers to numerical data, can be used in data_science/hashing algorithms/data analyst**

**•Syntax⌨️•**
`intvar = 10`

**•Usage Example❓•**
**We can use INT to calculate the missing angle of a triangle**


**Example📟:**
```python
Angle1 = 80
Angle2 = 70
print("Third angle is ", (Angle1+Angle2)-180, " Degrees°")
>> Third angle is 30 Degrees°
```
[GitHub](https://github.com/PythonNoob999/PythonTutorialBot/blob/master/examples/data_types_int_en.py)📒
''',
"data_types-float-ar": '''
**••البيانات العشرية Float••**

**•تعريف بسيط💬•**
**البيانات العشرية Float هي ترمز للاعداد اللتي بها ارقام عشرية، تستخدم في العمليات التي تحتاج دقة كبيرة للغاية**

**•طريقة الكتابة⌨️•**
`Floatvar = 1.532`

**•مثال للاستعمال❓•**
**يمكننا حسابة مؤشر كتلة الجسم (BMI) بدقة كبيرة**

**مثال📟:**
```python
# نقوم بتعريف متغيرين فيهم الوزن و الطول

height = 5.9
weight = 160.74

# نقوم بحسابة مؤشر كتلة الجسم (BMI)
bmi = weight / (height**2)
 
# نقوم بطباعة مؤشر كتلة الجسم (BMI)
print("Your bmi is ", bmi)
>> Your bmi is 4.61763861
```
[GitHub](https://github.com/PythonNoob999/PythonTutorialBot/blob/master/examples/data_types_float_ar.py)📒
''',
"data_types-float-en": '''
**••Float Data Type••**

**•Short Description 💬•**
**Float is a Double numerical data type, it's used in Micro operations and calculation that need to be specific**

**•Syntax⌨️•**
`Floatvar = 1.532`

**•Usage Example❓•**
**It can be used to calculate the body BMI accurately**

**Example📟:**
```python
# We declare height & weight in float variables

height = 5.9
weight = 160.74

# we calculate the BMI
bmi = weight / (height**2)
 
# now we print the bmi
print("Your bmi is ", bmi)
>> Your bmi is 4.61763861
```
[GitHub](https://github.com/PythonNoob999/PythonTutorialBot/blob/master/examples/data_types_float_en.py)📒
''',
"data_types-bool-ar": '''
**••المنطقية Boolean••**

**•تعريف بسيط💬•**
**البيانات المنطقية Boolean، و اللذي هي عبارة عن True, False او صحيح و خطأ، و هي ترمز ل قيمة صحيحة 1 او خاطئة 0**

**•طريقة الكتابة⌨️•**
`Boolvar = True`

**•مثال للاستعمال❓•**
**سنقوم بعمل متغيرين رقميين، و سنتأكد ان الرقمين مطابقين لباسورد معين، و ان كانو متطابقين، سنغير قيمة المتغير اللتي فيها النتيجه الي True، تعني صحيحة، او False، يعني خاطئة إذا كان الباسورد غير متطابق**

**مثال📟:**
```python
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
>> False
```
[GitHub](https://github.com/PythonNoob999/PythonTutorialBot/blob/master/examples/data_types_bool_ar.py)📒
''',
"data_types-bool-en": '''
**••Boolean Data Type••**

**•Short Description 💬•**
**Boolean data types can either represent True or False, aka 1 or 0**

**•Syntax⌨️•**
`Boolvar = True`

**•Usage Example❓•**
**We can make 2 int vars that have 2 passwords, and match it with the correct password, and make a result var and change it to True, if the var is identical to the password else we will but a default value to False**

**Example📟:**
```python
# we make the 2 passwords vars
password1 = 12345
password2 = 12344

# we make a var for the main password
password = 12345

# we make a Boolean var to store the access status

access = False

# We match the first password
if password1 == password:
    access = True

print(access) 
>> True

# We match the second password

if password2 == password:
    access = False

print(access)
>> False
```
[GitHub](https://github.com/PythonNoob999/PythonTutorialBot/blob/master/examples/data_types_bool_en.py)📒
''',
"data_types-list-en": '''
**••Array/List []••**

**•Short Description 💬•**
**Arrays aka Lists in python can be used to store multiple value's inside of it, it can store all data types also**

**•Syntax⌨️•**
`Listvar = [1, "1", 1.5, False]`

**•Usage Example❓•**
**We can use lists to store fruits, and printing them by the "index"**

**Example📟:**
```python
fruits = ["Apple", "Kiwi", "Banana"]
# indexing starts at 0 in most programming languages

print(fruits[0])
>> Apple

# you can also use negative indexes, wich will give you opposite result

print(fruits[-1]) # last item
>> Banana

print(fruits[-2]) # the item before the last one

>> Kiwi
fruits[0] = "Orange" # we can even change it's values
print(fruits)
>> ["Orange", "Kiwi", "Banana"]
```
[GitHub](https://github.com/PythonNoob999/PythonTutorialBot/blob/master/examples/data_types_list_en.py)📒
''',
"data_types-list-ar": '''
**••القوائم []••**

**•تعريف بسيط💬•**
**نستطيع استخدام القوائم لتخزين اي نوع بيانات داخلها و البحث عنهم عن طريق رقم المكان**

**•طريقة الكتابة⌨️•**
`Listvar = [1, "Hello", 1.232, False]`

**•مثال للاستعمال❓•**
**نستطيع تخزين قائمة من الفواكه و طباعتهم ب استخدام رقم المكان**

**مثال📟:**
```python
fruits = ["Apple", "Kiwi", "Banana"]
# رقم المكان يبدا ب 0 في اغلب اللغات البرمجية

print(fruits[0])
>> Apple

# يمكنك ايضا استخدام قيم سالبة و اللتي ستعطيك نتائج مختلفة

print(fruits[-1]) # اخر مكان
>> Banana

print(fruits[-2]) # المكان ما قبل الاخير

>> Kiwi
fruits[0] = "Orange" # نستطيع ايضا تغير قيمة معينة في القائمة
print(fruits)
>> ["Orange", "Kiwi", "Banana"]
```
[GitHub](https://github.com/PythonNoob999/PythonTutorialBot/blob/master/examples/data_types_list_ar.py)📒
''',
"data_types-tuple-en": '''
**••Tuples ()••**

**•Short Description 💬•**
**Tuples is similar to lists it's also used to store value's, but it's IMMUTABLE, that means you can't change it's values**

**•Syntax⌨️•**
`Tuplevar = (1, "Hello", 1.343, False)`

**•Usage Example❓•**
**We also can use the tuples like the lists, but this time we are dealing with unchangeable data!**

**Example📟:**
```python
# Creating a tuple with fruits
fruits = ("Apple", "Kiwi", "Banana")

# we can also print it's values with indexing

print(fruits[0])
>> Apple

# and also use negative indexing
print(fruits[-1]) 
>> Banana

# but unlike lists[], you can't change it's data

fruits[0] = "Orange"
>> TypeError: "str" object does not support item assignment❗️
```
[GitHub](https://github.com/PythonNoob999/PythonTutorialBot/blob/master/examples/data_types_tuple_en.py)📒
''',
"data_types-tuple-ar": '''
**••المترابطة ()••**

**•تعريف بسيط💬•**
**نوع البيانات المترابطة هي مثل القوائم، لكن عكس القوائم لا يمكنك تغيير قيمها الموجودة**

**•طريقة الكتابة⌨️•**
`Tuplevar = (1, "Hello", 1.243, False)`

**•مثال للاستعمال❓•**
**نستطيع استخدام المترابطات مثل القوائم، لكن هذه المرة لا يمكننا تغير قيمها**

**مثال📟:**
```python
# نصنع مترابطة بها القيم
fruits = ("Apple", "Kiwi", "Banana")

# نقوم بطباعة عناصرها ايضا ب استخدام رقم المكان

print(fruits[0])
>> Apple

# ايضا نستطيع استخدام ارقام سالبة
print(fruits[-1]) 
>> Banana

# لكن عكس القوائم، سنحصل علي خلل عند تغير قيمة بداخلها

fruits[0] = "Orange"
# خطأ، نوع البيانات النصية لايدعم تبادل القيم

>> TypeError: "str" object does not support item assignment❗️
```
[GitHub](https://github.com/PythonNoob999/PythonTutorialBot/blob/master/examples/data_types_tuple_ar.py)📒
''',
"data_types-dict-en": '''
**••Dictionary {}••**

**•Short Description 💬•**
**dictionary like list and tuple is used to store value's inside of them, but this you use key's instead of index to get a value from it!**

**•Syntax⌨️•**
`Dictvar = {
"key": "value", # key = value

"Bitcoin": "26500$", # bitcoin = 26500$

"Ahmed": {"age": 20}, # Ahmed = {"age": 20}

}`

**•Usage Example❓•**
**We can use dictionary's to list a fruits and it's price per kilo**

**Example📟:**
```python
# We make a price dictionary
fruits = {
"Apple": 3,
"Kiwi": 9,
"Banana": 4
}

# We can print fruit price by using it's name aka "key" as index

print(fruits["Kiwi"], "$")
>> 9$

# We can also change a fruit price
fruits["Banana"] = 2
print(fruits["Banana"], "$")
>> 2$

# And of course that well change the dictionary totally
print(fruits)
>> {
"Apple": 3,
"Kiwi": 9,
"Banana": 2
}
```
[GitHub](https://github.com/PythonNoob999/PythonTutorialBot/blob/master/examples/data_types_dict_en.py)📒
''',
"data_types-dict-ar": '''
**••Dictionary {}••**

**•تعريف بسيط💬•**
**نستطيع استخدام ال dictionary لتخزين البيانات مثل القوائم و المترابطات، لكن هذه المرة سنستخدم نظام
 مفتاح=قيمة
 بدلا من
 رقم المكان=قيمة 
لنحصل علي القيمة منها!**

**•طريقة الكتابة⌨️•**
`Dictvar = {
"مفتاح": "قيمة", # مفتاح=قيمة

"بيتكوين": "26500$", # بيتكوين= 26500$

"احمد": {"العمر": 20} # احمد = {"العمر": 20}

}`

**•مثال للاستعمال❓•**
**نستطيع بتخزين قائمة من اسعار الفواكه بالكيلو داخل dictionary**

**مثال📟:**
```python
# اولا نقوم بصناعة قائمة الاسعار
fruits = {
"تفاح": 3, # تفاح = 3$
"كيوي": 9, # كيوي = 9$ 
"موز": 4 # موز = 4$
}

# الان تستطيع طباعة سعر الفاكهة ب استخدام اسمها بدلآ من رقم مكانها في القائمة

print(fruits["كيوي"], "$")
>> 9$

# تستطيع ايضا تغير سعر الفاكهة!

fruits["موز"] = 2
print(fruits["موز"], "$")
>> 2$

# و هذا طبعا سيقوم بتغيير القائمة كليا

print(fruits)
>> {
"تفاح": 3,
"كيوي": 9,
"موز": 2
}
```
[GitHub](https://github.com/PythonNoob999/PythonTutorialBot/blob/master/examples/data_types_dict_ar.py)📒
''',
"functions-ar": '''
**••الدوال••**

**•تعريف بسيط💬•**
**الدالة هي عبارة عن مجموعة من العمليات التي نستطيع استخدامها ف وقت لاحق بمجرد مناداة الدالة و ستقوم بعمل العمليات المطلوبة و يمكنها اعادة قيمة لاستخدامها**

**•طريقة الكتابة⌨️•**
`# سنقوم بعمل دالة ب اسم function_name، و سوف نجعلها تستقبل معطيين ب اسم param1, param2

def function_name(param1, param2):
    #code`

**•مثال للاستعمال❓•**
**نستطيع عمل دالة لمعرفة الزاوية الناقصة في المثلث عن طريق اعطائها اول زاويتين**

**مثال📟:**
```python
# تقوم ب انشاء الدالة و جعلها تستقبل Angle1, Angle2

def third_angel(Angel1, Angel2):
#نقوم بمجمع الزاوية الاولي و التانية و وضعها في متغير
    Angels = Angel1+Angel2

#نقوم بجلب الزاوية التالته، عن طريق طرح الزاويتين من 180

    Angle3 = 180-Angels
    return Angle3

# نقوم بتجربة الدالة ب الزوايا a و b، و وضع النتيجه ف متغير
a = 70
b = 60
c = third_angel(a, b)

# نقوم بطباعة الزاوية الثالثة

print(c, " درجة")
>> 50 درجة
```
[GitHub](https://github.com/PythonNoob999/PythonTutorialBot/blob/master/examples/functions_ar.py)📒
''',
"functions-en": '''
**••Functions••**

**•Short Description 💬•**
**a function is a set of instructions that we can use multiple times instead of typing the same instructions every time we need it, a function can also return a Value so we can use it**

**•Syntax⌨️•**
`# we will make a function with the name "function_name" and make it take 2 parameters, param1 and param2

def function_name(param1, param2):
    #code`

**•Usage Example❓•**
**We can make a function that calculate the third angel of a triangle by giving it the first 2 angels as parameters**

**Example📟:**
```python
# we make a function that takes the first angle and the second angle

def third_angle(Angle1, Angle2):
# we make a variable that has the sum of the 2 Angles

    Angles = Angle1+Angle2

# we calculate the third angle by substracting 180 from Angle1+Angle2

    Angle3 = 180-Angles

# we return the third_angle
    return Angle3

# we try using the function with angles 1 and 2
a = 70
b = 60
c = third_angle(a, b)

# we print the third angle
print(c, " Degrees")
>> 50 Degrees
```
[GitHub](https://github.com/PythonNoob999/PythonTutorialBot/blob/master/examples/functions_en.py)📒
''',
"loops-ar": "اختر نوع الحلقة",
"loops-en": "Choose loop",
"loops-while-ar": '''
**••الحلقة While ➿••**

**•تعريف بسيط💬•**
**الحلقة المتكررة while، تقوم بتكرير عملية معينه طالما الشرط الخاص بها لم يتحقق، بعدها تقوم بكسر الحلقة و تكملة البرنامج**

**•طريقة الكتابة⌨️•**
`# هنا نقوم بعمل while و يكون الشرط الخاص بها هو condition، و سنقوم بعمل عملية تحتها ب اسم code

while condition:
    #Code`

**•مثال للاستعمال❓•**
**نستطيع تعيين متغير ب اسم المستخدم، 
و تعيين متغير ب مرات طباعة اسم المستخدم
و سنقوم بعمل شرط بان طالما عدد مرات الطباعة اقل من عدد المرات اللذي نريدها، سيقوم بزيادة عدد الطباعات**

**مثال📟:**
```python
# نقوم بتعين الاسم و عدد مرات الطباعة
name = "احمد"
number = 4

# سنقوم بتعيين متغير و نخزن فيه كم مرة قام فيها البرنامج ب الطباعة

printed = 0

# سنقوم بعمل حلقة while و شرطها ان تتأكد في كل مرة ان عدد المرات اللتي تم طباعتها اقل من العدد الذي نريده، و اذا تحقق الشرط نطبع الاسم،. ونقوم بزيادة عدد المرات اللتي تم طباعتها ب 1

while printed < number:
    print("اسمك هو ", name)
    printed = printed + 1

# سنقوم في النهاية ب طباعة ان الحلقة قد انتهت
print("تم الانتهاء")

# المخرجات:
>> اسمك هو احمد
>> اسمك هو احمد
>> اسمك هو احمد
>> اسمك هو احمد
>> تم الانتهاء
```
[GitHub](https://github.com/PythonNoob999/PythonTutorialBot/blob/master/examples/loops_while_ar.py)📒
''',
"loops-while-en": '''
**••While loop ➿••**

**•Short Description 💬•**
**the while loop will repeat a block of code or instructions, while it's condition is True, otherwise it will break from itself and continue the program**

**•Syntax⌨️•**
`# here we make a while loop with condition named "condition" and we will execute code on it

while condition:
    #code`

**•Usage Example❓•**
**We can make a simple program
we but a name in a variable, and the number of times we want our name to be printed in another variable

and we will make a variable that we will use to store the number of times we already printed the name to but it in the while condition**

**Example📟:**
```python
# we make name and number variables

name = "Jack"
number = 4

# we make a variable to store the amount of time we printed the name

printed = 0

# we will make a while loop that will check if the printed time's is less than the number we want to print, if it's condition is True, the loop will print the name and increase the printed variable by 1

while printed < number:
    print("Your name is: ", name)
    printed = printed + 1

# we will print that the program finished outside the while loop, so this command will execute when the while loop is finished

print("Done")

# OUTPUT:
>> Your name is Jack
>> Your name is Jack
>> Your name is Jack
>> Your name is Jack
>> Done
```
[GitHub](https://github.com/PythonNoob999/PythonTutorialBot/blob/master/examples/loops_while_en.py)📒
''',
"loops-for-ar": '''
**••حلقة for ➿••**

**•تعريف بسيط💬•**
**حلقة for، تستخدم للمرور علي عناصر قائمة/نص (str) و العديد من انواع البيانات، و تكرر عمليه معينه باستخدام العنصر اللذي في الدور الحالي**

**•طريقة الكتابة⌨️•**
`# هنا نقوم بعمل قائمة و نعمل حلقة for للمرور علي كل عناصرها, و في كل عنصر سنقوم بطباعته

list = [1, 2, 3, 4]

for item in list:
    print(item)

# المخرجات:
>> 1
>> 2
>> 3
>> 4`

**•مثال للاستعمال❓•**
**نستطيع استخدام حلقة for، لعمل برنامج بسيط
يقوم ب المرور علي عناصر قائمة رقمية int، و يقوم بطباعة الرقم في نفسه**

**مثال📟:**
```python
# نقوم بعمل قائمة للتجريب عليها
lst = [2, 6, 9, 12]

# نقوم ب المرور علي عناصر القائمة و نقوم بطباعة كل عنصر في نفسه

for number in lst:
    print(number*number)

# سنقوم بطباعة ان البرنامج انتهي بعد تنفيذ الحلقة
print("انتهي البرنامج")
# المخرجات:
>> 4
>> 36
>> 81
>> 144
>> انتهي البرنامج
```
[GitHub](https://github.com/PythonNoob999/PythonTutorialBot/blob/master/examples/loops_for_ar.py)📒
''',
"loops-for-en": '''
**••for loop➿••**

**•Short Description 💬•**
**a for loop is used to iterate over all the items of a list/str/and alot more, item by item, and making opreations with it, until the source that we iterate over him ends**

**•Syntax⌨️•**
`# we will make a list of number and iterate over every item one by one ans print it

list = [1, 2, 3, 4]

for item in list:
    print(item)

# OUTPUT:
>> 1
>> 2
>> 3
>> 4`

**•Usage Example❓•**
**we can make a simple program, that takes a list contains multiple int value's, and simply print the number times itself**

**Example📟:**
```python
# we make the list we want to test with

lst = [2, 6, 9, 12]

# we iterate over every number and prints it times itself

for number in lst:
    print(number*number)

# we print that the program has ended after we finish executing the for loop

print("Finished")

# OUTPUT:
>> 4
>> 36
>> 81
>> 144
>> Finished
```
[GitHub](https://github.com/PythonNoob999/PythonTutorialBot/blob/master/examples/loops_for_en.py)📒
''',
"if_else-ar": '''
**••if-elif-else الشرطية••**

**•تعريف بسيط💬•**
**نستخدم if-elif-else نقوم بوضع شرط معين ب استخدام ifو اذا كان هذا الشرط صحيح سوف نقوم بتنفيذ مجموعة من العمليات، و نقوم بوضع شرط بديل للشرط الاول اذا كان للاول غير صحيح ب استخدام elif، و اخيرا نقوم ب استخدام else، لتحقيق كود معين اذا كانت جميع الشروط التي فوقها غير صحيحة**

**•طريقة الكتابة⌨️•**
```python
# هنا نقوم بعمل شرط if، يتاكد من ان المتغير number قيمته تساوي 3، و سيقوم بطباعة انه يساوي 3

number = 3
if number == 3:
    print("المتغير يساوي 3")
# المخرجات:
>> المتغير يساوي 3

# هنا نقوم بعمل نفس الشرط لكن سيكون المتغير ب قيمه 2 هذه المره، و سنضع شرط else يقوم بتحقيق كود اذا كانت كل الشروط التي اعلاه غير صحيحة

number = 2
if number == 3:
    print("المتغير يساوي 3")
else:
    print("المتغير لا يساوي 3")

# المخرجات:
>> المتغير لا يساوي 3

# هنا نقوم بعمل نفس العمليات لكن هذه المرة سنضع شرط elif، يقوم بمراقبة الشرط الاول if و ان كان شرط if غير صحيح لكن شرطه هو صحيح، سيقوم بطباعة ان قيمة المتغير تساوي 2، لكن طبعا ان كان شرط if و elif كلاهما غير صحيح

number = 2
if number == 3:
    print("المتغير يساوي 3")

elif number== 2:
    print("المتغير يساوي 2")

else:
    print("المتغير لا يساوي 3")

# المخرجات:
>> المتغير يساوي 2

# معلومة❗️، يمكنك وضع العديد من الشروط الجانبية elif كما تريد، لكن شرطا مهم ان يكون اول شرط if، مثال:

number = 2
if number == 1:
    print(number)
elif number == 2:
    print(number)
elif number == 3:
    print(number)
else:
    print("Unkown")
```

**•مثال للاستعمال❓•**
**نستطيع عمل برنامج بسيط يقوم ب اخد عمر المستخدم

ان كان اكبر من 18 سيطبع ان مسموح له بالدخول 
ان كان يساوي 18 سيطبع له ان يحاول السنة القادمة
ان كان اقل من 18 سيطبع له انه صغير علي الخدمة**

**مثال📟:**
```python
# نقوم باخد عمر المستخدم 
age = int(input("قم بكتابة عمرك: "))
# نقوم بالتاكد انه اكبر من 18 سنة و سيقوم بطباعة ان الدخول مسموح
if age > 18:
    print("تستطيع استخدام الخدمة")

# ان لم يكن اكبر من 18، نتاكد من ان عمره يساوي 18 لتذكيره ب التسجيل السنه القادمة

elif age == 18:
    print("يجب ان تكون اكبر من 18 سنة!، حاول السنة القادمة")

# اذا كان المستخدم ليس اكبر من 18 ولا يساوي 18، نقوم بطباعة انه صغير علي استخدام الخدمة
else:
    print("لا تستطيع استخدام الخدمة")

# المخرجات
>> قم بكتابة عمرك
# سوف نقوم بكتابة 19 للتجربة
>> تستطيع استخدام الخدمة

# سوف نقوم بكتابة 17 هذه المرة
>> لا تستطيع استخدام الخدمة

# اخيرا سوف نجرب كتابة 18
>> يجب ان تكون اكبر من 18 سنة!، حاول السنة القادمة
```
[GitHub](https://github.com/PythonNoob999/PythonTutorialBot/blob/master/examples/if_else_ar.py)📒
''',
"if_else-en": '''
**••If-elif-else statements••**

**•Short Description 💬•**
**we use if-elif-else to put a condition and check if it True, and if it's True the condition will run some opreations or code

we use if to check if a condition is correct

we use elif to check the if/elif statement above it, if it's not correct, it will check it's condition, and if it's condition is True it will do some opreations or code 

we use else to check if all the if/elif statements above it all conditions are not correct, then the else will do some opreations or code**

**•Syntax⌨️•**
`# here we make a if statment to check if the variable number value is 3, then i lt will print that the variable is equal to 3

number = 3
if number == 3:
    print("the variable is equal to 3")

# OUTPUT:
>> the variable is equal to 3

# here we make the exact code, but this time we will add an else statment and change the number variable value to 2, it will check if the all the  conditions above it is not correct, then it will print variable does not equal to 3

number = 2
if number == 3:
    print("the variable is equal to 3")
else:
    print("the variable does not equal to 3")

# OUTPUT:
>> the variable does not equal to 3

# now we make the same code but this time we will add an elif statement, it will check if the condition above it is correct, if not, it will print that the variable is equal to 2

number = 2
if number == 3:
    print("the variable is equal to 3")
elif number == 2:
    print("the variable is equal to 2")
else:
    print("the variable does not equal to 3")

# OUTPUT:
>> the variable is equal to 2

# Additional information❗️, we can put as much as elif statements as we want, but the first condition must be a if statment

number = 2
if number == 1:
    print(number)
elif number == 2:
    print(number)
elif number == 3:
    print(number)
else:
    print("Unkown")`

**•Usage Example❓•**
**We can make a simple program to take the user age 
and if the age is bigger than 18, it will print to the user that he can access our service

else if the user age is exactly equal to 18, it will print to him he can't use our service and to try again next year

else if the user age is smaller than 18, we will print that he can't use our service**

**Example📟:**
```python
# we take a user input and turn it to int

age = int(input("Type your age: "))

# we wil check if the user age is bigger than 18, then we will print to the user that he can use the service

if age > 18:
    print("You can use our service!")

# now we make an elif statement, it will check if the condition above it is not correct, then it will check that the user age is 18 then it will print to the user that he can't use our service and to try again next year

elif age == 18:
    print("You cant use our service yet!, try again next year")

# finally we make an else statment, and it will check if the none of the above conditions are True, it will print to the user that he can't use our service

else:
    print("You cant use our service!")

# OUTPUT
>> Type your age: 
# first time we will write 19
>> You can use our service!

# the second time we will write 18
>> You cant use our service yet!, try again next year

# the last time we will write 17
>> You cant use our service!
```
[GitHub](https://github.com/PythonNoob999/PythonTutorialBot/blob/master/examples/if_else_en.py)📒
''',
"lambda-ar": '''
**••lambda الدالة المجهولة••**

**•تعريف بسيط💬•**
**الدالة المجهولة او lambda, هي تعمل ك الدالة العادية، لكنها نسخه مصغرة من الدالة العادية، يمكنك عمل عمليات بسيطه جدا بها ك الدالة العادية**

**•طريقة الكتابة⌨️•**
`# تشكيل الدالة المجهولة يتكون من التالي
# 1- كلمة lambda لتعريفها كدالة مجهولة
# 2- معطيات الدالة، المعطيات التي تعطي للدالة لاستخدامها، مثل الدالة العادية
# 3- العملية التي ستقوم بإرجاعها الدالة
# سنقوم بعمل دالة وهمية و نضعها في متغير، الدالة تاخد المعطيات x و y، و تقوم بإرجاع قيمة جمعهم

func = lambda x,y: x+y
# نقوم بتجربة الدالة بالعددين 3 و 5 و نقوم بطباعة الناتج

print(func(3,5))

# المخرجات:
>> 8`

**•مثال للاستعمال❓•**
**نستطيع عمل دالة مجهولة بسيطة للغاية، تقوم بإرجاع عمر المستخدم بعد 5 سنين**

**مثال📟:**
```python
# اولا نقوم باخذ عمر المستخدم
age = int(input("قم بكتابة عمرك: "))

# سنقوم بعمل دالة مجهولة تاخد المعطي number، و تقوم بإرجاع المعطي number بزيادة 5
func = lambda number: number+5

# اخيرا نقوم بطباعة النتيجه للمستخدم
print("عمرك بعد 5 سنين هو ", func(age))

# المخرجات:
>> قم بإدخال عمرك: 
# سنقوم بادخال 18 للتجربة
>> عمرك بعد 5 سنين هو 23
```
[GitHub](https://github.com/PythonNoob999/PythonTutorialBot/blob/master/examples/lambda_ar.py)📒
''',
"lambda-en": '''
**••lambda, anonymous functions••**

**•Short Description 💬•**
**lambda are anonymous functions, the serve as a micro function that can do very simple opreations**

**•Syntax⌨️•**
`# a lambda function contains of
# 1- the lambda keyword to identify it
# 2- the function parameters
# 3- the value that the function will return
# here we will make a simple lambda function that takes x,y and return x+y, and put the function inside a variable

func = lambda x,y: x+y
# now let's try printing the function result when we use it with numbers, 5 and 8

print(func(5,8))
# OUTPUT:
>> 13`

**•Usage Example❓•**
**we can make a very simple program that takes the user age and tells him how old he will be after 5 years**

**Example📟:**
```python
# first we take the user age
age = int(input("Type your age: "))

# now we will make a lambda function that takes a number as a param, and return the number + 5
myfunc = lambda number: number+5

# Now we will print the new user age
print("You will be ", myfunc(age), " Years old in 5 years")

# OUTPUT:
>> Type your age: 
# we will type 16 as our age
>> You will be 21 Years old in 5 years
```
[GitHub](https://github.com/PythonNoob999/PythonTutorialBot/blob/master/examples/lambda_en.py)📒
''',
"basic_funcs-ar": "قم بإختيار الدالة اللتي تريد تعلمها!",
"basic_funcs-en": "Choose a function to learn!",
"basic_funcs-len()-ar": '''
**••len() الدالة••**

**•تعريف بسيط💬•**
**نستخدم الدالة ()len لارجاع طول انواع بيانات معينة، مثل النصوص و القوائم و انواع اخري**

**•طريقة الكتابة⌨️•**
`# معطيات الدالة ()len تكون من انواع البيانات المحددة فقط

len(list, str, bytes, tuple, range)
# و اللتي تكون قائمة او نص او bytes او مترابطة او الدالة range`

**•مثال للاستعمال❓•**
**نستطيع استخدام الدالة len لحسابة طول العديد من الأشياء**

**مثال📟:**
```python
# نقوم بعمل متغيرات فيها انواع بيانات مختلفة للتجربة

# قائمة
list = [4, 8, 7, "Ahmed", True]
# مترابطة
tuple = (4, 8, 7, "Ahmed", True)
# نص 
string = "Hello World!"

# الان سوف نقوم بطباعة طول كل متغير

# الدالة ستقوم بحسابة عدد عناصر القائمة
print("طول القائمة هو ", len(list), " عناصر")
# الدالة ستقوم بحسابة عدد عناصر المترابطة
print("طول المترابطة هو ", len(tuple), " عناصر")
# في حالة النصوص، الدالة سوف تقوم بحسابة عدد حروف النص
print("طول النص هو ", len(string), " عنصر")

# المخرجات
>> طول القائمة هو 5 عناصر
>> طول المترابطة هو 5 عناصر
>> طول النص هو 12 عنصر
# سنلاحظ ان الدالة قامت بحسابة طول النص ك 12 عنصر بدلا من 11 لان عدد حروف الجملة هو 11، لكن الدالة تقوم بحسابة المسافات ايضا
```
[GitHub](https://github.com/PythonNoob999/PythonTutorialBot/blob/master/examples/basic_funcs_len_ar.py)📒
''',
"basic_funcs-len()-en": '''
**••len() function••**

**•Short Description 💬•**
**the len() function return the number of items inside a string/list/tuple/bytes/range()**

**•Syntax⌨️•**
`len(str, list, tuple, bytes, range())`

**•Usage Example❓•**
**We can use the len() function to get the number of items in a str/tuple/list**

**Example📟:**
```python
# we make variables that contain multiple data types to calculate there length using the len() function

list = [3, 4, 8, "Ahmed", True]
tuple = (3, 4, 8, "Ahmed", True)
string = "Hello World!"

# now we calculate each variable length and print it

print("the list has ", len(list), " items")

print("the tuple has ", len(tuple), " items")

print("the string has ", len(string), " letters")
# OUTPUT
# the list and tuple contains 5 items, 3 int, 1 string, 1 boolean, so the total length is 5

>> the list has 5 items
>> the tuple has 5 items
# in the string case the len() function calculate the string, letter by letter
>> the string has 12 letters
# now you might think why the string has 12 "letter", when it contains only of 11 letters. well, the len() function also count empty spaces in a string
```
[GitHub](https://github.com/PythonNoob999/PythonTutorialBot/blob/master/examples/basic_funcs_len_en.py)📒
''',
"basic_funcs-min()-ar": '''
**••min() الدالة••**

**•تعريف بسيط💬•**
**نستخدم الدالة ()min للحصول علي اقل قيمة موجودة في قائمة او مترابطة**

**•طريقة الكتابة⌨️•**
`# هنا نقوم بعمل قائمة فيها بعض الارقام
numbers = [5, 19, 3, 66, 1]
# هنا نقوم بطباعة اقل قيمة في القائمة
print(min(numbers))
>> 1`

**•مثال للاستعمال❓•**
**نستطيع نقوم بعمل برنامج يقوم ب اخذ رقم من مستخدم و وضعه في قائمة مليئة ب الارقام
و اذا كان الرقم اللذي اختاره المستخدم هو اقل رقم، سنطبع له انه قام بكتابة اصغر رقم**

**مثال📟:**
```python
# نقوم ب اخذ رقم من المستخدم 
number = int(input("قم بكتابة رقم "))

# تقوم بعمل قائمة فيها عدة ارقام عشوائية و فيها الرقم الخاص ب المستخدم
numbers = [73, 13, 9, 22, number]

# الان نقوم بعمل شرط يتاكد من ان كان اصغر رقم يساوي الرقم اللذي كتبه المستخدم

if min(numbers) == number:
# سنقوم بطباعة ان المستخدم قام بكتابة اقل رقم في القائمة
    print("لقد قمت باختيار اصغر رقم في القائمة")

# نقوم بعمل شرط else، ان كان المستخدم لم يقم بكتابة اصغر قيمة في القائمة
else:
    print("رقمك ليس الاصغر في القائمة")

# المخرجات
>> قم بكتابة رقم
# سوف نقوم بكتابة 10 في اول مرة 
>> رقمك ليس الاصغر في القائمة
# الان سوف نجرب بكتابة 5 في تاني مرة
>> لقد قمت ب اختيار اصغر رقم في القائمة
```
[GitHub](https://github.com/PythonNoob999/PythonTutorialBot/blob/master/examples/basic_funcs_min_ar.py)📒
''',
"basic_funcs-min()-en": '''
**••min() function••**

**•Short Description 💬•**
**min() function used to return the smallest value in list/tuple**

**•Syntax⌨️•**
`# we will make a simple list 
numbers = [3, 9, 5, 1, 18]

# now we print the min() value of the list numbers
print(min(numbers))
>> 1`

**•Usage Example❓•**
**we can make a simple program that takes an input from the user and put it in a list with a bunch of numbers
then if the number he wrote is the smallest we will print that he won
other wise we will print that he lost**

**Example📟:**
```python
# we take the user input
number = int(input("Type a number: "))

# we put the number in a list
numbers = [62, 12, 94, 7, number]

# now we check if the smallest number in the list (numbers) is equal to the user number

if min(numbers) == number:
    print("You Won! ")

# other wise we will print that he lost
else:
    print("You lost! ")
```
[GitHub](https://github.com/PythonNoob999/PythonTutorialBot/blob/master/examples/basic_funcs_min_en.py)📒
''',
"basic_funcs-max()-ar": '''
**••max() الدالة••**

**•تعريف بسيط💬•**
**نستخدم الدالة ()max للحصول علي  اكبر قيمة موجودة في قائمة او مترابطة**

**•طريقة الكتابة⌨️•**
`# هنا نقوم بعمل قائمة فيها بعض الارقام
numbers = [5, 19, 3, 66, 1]
# هنا نقوم بطباعة اكبر قيمة في القائمة
print(max(numbers))
>> 66`

**•مثال للاستعمال❓•**
**نستطيع نقوم بعمل برنامج يقوم ب اخذ رقم من مستخدم و وضعه في قائمة مليئة ب الارقام
و اذا كان الرقم اللذي اختاره المستخدم هو اكبر رقم، سنطبع له انه قام بكتابة اكبر رقم**

**مثال📟:**
```python
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
>> قم بكتابة رقم
# سوف نقوم بكتابة 10 في اول مرة 
>> رقمك ليس الاكبر في القائمة
# الان سوف نجرب بكتابة 105 في تاني مرة
>> لقد قمت ب اختيار اكبر رقم في القائمة
```
[GitHub](https://github.com/PythonNoob999/PythonTutorialBot/blob/master/examples/basic_funcs_max_ar.py)📒
''',
"basic_funcs-max()-en": '''
**••max() function••**

**•Short Description 💬•**
**max() function used to return the biggest value in list/tuple**

**•Syntax⌨️•**
`# we will make a simple list 
numbers = [3, 9, 5, 1, 18]

# now we print the max() value of the list numbers
print(max(numbers))
>> 18`

**•Usage Example❓•**
**we can make a simple program that takes an input from the user and put it in a list with a bunch of numbers
then if the number he wrote is the biggest we will print that he won
other wise we will print that he lost**

**Example📟:**
```python
# we take the user input
number = int(input("Type a number: "))

# we put the number in a list
numbers = [62, 12, 94, 7, number]

# now we check if the biggest number in the list (numbers) is equal to the user number

if max(numbers) == number:
    print("You Won! ")

# other wise we will print that he lost
else:
    print("You lost! ")
```
[GitHub](https://github.com/PythonNoob999/PythonTutorialBot/blob/master/examples/basic_funcs_max_en.py)📒
''',
"basic_funcs-sum()-ar": '''
**••sum() الدالة••**

**•تعريف بسيط💬•**
**نقوم باستخدام الدالة ()sum لجلب مجموع القيم داخل قائمة/مترابطة**

**•طريقة الكتابة⌨️•**
`# هنا نقوم بعمل قائمة من الارقام
numbers = [15, 6, 8]
# نقوم بطباعة مجموع قيم القائمة
print(sum(numbers))
>> 29
# الناتج هو 29 لان. 15+6+8 (عناصر القائمة) تساوي 29`

**•مثال للاستعمال❓•**
**نستطيع بعمل برنامج بسيط، يقوم دائما باخذ معطي من مستخدم باستخدام الحلقة while، و اضافته في قائمة، و حين يكتب المستخدم كلمة exit نقوم ب الخروج من الحلقة while، و نقوم بطباعة مجموع الارقام اللذي كتبه المستخدم**

**مثال📟:**
```python
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
>> قم بكتابة رقم 
# هنا سنقوم بكتابة الاعداد 5, 8, 10، 12
# بعدها سنقوم بكتابة كلمة exit
>> [5, 8, 10, 12]
>> 35
```
[GitHub](https://github.com/PythonNoob999/PythonTutorialBot/blob/master/examples/basic_funcs_sum_ar.py)📒
''',
"basic_funcs-sum()-en": '''
**••sum() function••**

**•Short Description 💬•**
**the sum() function is used to return the sum of all the values inside a list/tuple**

**•Syntax⌨️•**
`# here we make a list with some numbers

numbers = [23, 16, 8, 10]
# now we print the sum of the list 
print(sum(numbers))
>> 57
# it printed 57 because 23+16+8+10 (the "numbers" list values) is 57`

**•Usage Example❓•**
**We can make a simple program
That always takes a user input using a While loop➿, and we check if the user input is not the word "exit" then we will add it as a number in a list, else if the user input is the word "exit" we will break out of the while loop, and then print the list and the sum() of it**

**Example📟:**
```python
# we make a empty list
numbers = []

# we make a while loop and take the user input
while True:
    number = input("Type a number ")
# now we make a if statment to check if the user input in the variable "number" does not equal to "exit", then it will add it to the number list

    if number != "exit":
        numbers.append(int(number))
# otherwise, we will break out of the loop

    else:
        break

# finally when the loop ends, we print the numbers list and its sum
print(numbers)
print(sum(numbers))

# OUTPUT
>> Type a number
# we will type 5
>> Type a number
# we will type 8
>> Type a number
# we will type 12
>> Type a number
# this time we will type exit to finish
# now it will print the list of numbers and sum
>> [5, 8, 12]
>> 25
```
[GitHub](https://github.com/PythonNoob999/PythonTutorialBot/blob/master/examples/basic_funcs_sum_en.py)📒
''',
"basic_funcs-enumerate()-ar": '''
''',
"basic_funcs-enumerate()-en": '''
''',
"basic_funcs-range()-ar": '''
''',
"basic_funcs-range()-en": '''
''',
"basic_funcs-type()-ar": '''
''',
"basic_funcs-type()-en": '''
''',
"basic_funcs-isinstance()-ar": '''
''',
"basic_funcs-isinstance()-en": '''
''',
}

keyboards = {
"start-en": [
    [Button("variables💾", callback_data="info-variables"), Button("Data Types📋", callback_data="data_types-en")],
    [Button("functions📠", callback_data="info-functions"), Button("loops💈", callback_data="loops-en")],
    [Button("if-else🖋✒️", callback_data="info-if_else"), Button("lambda❓", callback_data="info-lambda")],
    [Button("Basic functions☕", callback_data="basic_funcs-en")],
    [Button("Language💬", callback_data="set_lang")]
],
"start-ar": [
    [Button("المتغيرات💾", callback_data="info-variables"), Button("انواع البيانات📋", callback_data="data_types-ar")],
    [Button("الدوال📠", callback_data="info-functions"), Button("الحلقات💈", callback_data="loops-ar")],
    [Button("if الشرطية🖋✒️", callback_data="info-if_else"), Button("الدالة مجهولة الهوية❓", callback_data="info-lambda")],
    [Button("الدوال الجاهزة☕", callback_data="basic_funcs-ar")],
    [Button("اللغة💬", callback_data="set_lang")]
],
"basic_funcs-ar": Markup([
    [Button("len()", callback_data="basic_funcs-len()-ar"), Button("min()", callback_data="basic_funcs-min()-ar"), Button("max()", callback_data="basic_funcs-max()-ar")],
    [Button("sum()", callback_data="basic_funcs-sum()-ar"), Button("enumerate()", callback_data="basic_funcs-enumerate()-ar"), Button("range()", callback_data="basic_funcs-range()-ar")],
    [Button("type()", callback_data="basic_funcs-type()-ar"), Button("isinstance()", callback_data="basic_funcs-isinstance()-ar")],
    [BACK],
]),
"basic_funcs-en": Markup([
    [Button("len()", callback_data="basic_funcs-len()-en"), Button("min()", callback_data="basic_funcs-min()-en"), Button("max()", callback_data="basic_funcs-max()-en")],
    [Button("sum()", callback_data="basic_funcs-sum()-en"), Button("enumerate()", callback_data="basic_funcs-enumerate()-en"), Button("range()", callback_data="basic_funcs-range()-en")],
    [Button("type()", callback_data="basic_funcs-type()-en"), Button("isinstance()", callback_data="basic_funcs-isinstance()-en")],
    [BACK],
]),
"data_types-ar" : Markup([
    [Button("string النصية💬", callback_data="data_types-str-ar"), Button("int الرقمية🔢", callback_data="data_types-int-ar"), Button("float العشرية📟", callback_data="data_types-float-ar")], 
    [Button("bool المنطقية🧠", callback_data="data_types-bool-ar")],
    [Button("القوائم []", callback_data="data_types-list-ar"), Button("مترابطة ()", callback_data="data_types-tuple-ar"), Button('dict {}', callback_data="data_types-dict-ar")],
    [BACK]
]),
"data_types-en": Markup([
    [Button("string💬", callback_data="data_types-str-en"), Button("int🔢", callback_data="data_types-int-en"), Button("float📟", callback_data="data_types-float-en"), Button("bool🧠", callback_data="data_types-bool-en")],
    [Button("array/list []", callback_data="data_types-list-en"), Button("tuple ()", callback_data="data_types-tuple-en"), Button('dict {}', callback_data="data_types-dict-en")],
    [BACK]
]),
"loops-en": Markup([
    [Button("While loop➰", callback_data="loops-while-en"), Button("For loop➰", callback_data="loops-for-en")],
    [BACK]
]),
"loops-ar": Markup([
    [Button("While حلقة➰", callback_data="loops-while-ar"), Button("For حلقة➰", callback_data="loops-for-ar")],
    [BACK]
]),
"variables": Markup([[BACK]]),
"functions": Markup([[BACK]]),
"if_else": Markup([[BACK]]),
"lambda": Markup([[BACK]]),
"lang": RMarkup([
    ["English🇺🇲", "Arabic🇸🇦"]
], resize_keyboard=True, one_time_keyboard=True),
"back": Markup([[BACK]]),
"admin": Markup([
    [Button("Message generator⚙️", callback_data="make_a_message")]
])
}