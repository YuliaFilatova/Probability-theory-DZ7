import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

#1)  Даны две  независимые выборки. Не соблюдается условие нормальности
# x1  380,420, 290
# y1 140,360,200,900
#Сделайте вывод по результатам, полученным с помощью функции

alpha = 0.05
x= np.array([380, 420, 290])
y= np.array([140, 360, 200, 900])
d = stats.mannwhitneyu(x,y)
print('\n>>> Statistics = %.2f \n>>> Р-value = %.3f' % (d))
s, p = stats.mannwhitneyu(x,y)
if p > alpha:
    print('>>> Cтатистически значимых различий нет, нулевая гипотеза не отвергается.')
else:
    print('>>> Cтатистически значимые различия присутствуют, нулевую гипотезу отвергаем.')


#2) Исследовалось влияние препарата на уровень давления пациентов. Сначала измерялось давление до приема препарата, потом через 10 минут и через 30 минут. Есть ли статистически значимые различия?
#1е измерение до приема препарата: 150, 160, 165, 145, 155
#2е измерение через 10 минут: 140, 155, 150,  130, 135
#3е измерение через 30 минут: 130, 130, 120, 130, 125

alpha=0.05
x1=np.array([150, 160, 165, 145, 155])
x2=np.array([140, 155, 150, 130, 135])
x3=np.array([130, 130, 120, 130, 125])
d = stats.friedmanchisquare(x1, x2, x3)
print('\n>>> Statistics = %.2f \n>>> Р-value = %.3f' % (d))
s, p = stats.friedmanchisquare(x1, x2, x3)
if p > alpha:
    print('>>> Cтатистически значимых различий нет, нулевая гипотеза не отвергается, препарат не влияет на давление.')
else:
    print('>>> Cтатистически значимые различия присутствуют, нулевую гипотезу отвергаем, препарат влияет на давление.')

#3) Сравните 1 и 2 е измерения, предполагая, что 3го измерения через 30 минут не было.

alpha=0.05
x1=np.array([150, 160, 165, 145, 155])
x2=np.array([140, 155, 150, 130, 135])
d = stats.wilcoxon(x1, x2)
print('\n>>> Statistics = %.2f \n>>> Р-value = %.3f' % (d))
s, p = stats.wilcoxon(x1, x2)
if p > alpha:
    print('>>> Cтатистически значимых различий нет, нулевая гипотеза не отвергается, препарат не влияет на давление.')
else:
    print('>>> Cтатистически значимые различия присутствуют, нулевую гипотезу отвергаем, препарат влияет на давление.')

#4) Даны 3 группы  учеников плавания. Сделайте вывод по различиям.
#В 1 группе время на дистанцию 50 м составляют:
# 56, 60, 62, 55, 71, 67, 59, 58, 64, 67
#Вторая группа : 57, 58, 69, 48, 72, 70, 68, 71, 50, 53
#Третья группа: 57, 67, 49, 48, 47, 55, 66, 51, 54

alpha=0.05
x1=np.array([56, 60, 62, 55, 71, 67, 59, 58, 64, 67])
x2=np.array([57, 58, 69, 48, 72, 70, 68, 71, 50, 53])
x3=np.array([57, 67, 49, 48, 47, 55, 66, 51, 54])
d = stats.kruskal(x1,x2,x3)
print('\n>>> Statistics = %.2f \n>>> Р-value = %.3f' % (d))
s, p = stats.kruskal(x1,x2,x3)
if p > alpha:
    print('>>> Cтатистически значимых различий нет, нулевая гипотеза не отвергается, время на дистанцию одинаковое.')
else:
    print('>>> Cтатистически значимые различия присутствуют, нулевую гипотезу отвергаем, время на дистанцию не одинаковое.')

#5) Заявляется, что партия изготавливается со средним арифметическим 2,5 см.
# Проверить данную гипотезу, если известно, что размеры изделий подчинены нормальному
# закону распределения. Объем выборки 10, уровень статистической значимости 5%
#2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34

alpha = 0.05
data = [2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34]
n = len(data)
mean = np.mean(data)
std = np.std(data, ddof=1)
t_stat = (mean - 2.5) / (std / np.sqrt(10))
t_critical = stats.t.ppf(1 - alpha, n-1)
if t_stat < t_critical:
    print(">>> Нулевая гипотеза не отвергается, партия изготавливается со средним арифметическим 2,5 см.")
else:
    print(">>> Нулевая гипотеза отвергается, партия изготавливается со средним арифметическим не равным 2,5 см.")
    
mean, std, t_stat, t_critical
