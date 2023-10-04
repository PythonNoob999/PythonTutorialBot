# نصنع مترابطة بها القيم
fruits = ("Apple", "Kiwi", "Banana")

# نقوم بطباعة عناصرها ايضا ب استخدام رقم المكان

print(fruits[0])
#>> Apple

# ايضا نستطيع استخدام ارقام سالبة
print(fruits[-1]) 
#>> Banana

# لكن عكس القوائم، سنحصل علي خلل عند تغير قيمة بداخلها

fruits[0] = "Orange"
# خطأ، نوع البيانات النصية لايدعم تبادل القيم

#>> TypeError: "str" object does not support item assignment❗️
