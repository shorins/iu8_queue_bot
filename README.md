<h1 align="center">Queue Bot 🤖</h1>

<p align="center">
  <img src="public/logo.jpg" alt="Queue Bot Logo" width="400"/>
</p>

<p align="center">
  <a href="https://t.me/QueueBest_bot">
    <img src="https://img.shields.io/badge/Telegram-Bot-blue?style=for-the-badge&logo=telegram" alt="Telegram Bot">
  </a>
  <img src="https://img.shields.io/badge/python-3.8-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/docker-ready-blue?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
</p>

<p align="center">
  <a href="https://t.me/QueueBest_bot">
    <img src="public/open_in_telegram.png" alt="Open in Telegram" width="200"/>
  </a>
</p>

<p align="center">
    <b>Modern and convenient bot for managing queues in Telegram group chats.</b>
    <br>
    <b>Современный и удобный бот для управления очередями в групповых чатах Telegram.</b>
</p>

---

## 📑 Table of Contents / Оглавление

*   [🇬🇧 English Version](#-english-version)
    *   [Features](#-features)
    *   [Installation & Run (Docker)](#-installation--run-docker)
    *   [How to Use](#-how-to-use)
    *   [Authors](#-authors)
*   [🇷🇺 Русская версия](#-русская-версия)
    *   [Особенности](#-особенности)
    *   [Установка и запуск (Docker)](#-установка-и-запуск-docker)
    *   [Как пользоваться](#-как-пользоваться)
    *   [Авторы](#-авторы-1)

---

# 🇬🇧 English Version

## ✨ Features

*   🚀 **Instant Queue Creation**: Just enter the command and the name.
*   👥 **Groups & Supergroups**: Full support for Topics.
*   🐳 **Docker**: Easy installation and run with a single command.
*   📱 **Interactive Interface**: Buttons to join, skip, and move within the queue.

## 🛠 Installation & Run (Docker)

The easiest way to run the bot is using Docker.

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/shorins/iu8_queue_bot.git
    cd iu8_queue_bot
    ```

2.  **Configure environment**:
    Create a `.env` file from the example:
    ```bash
    cp .env.example .env
    ```
    Open `.env` and set your `TELE_API_TOKEN`.

3.  **Run**:
    ```bash
    docker-compose up -d --build
    ```

The bot will start and store data in the `db_data` folder.

## 📖 How to Use

1.  **Add the bot** [@QueueBest_bot](https://t.me/QueueBest_bot) to your group.
2.  **Grant permissions**: It is recommended to make the bot an administrator to delete service messages.
3.  **Create a queue**:
    *   Type `/create_queue` or `/plan_queue`.
    *   Enter the queue name.
4.  **Manage**: Use the buttons under the queue message.

## 👨‍💻 Authors

**Original Project (2021):**
*   [Alexey Alexandrov](https://github.com/aaaaaaaalesha) — *Initial work & Core logic*

**Fork & Maintenance (2025):**
*   [Sergey Shorin](https://github.com/shorins) — *Adaptation for modern needs:*
    *   🐳 **Docker**: Full containerization for easy deployment.
    *   👥 **Groups & Topics**: Support for supergroups and threads.
    *   🛠 **Refactoring**: Critical bug fixes (including 0-indexing), code optimization.
    *   🎨 **UI/UX**: Simplified interaction.

---

# 🇷🇺 Русская версия

## ✨ Особенности

*   🚀 **Мгновенное создание очередей**: просто введите команду и название.
*   👥 **Работа в группах и супергруппах**: полная поддержка топиков (Topics).
*   🐳 **Docker**: легкая установка и запуск одной командой.
*   📱 **Интерактивный интерфейс**: кнопки для записи, пропуска и перемещения в очереди.

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
2.  **Дайте права**: рекомендуется сделать бота администратором для удаления служебных сообщений.
3.  **Создайте очередь**:
    *   Введите `/create_queue` или `/plan_queue`.
    *   Введите название очереди.
4.  **Управляйте**: используйте кнопки под сообщением очереди.

## 👨‍💻 Авторы

**Оригинальный проект (2021):**
*   [Alexey Alexandrov](https://github.com/aaaaaaaalesha) — *Идея и базовая логика*

**Fork & Maintenance (2025):**
*   [Sergey Shorin](https://github.com/shorins) — *Адаптация под современные реалии:*
    *   🐳 **Docker**: полная контейнеризация для легкого развертывания.
    *   👥 **Группы и Топики**: поддержка работы в супергруппах и тредах (Topics).
    *   🛠 **Рефакторинг**: исправление критических багов (включая 0-индексацию), оптимизация кода.
    *   🎨 **UI/UX**: упрощение взаимодействия.

---
<p align="center">
  <i>Developed with ❤️ for efficient teamwork.</i>
</p>
