# app/utils/monitoring/pyroscope.py
import pyroscope
import os


def configure_pyroscope():
    pyroscope.configure(
        application_name=os.getenv("PYROSCOPE_APPLICATION_NAME"),
        server_address=os.getenv("PYROSCOPE_SERVER"),
        auth_token=os.getenv("PYROSCOPE_AUTH_TOKEN"),
    )
    print('Pyroscope Configured')
