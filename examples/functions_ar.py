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
#>> 50 درجة
