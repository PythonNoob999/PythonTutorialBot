# اولا نقوم بصناعة قائمة الاسعار
fruits = {
"تفاح": 3, # تفاح = 3$
"كيوي": 9, # كيوي = 9$ 
"موز": 4 # موز = 4$
}

# الان تستطيع طباعة سعر الفاكهة ب استخدام اسمها بدلآ من رقم مكانها في القائمة

print(fruits["كيوي"], "$")
#>> 9$

# تستطيع ايضا تغير سعر الفاكهة!

fruits["موز"] = 2
print(fruits["موز"], "$")
#>> 2$

# و هذا طبعا سيقوم بتغيير القائمة كليا

print(fruits)
#>> {
#    "تفاح": 3,
#    "كيوي": 9,
#    "موز": 2
#}