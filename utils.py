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
`{}`
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
`{}`
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
`number = 5
print(number*2)
>> 10`
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
`# هنا نقوم بعمل متغير ب قيمة 5 و طباعته x 2
number = 5
print(number*2)
>> 10`
''',
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
`
user_name = "Ahmed"
password = "12345abc"
`
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
`
user_name = "Jack"
password = "12345abc"
`
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
`# نقوم بعمل متغيرين فيهم اول زاويتين
Angle1 = 70
Angle2 = 80
# نقوم بجمع المتغيرين و نطرحهم من 180
print("Third angle is ", (Angle1+Angle2)-180, " Degrees°")`
>> Third angle is 30 Degrees°
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
`Angle1 = 80
Angle2 = 70
print("Third angle is ", (Angle1+Angle2)-180, " Degrees°")`
>> Third angle is 30 Degrees°
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
`# نقوم بتعريف متغيرين فيهم الوزن و الطول

height = 5.9
weight = 160.74

# نقوم بحسابة مؤشر كتلة الجسم (BMI)
bmi = weight / (height**2)
 
# نقوم بطباعة مؤشر كتلة الجسم (BMI)
print("Your bmi is ", bmi)
>> Your bmi is 4.61763861`
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
`# We declare height & weight in float variables

height = 5.9
weight = 160.74

# we calculate the BMI
bmi = weight / (height**2)
 
# now we print the bmi
print("Your bmi is ", bmi)
>> Your bmi is 4.61763861`
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
`# نقوم بعمل المتغييرين
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
>> False`
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
`# we make the 2 passwords vars
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
>> False`
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
`fruits = ["Apple", "Kiwi", "Banana"]
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
>> ["Orange", "Kiwi", "Banana"]`
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
`fruits = ["Apple", "Kiwi", "Banana"]
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
>> ["Orange", "Kiwi", "Banana"]`
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
`# Creating a tuple with fruits
fruits = ("Apple", "Kiwi", "Banana")

# we can also print it's values with indexing

print(fruits[0])
>> Apple

# and also use negative indexing
print(fruits[-1]) 
>> Banana

# but unlike lists[], you can't change it's data

fruits[0] = "Orange"
>> TypeError: "str" object does not support item assignment❗️`
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
`# نصنع مترابطة بها القيم
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

>> TypeError: "str" object does not support item assignment❗️`
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
`# We make a price dictionary
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
}`
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
`# اولا نقوم بصناعة قائمة الاسعار
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
}`
'''
}

keyboards = {
"start-en": [
    [Button("variables💾", callback_data="info-variables"), Button("Data Types📋", callback_data="data_types-en")],
    [Button("functions📠", callback_data="info-functions"), Button("loops💈", callback_data="info-loops")],
    [Button("if-else🖋✒️", callback_data="info-if_else"), Button("lambda❓", callback_data="info-lambda")],
    [Button("Language💬", callback_data="set_lang")]
],
"start-ar": [
    [Button("المتغيرات💾", callback_data="info-variables"), Button("انواع البيانات📋", callback_data="data_types-ar")],
    [Button("الدوال📠", callback_data="info-functions"), Button("الحلقات💈", callback_data="info-loops")],
    [Button("if الشرطية🖋✒️", callback_data="info-if_else"), Button("الدالة مجهولة الهوية❓", callback_data="info-lambda")],
    [Button("اللغة💬", callback_data="set_lang")]
],
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
"variables": Markup([[BACK]]),
"lang": RMarkup([
    ["English🇺🇲", "Arabic🇸🇦"]
], resize_keyboard=True, one_time_keyboard=True),
"back": Markup([[BACK]]),
"admin": Markup([
    [Button("Message generator⚙️", callback_data="make_a_message")]
])
}