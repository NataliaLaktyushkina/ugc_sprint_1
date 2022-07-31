# Проектная работа 8 спринта

[Репозиторий ugc_sprint_1 (проектная работа 8-го спринта)](https://github.com/NataliaLaktyushkina/ugc_sprint_1)

Ваша цель — сохранить метки данных о просмотрах фильмов
из приложения в аналитическое хранилище. 
Это позволит аналитикам изучать историю просмотров
и предлагать улучшения онлайн-кинотеатра.

# Запуск проекта
`docker compose -f docker-compose.spark.python.yml -f docker-compose.kafka.yml`

# Описание архитектуры
[as_is](uml/as_is.drawio)

as_is в формате [png](uml/as_is.png)

# Spark Jupyter

Задание №1 - рассчитанный [rating by reviews](/spark_data/combined/rating_by_reviews)

Задание №2 - в [products.csv](/spark_data/combined/products_with_ratings.csv) добавлена колонка "rating_by_reviews"

[Код](/spark_data/Ice_cream_rating.ipynb)

# ClickHouse

[Схема](/click_house/clickhouse_schema.drawio) кластера 

# Исследование выбор хранилища

В результате вашего исследования у вас должны быть:
- Числа скорости вставки и чтения данных в хранилищах.
- Схемы хранения и обработки данных в разных хранилищах.
- Скрипты, которые загружают или генерируют данные в хранилища.
- Какая-то дополнительная информация о работе с хранилищами, которая поможет принять взвешенное решение.

# Загрузка данных из Kafka в Clickhouse
Вы познакомились со всеми необходимыми технологиями. Дело за малым: написать ETL для перегрузки данных в аналитическое хранилище, чтобы аналитики наконец смогли выполнять свою работу. Основная цель — сохранить метки данных о просмотрах фильмов из приложения в аналитическое хранилище. Это позволит аналитикам изучать историю просмотров и предлагать дальнейшие улучшения онлайн-кинотеатра.
В рамках этой задачи необходимо обратить внимание на несколько важных моментов:
- Проверьте, что схема данных вашего аналитического хранилища поддерживает возможность находить самые просматриваемые фильмы и понимать, какие фильмы не досматривают до конца.
- Продумайте возможность непрерывной работы ETL-процесса так, 
чтобы он был толерантен к сбоям источника данных и хранилища.
- Так как поток данных ожидается непрерывным нужно проверить, что ваше приложение не «течёт». 
То есть нужно внедрить средства мониторинга памяти приложения.

