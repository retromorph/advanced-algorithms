# Advanced algorithms

Этот репозиторий - попытка выстроить повествование о продвинутых алгоритмах с теоретической точки зрения с нуля.

## Настройка окружения

Предварительно должна быть установлена [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)

```sh
git clone https://github.com/retromorph/advanced-algorithms.git
cd advanced-algorithms
conda create env -f environment.yml
conda activate advanced-algorithms
jupyter notebook
```

## Структура курса

Курс организован в пронумерованные от 000 до 999 разделы (папки). 
В каждой папке лежат ipynb ноутбуки, в которых находится теория и код по теме

## Языки программирования

В этом репозитории используются
- C++ для всех итоговых реализаций
- Python для демонстрации идей и для генерации сопровождающей информации (тесты, подсчеты, графики)

Зачастую в одном ноутбуке может быть и код на C++ и код на Python. Так что иногда придется переключать кернелы

## Готовые разделы
