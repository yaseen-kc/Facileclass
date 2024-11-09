# **FacileClass** - A Unified Learning Management System (LMS) 📚

FacileClass is a comprehensive Learning Management System that brings all your learning tools together! 🛠️ It allows educators and students to manage multiple classes in one central location, making the educational experience seamless and efficient. 🚀 With easy setup instructions, anyone can get started in minutes.

## 💡 **Features**

- 📚 **Class Management**: Create and manage multiple classes with ease.
- ☁️ **Google Drive Integration**: Upload and organize files directly to Google Drive using the Drive API.
- 🔄 **Real-Time Updates**: Dynamic content updates with AJAX for smooth interactions.
- 🎨 **Responsive Interface**: A modern and user-friendly UI built with Bootstrap, HTML, and CSS.

## 🛠️ **Setup Instructions**

### 1. **Setup Virtual Environment** 🧰

First, create a virtual environment to isolate project dependencies.

```bash
pip install virtualenv
py -m venv env
.\env\Scripts\activate
```

### 2. **Install Required Python Modules** 📦

After activating the virtual environment, install the necessary Python dependencies from `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 3. **Start the Web Server** 🚀

Once the dependencies are installed, start the development server.

```bash
python manage.py runserver
```

### 4. **Access the Application** 🌐

Once the server is running, open your browser and go to:

[http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the application.

## 🌍 **Hosted Version**

Try the live version of FacileClass hosted on Heroku:

🔗 [FacileClass on Heroku](https://facileclass.herokuapp.com/)

## ⚙️ **Tools and Technologies Used**

- **Django** 🐍: A powerful Python web framework for building web applications.
- **SQLite** 🗃️: A lightweight, serverless database for fast development.
- **Google Drive API** 🧑‍💻: Integration with Google Drive for seamless file storage.
- **Bootstrap** 🖌️: A responsive CSS framework for creating mobile-first websites.
- **HTML, CSS, JavaScript** 🖥️: The foundational web technologies for building the user interface.
- **AJAX** 🔄: For updating parts of the web page without reloading the entire page.

## 🚀 **Future Enhancements** ✨

- 📱 **Mobile App Integration**: A mobile-friendly version of the app.
- 💬 **Real-Time Chat**: Add messaging features between teachers and students.
- 📅 **Calendar Integration**: Sync classes and deadlines with Google Calendar.

## 📜 **License**

This project is open-source and available under the [MIT License](LICENSE).
