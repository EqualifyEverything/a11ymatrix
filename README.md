# A11yMatrix

A11yMatrix is a powerful accessibility testing tool that helps developers and testers identify and resolve accessibility issues in their web applications. This repository includes the core functionality, as well as a front-end web application to provide a seamless user experience.

## 🎯 Overview

A11yData processes and monitors web accessibility data, leveraging RabbitMQ for processing and monitoring web pages using tools such as Axe and Uppies.

## 💡 Features

- Web accessibility data processing
- RabbitMQ integration for message processing
- Monitoring and managing the status of the processing queues
- Dockerized application for easy deployment

## 🛠️ Installation

Prerequisites:
- Docker
- RabbitMQ server with credentials

| Docker env var   | Default value         | Description                 |
|------------------|-----------------------|-----------------------------|
| APP_PORT         | 8087                  | Application port            |
| DB_HOST          | postgres              | Database host               |
| DB_PORT          | 5432                  | Database port               |
| DB_USER          | a11ydata              | Database user               |
| DB_PASSWORD      | a11yAllTheThings!     | Database password           |
| DB_NAME          | a11ydata              | Database name               |
| LOG_LEVEL        | INFO                  | Logging level               |



## 📚 Usage

Start and stop the RabbitMQ monitoring using the `/rabbit/ears/start` and `/rabbit/ears/stop` endpoints.

Manage Uppies processing using the `/uppies/start` and `/uppies/stop` endpoints.

## 📁 Repo Overview

- Dockerfile: Docker configuration file for building the application image
- src/endpoints.py: Flask application with API endpoints
- src/send.py: Functions for sending messages to the queues
- src/utils/process.py: Uppies processing script
- src/utils/yeet_uppies.py: Uppies processing control
- src/utils/auth.py: Helper function for RabbitMQ authentication
- src/data/: Contains the database access and query execution logic.
- access.py: Defines the connection class for managing database connections.
- select.py: Contains functions for executing select queries.
- src/utils/: Contains utility functions and configurations.
- watch.py: Sets up and configures the logger used throughout the application.
- README.md: This file, which provides an overview of the project and instructions for getting started.

## 👩‍💻👨‍💻 Contributing

We love contributions! If you have any ideas or suggestions, please feel free to create an issue or submit a pull request. Let's make A11yData even better together! 🤝

## 🎉 Final Thoughts

We hope you enjoy using A11yData as much as we enjoyed building it! Let's work together to make the web a more accessible place for all.

Happy coding! 🎉👩‍💻👨‍💻

## 📄 License

A11yData is released under the GPL-3.0 License.