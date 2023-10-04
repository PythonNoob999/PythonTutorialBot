fruits = ["Apple", "Kiwi", "Banana"]
# رقم المكان يبدا ب 0 في اغلب اللغات البرمجية

print(fruits[0])
#>> Apple

# يمكنك ايضا استخدام قيم سالبة و اللتي ستعطيك نتائج مختلفة

print(fruits[-1]) # اخر مكان
#>> Banana

print(fruits[-2]) # المكان ما قبل الاخير

#>> Kiwi
fruits[0] = "Orange" # نستطيع ايضا تغير قيمة معينة في القائمة
print(fruits)
#>> ["Orange", "Kiwi", "Banana"]
