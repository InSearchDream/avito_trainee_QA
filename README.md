# Описание структуры файлов в репозитории
- №1.pdf - файл с выполнением первого задания
- .idea - служебные файлы среды PyCharm
- TESTCASES.md - файл с описанием тест-кейсов
- README.md - файл с инструкцией
- volume_watter_1.py - автотест проверки счетчика сохраненного объема воды
- volume_CO2.py - автотест проверки счетчика предотвращенного объема выброса CO2
- electric_power_3.py - автотест проверки счетчика сэкономленной электроэнергии
- output - папка, содержащая результирующие скриншоты

# Инструкция по запуску автотестов

## Предварительные действия
1. Устанавливаем на ПК python версии 3.9
2. С официального сайта скачиваем дистрибутив PyCharm и устанавливаем его на ПК
3. Загружаем файлы из текущего репозитория
4. Открываем загруженный проект в PyCharm
5. Если отображается ошибка Unresolved reference 'playwright', то через Interpreter Settings... добавляем библиотеку pytest-playwright

## Запуск тестов
1. В PyCharm выбираем необходимый нам тест
- volume_watter_1.py
- volume_CO2.py
- electric_power_3.py
2. Нажимаем по нему ПКМ
3. Выбираем действие RUN 'название_теста' 

## Результат работы тестов
После проведения всех тестов в папке output должно располагаться 3 скриншота. 
- 1.png - скриншот счетчика сохраненного объема воды (тест volume_watter_1.py)
- 2.png - скриншот счетчика предотвращенного объема выброса CO2 (тест volume_CO2.py)
- 3.png - скриншот счетчика сэкономленной электроэнергии (тест electric_power_3.py)