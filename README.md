<h1 align="center">Queue Bot 🤖</h1>

<p align="center">
  <img src="public/logo_gemini_original.png" alt="Queue Bot Logo" width="200"/>
</p>

<p align="center">
  <a href="https://t.me/QueueBest_bot">
    <img src="https://img.shields.io/badge/Telegram-Bot-blue?style=for-the-badge&logo=telegram" alt="Telegram Bot">
  </a>
  <img src="https://img.shields.io/badge/python-3.8-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/docker-ready-blue?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
</p>

<p align="center">
    <b>Современный и удобный бот для управления очередями в групповых чатах Telegram.</b>
</p>

---

## ✨ Особенности

*   🚀 **Мгновенное создание очередей**: Просто введите команду и название.
*   👥 **Работа в группах и супергруппах**: Полная поддержка топиков (Topics).
*   🐳 **Docker**: Легкая установка и запуск одной командой.
*   📱 **Интерактивный интерфейс**: Кнопки для записи, пропуска и перемещения в очереди.

## 🛠 Установка и запуск (Docker)

Самый простой способ запустить бота — использовать Docker.

1.  **Клонируйте репозиторий**:
    ```bash
    git clone https://github.com/shorins/iu8_queue_bot.git
    cd iu8_queue_bot
    ```

2.  **Настройте окружение**:
    Создайте файл `.env` из примера:
    ```bash
    cp .env.example .env
    ```
    Откройте `.env` и укажите ваш `TELE_API_TOKEN`.

3.  **Запустите**:
    ```bash
    docker-compose up -d --build
    ```

Бот запустится и будет хранить данные в папке `db_data`.

## 📖 Как пользоваться

1.  **Добавьте бота** [@QueueBest_bot](https://t.me/QueueBest_bot) в вашу группу.
2.  **Дайте права**: Рекомендуется сделать бота администратором для удаления служебных сообщений.
3.  **Создайте очередь**:
    *   Введите `/create_queue` или `/plan_queue`.
    *   Введите название очереди.
4.  **Управляйте**: Используйте кнопки под сообщением очереди.

## 👨‍💻 Авторы

**Original Project (2021):**
*   [Alexey Alexandrov](https://github.com/aaaaaaaalesha) — *Initial work & Core logic*

**Fork & Maintenance (2025):**
*   [Sergey Shorin](https://github.com/shorins) — *Dockerization, Topics support, Refactoring & UI improvements*

---
<p align="center">
  <i>Developed with ❤️ for efficient teamwork.</i>
</p>
