# TinyML-frontend

![GitHub Actions](https://github.com/TinyMLaas/TinyML-frontend/actions/workflows/frontend_pylint.yml/badge.svg)

frontend for [TinyMLaaS](https://github.com/JeHugawa/TinyMLaaS-main).

## Dependecies

Depends on package `usbutils`.

On Debian-based systems install it with:

```bash
apt install usbutils
```

## USB-detection

The frontend uses the external command `lsusb` to find suitable usb-devices.

This means that the frontend can't natively find usb devices on windows and needs to be run in a docker container for this feature.

## Running

Run backend from [this repository](https://github.com/TinyMLaas/TinyML-backend)

Activate virtual environment with:

```
source /venv/bin/activate
```

Install dependencies with:

```
pip install requirements.txt
```

Create an .env file in frontend root directory that points to backend:

```
BACKEND_URL = "http://localhost:8000"
```

Run frontend with:

```
streamlit run TinyMLaaS.py
```

## Testing

This project uses Robot Framework to run end-to-end testing. For testing you need to have both the backend and frontend running. Before running frontend, environment variable _ROBOT_TESTS_ 
should be set to _true_. On bash, you can do that with

```
ROBOT_TESTS=true && export ROBOT_TESTS
```

This makes it that the robot tests don't access actual usb-devices, but rather use sepcifically defined mock data.

In the backend you will need to have enough test data in the database to run the robot tests. You can set up the database in the backend folder with

```
touch tiny_mlaas.db
sqlite3 tiny_mlaas.db < schema.sql
sqlite3 tiny_mlaas.db < populate.sql
```

Run Robot Framework tests with:

```
robot -d robot_output tests/
```
The -d flag directs the robot test outputs, which can be quite generous, to a named folder. 



