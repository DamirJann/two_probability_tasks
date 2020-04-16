## Задание 2: геометрическая вероятность

* Из отрезка [0; 1] случайно выбираются числа a и b. Какова вероятность того, что <img src="http://www.sciweavers.org/tex2img.php?eq=a%5E2%20%3C%20b%20%3C%20%5Csqrt%7Ba%7D&bc=White&fc=Black&im=jpg&fs=12&ff=ccfonts,eulervm&edit=0" align="center" border="0" alt="a^2 < b < \sqrt{a}" width="97" height="19" />

**Решение:** При помощи функции random() "бросим" a, b на отрезок [0,1]. Проведём 1000 испытаний. На каждом этапе будем хранить общее количество испытаний и количество благоприятных случаев, то есть <img src="http://www.sciweavers.org/tex2img.php?eq=a%5E2%20%3C%20b%20%3C%20%5Csqrt%7Ba%7D&bc=White&fc=Black&im=jpg&fs=12&ff=ccfonts,eulervm&edit=0" align="center" border="0" alt="a^2 < b < \sqrt{a}" width="97" height="19" />. Тогда отношение благоприятных исходов к числу испытаний и есть искомая вероятность.

Построим модель броска двух точек на отрезок и график зависимости вероятности от количества испытаний.

* До 50 испытаний

![Alt Text](
https://github.com/DamirJann/two_probability_tasks/blob/master/task2/gifs/slowModelPlot.gif)

* До 1000 испытаний

![Alt Text](
https://github.com/DamirJann/two_probability_tasks/blob/master/task2/gifs/fast_plot.gif)
