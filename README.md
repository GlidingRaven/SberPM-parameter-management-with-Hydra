# Управление параметрами в Process mining при помощи фреймоврка Hydra

![example](files/1.jpg)

Рабочий пример использования библиотеки SberPM для Process mining'а вместе с фреймворком Hydra, для удобного логирования запусков и управления параметрами датасета и модели.

Версии библиотек, нужных для запуска программы, перечисленны в файле req.txt

## Встроенные Датасеты

**example.csv** - демонстрационная выборка из библиотеки [Sber_Process_Mining](https://github.com/SberProcessMining/Sber_Process_Mining). Конфигурация для него содержится в файле *cond/dataset/example.yaml*:
```
name: example
filename: example.csv
separator: ','
id_col: id
act_col: stages
time_col: dt
date_format: '%Y-%m-%d'
```

**BPI2016_Complaints.csv** - выборка из соревнования BPI Challenge 2016 [Complaints](https://data.4tu.nl/articles/dataset/BPI_Challenge_2016_Complaints/12717647/1). Конфигурация для него *cond/dataset/complains.yaml*:
```name: complains
filename: BPI2016_Complaints.csv
separator: ';'
id_col: Office_U
act_col: Office_W
time_col: ContactDate
date_format: '%Y-%m-%d'
```
