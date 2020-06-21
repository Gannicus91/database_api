# database_api

1. Восстановить базу данных из дампа:
    ```shell script
    > psql -U postgres university < university_backup
    ```
2. Создать и активировать виртуальное окружение
    ```shell script
    > python3 -m venv env
    > source env/bin/activate
    ```
3. Установить зависимости
    ```shell script
    > pip install -r requirements.txt
    ```
4. Запустить сервер
    ```shell script
    > ./manage.py runserver 127.0.0.1:8000
    ```
