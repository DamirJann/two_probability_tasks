
## Задание 2: геометрическая вероятность

<strong> Из отрезка [0; 1] случайно выбираются числа a и b. Какова вероятность того, что ![Alt Text](
https://github.com/DamirJann/two_probability_tasks/blob/master/task2/gifs/Tex2Img_1587067986.jpg) </strong>

**Решение:** При помощи функции random() "бросим" a, b на отрезок [0,1]. Проведём 1000 испытаний. На каждом этапе будем хранить общее количество испытаний и количество благоприятных случаев, то есть таких, что ![Alt Text](
https://github.com/DamirJann/two_probability_tasks/blob/master/task2/gifs/Tex2Img_1587067986.jpg). Тогда отношение благоприятных исходов к числу испытаний и есть искомая вероятность.

Построим модель броска двух точек на отрезок и график зависимости вероятности от количества испытаний. 

* До 50 испытаний

![Alt Text](
https://github.com/DamirJann/two_probability_tasks/blob/master/task2/gifs/slowModelPlot.gif)

* До 1000 испытаний

![Alt Text](
https://github.com/DamirJann/two_probability_tasks/blob/master/task2/gifs/fast_plot.gif)
