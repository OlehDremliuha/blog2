# Simple Blog - Django Web Application

Це простий веб-додаток блогу, створений у рамках навчального курсу. Додаток дозволяє користувачам реєструватися, створювати записи, залишати коментарі та керувати власним профілем.

## 🔧 Використані технології

- **Мова програмування:** Python 3.x  
- **Фреймворк:** Django 
- **База даних:** SQLite 
- **HTML/CSS:** Django templates з Bootstrap  
- **Інші бібліотеки:**
  - Pillow 
  - Django Messages 

## 💡 Основна функціональність

- ✅ Реєстрація та вхід/вихід користувачів
- ✅ Скидання паролю через email
- ✅ Створення, редагування та видалення записів (posts)
- ✅ Додавання коментарів до постів
- ✅ Перегляд та редагування профілю користувача

 ## 🚀 Як запустити проект локально

1. Клонувати репозиторій:

git clone https://github.com/your-username/blog-project.git
cd blog-project
Створити та активувати віртуальне середовище:

python -m venv venv
source venv/bin/activate  # або venv\Scripts\activate на Windows
Встановити залежності:

pip install -r requirements.txt
Застосувати міграції:

python manage.py migrate
Запустити сервер:

python manage.py runserver
Відкрити браузер і перейти за адресою:
http://127.0.0.1:8000/

