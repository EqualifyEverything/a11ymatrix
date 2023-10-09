# app/utils/monitoring/pyroscope.py
# https://grafana.com/docs/pyroscope/latest/configure-client/language-sdks/python/
import pyroscope
import os


def configure_pyroscope():
    pyroscope.configure(
        application_name=os.getenv("PYROSCOPE_APPLICATION_NAME"),
        server_address=os.getenv("PYROSCOPE_SERVER"),
        auth_token=os.getenv("PYROSCOPE_AUTH_TOKEN"),
        detect_subprocesses=True,
        oncpu=True,
        gil_only=True,
        log_level=os.getenv("LOG_LEVEL")
    )
    print('Pyroscope Configured')

