<h1 align="center"> 🚶IU8-QueueBot🚶🚶 </h1>

[comment]: <> (Badges)

<p align="center">
  <a href="https://img.shields.io/badge/aiogram-v.2.17.1-orange?style=plastic">
    <img alt="Aiogram" src="https://img.shields.io/badge/aiogram-v.2.17.1-orange?style=plastic">
  </a>
  <a href="https://github.com/aaaaaaaalesha/iu8_queue_bot/deployments/activity_log?environment=iu8-queue-bot">
    <img alt="Deployment" src="https://img.shields.io/github/deployments/aaaaaaaalesha/iu8_queue_bot/iu8-queue-bot?style=plastic">
  </a>
  <a href="https://www.npmjs.com/package/readme-md-generator">
    <img alt="Build Status" src="https://github.com/aaaaaaaalesha/iu8_queue_bot/actions/workflows/main.yaml/badge.svg">
  </a>
  <a href="https://www.codefactor.io/repository/github/aaaaaaaalesha/iu8_queue_bot/overview/main">
    <img alt="CodeFactor" src="https://www.codefactor.io/repository/github/aaaaaaaalesha/iu8_queue_bot/badge/main?style=plastic">
  </a>
  <a href="https://img.shields.io/github/languages/code-size/aaaaaaaalesha/iu8_queue_bot?style=plastic">
    <img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/aaaaaaaalesha/iu8_queue_bot?style=plastic">
  </a>
  <a href="https://img.shields.io/github/stars/aaaaaaaalesha/iu8_queue_bot?style=plastic">
    <img alt="Stars" src="https://img.shields.io/github/stars/aaaaaaaalesha/iu8_queue_bot?style=plastic" />
  </a>
  <a href="https://img.shields.io/github/watchers/aaaaaaaalesha/iu8_queue_bot?style=plastic">
    <img alt="GitHubWatchers" src="https://img.shields.io/github/watchers/aaaaaaaalesha/iu8_queue_bot?style=plastic">
  </a>
</p>

[comment]: <> (Logo)
<p align="center">
  <a href="https://t.me/iu8_queue_bot">
    <img alt="queue_bot" height="200" width="200" src="https://user-images.githubusercontent.com/55093100/147390446-d783063a-e68e-4caa-9711-731c13a9fd2d.png"/>
  </a>
</p>

[comment]: <> (Techs)
<p align="center">
  <a href="#">
    <img alt="Python" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
  </a>
  <a href="#">
    <img alt="SQLite" src="https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white">
  </a>
  <a href="#">
    <img alt="GitHub Actions" src="https://img.shields.io/badge/githubactions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white">
  </a>
  <a href="#">
    <img alt="Heroku" src="https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white">
  </a>
</p>

---

## Телеграм-бот для создания очередей в групповых чатах

Этот бот поможет запланировать очередь на определённую дату и время, своевременно запустить её в вашем групповом чате!

Попробуйте [@iu8_queue_bot](https://t.me/iu8_queue_bot) сами, а если возникли вопросы, смотрите, как пользоваться ботом,
ниже.

## Запуск через Docker

Для запуска бота на сервере используйте Docker. Это самый простой способ.

1.  **Установите Docker и Docker Compose**.
2.  **Клонируйте репозиторий**:
    ```bash
    git clone https://github.com/aaaaaaaalesha/iu8_queue_bot.git
    cd iu8_queue_bot
    ```
3.  **Создайте файл `.env`**:
    ```bash
    cp .env.example .env
    # Отредактируйте .env и вставьте ваш токен
    ```
4.  **Запустите бота**:
    ```bash
    docker-compose up -d --build
    ```

Бот запустится в фоне. Данные базы данных будут сохранены в папке `db_data`.

## Как пользоваться?

### 1. Начало работы
Добавьте бота [@iu8_queue_bot](https://t.me/iu8_queue_bot) в ваш групповой чат.

### 2. Создание очереди
Любой участник группы может создать очередь. Для этого:
1. Отправьте команду `/create_queue` (или `/plan_queue`) прямо в групповой чат.
2. Бот попросит ввести **название очереди**.
3. После ввода названия очередь **сразу же запустится**.

### 3. Участие в очереди
Когда очередь запущена, в чате появится сообщение с кнопками:
- **Записаться**: Добавить себя в конец очереди.
- **Выписаться**: Удалить себя из очереди.
- **В хвост**: Переместиться в конец очереди.
- **Пропустить**: Поменяться местами со следующим участником.
- **Список**: Обновляется в реальном времени в сообщении бота.

### Команды
- `/start` - Начало работы
- `/help` - Помощь
- `/create_queue` - Создать очередь (только в группе)
- `/queues_list` - Посмотреть запланированные очереди
- `/delete_queue` - Удалить очередь (для создателя)

## Author

#### Copyright © 2021, [Alexey Alexandrov](https://github.com/aaaaaaaalesha)

[![Telegram](https://img.shields.io/badge/aaaaaaaalesha-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/aaaaaaaalesha)
<a href="mailto:sks2311211@mail.ru">
<img alt="build status" src="https://img.shields.io/badge/-sks2311211@mail.ru-c14438?style=flat&logo=Gmail&logoColor=white&link=mailto:sks2311211@mail.ru" />
</a>

