# Тестовое задание "Получение данных об объектах из BIM-модели"

## Описание

Для расчёта пожарной безопасности из готовой BIM-модели здания необходимо получить следующие данные:
1. Файл с геометрией здания в gbXML-формате.
2. Файл с данными о нескольких объектах внутри здания в любом открытом формате: TXT, CSV, XML. Данные должны обязательно содержать координаты x, y, z объекта.

Подробное описание задания: [Test_BIM_FDS](https://github.com/lotus-uems/Test_BIM_FDS)

## Решение

### 1. Геометрия здания

Для выгрузки геометии здания в приложении Autodesk Revit открываем BIM-модель здания (в данном случае это модель, взятая из примеров — "rst_advanced_sample_project.rvt"). Выбираем меню "Файл > Экспорт > gbXML", в диалоговом окне выбираем режим сохранения "Использовать элементы здания", далее выбираем путь, где нужно сохранить XML-файл с геометрией здания (в нашем примере это "rac_advanced_sample_project.xml").

### 2. Данные об объектах

Для получения данных об объектах внутри здания в приложении Autodesk Revit открываем ту же BIM-модель здания, выбираем меню "Файл > Экспорт > IFC", в диалоговом окне выбираем путь к файлу, куда будет сохранена модель в IFC-формате, и нажимаем кнопку "Экспорт". Далее данные о нужных объектах выгружаем из IFC-модели в CSV-файл при помощи утилиты [export_objects.py](https://github.com/SergeFrancois/lotus_bim_fds_test_solution/export_objects.py), которая основана на использовании открытой библиотеки [IfcOpenShell](https://wiki.osarch.org/index.php?title=IfcOpenShell) (объекты выбираются по ключевым словам, которые содержатся в названии семейтва). Например:

в Windows:
```
python.exe export_objects.py rac_advanced_sample_project.ifc project_objects.csv plant female male
```
в Linux:
```
python3 export_objects.py rac_advanced_sample_project.ifc project_objects.csv plant female male
```
Полученный файл (в нашем примере это "project_objects.csv") содержит название семейтва объктов, название типа в семействе и координаты расположения объекта в здании.
На рисунке сплошной красной линией отмечены искомые объекты.

![Desired objects](https://github.com/SergeFrancois/lotus_bim_fds_test_solution/project_objects.png)
