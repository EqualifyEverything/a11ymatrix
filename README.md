# 🚀 A11y Uppies Manager 🌟
_TODO: Change name to matrix__
Welcome to the A11y Uppies Manager, a creative and powerful solution for managing your uppies! 🎉

## 🎯 Overview
A11y Uppies Manager is designed to handle the communication between the main application and Franklin API, managing the processing of URLs and adjusting the number of workers for optimal performance. 🚀

## 💡 Features
- Start and stop uppies processing with API endpoints
- Automatically adjust the number of workers based on response time
- Detailed logging with adjustable log levels
- Dockerized for easy deployment 🐳

## 🛠️ Installation
Prerequisites
Docker installed on your system

### Steps
1. Clone the repository:

```bash
git clone https://github.com/your-repo/a11y-uppies-manager.git
cd a11y-uppies-manager
```

2. Build the Docker image:

```bash
docker build -t a11y-uppies-manager .
```

3. Run the Docker container:

```bash
docker run -d -p 8087:8087 --name uppies-manager --env FRANKLIN_URL=http://franklin.whatever --env LOG_LEVEL=INFO a11y-uppies-manager
```
Replace http://franklin.whatever with your Franklin API URL and set the LOG_LEVEL to your desired level.

## 📚 Usage
### API Endpoints
- Start uppies processing:

```bash
POST /uppies/start
```

- Stop uppies processing:

```bash
POST /uppies/stop
```

- Get the status of uppies processing:

```bash
GET /status
```

## ⚙️ Configuration
Use the following environment variables to configure the A11y Uppies Manager:

- `APP_PORT`: Port on which the application will run (default: 8087)
- `FRANKLIN_URL`: URL of the Franklin API
- `LOG_LEVEL`: Log level for the application (default: INFO)

## 📖 Documentation
For a detailed explanation of the code and its functionality, check the source files, which are well-documented with inline comments.

TODO: Docs & Such

## 👩‍💻👨‍💻 Contributing
We love contributions! If you have any ideas or suggestions, please feel free to create an issue or submit a pull request. Let's make the A11y Uppies Manager even better together! 🤝

## 🎉 Final Thoughts
We hope you enjoy using A11y Uppies Manager as much as we enjoyed building it! Let's make the web more accessible for everyone! 🌐🦾

Happy coding! 🎉👩‍💻👨‍💻
