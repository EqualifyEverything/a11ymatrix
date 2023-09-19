# app/utils/monitoring/__init__.py
from .sentry import configure_sentry
from .pyroscope import configure_pyroscope
from .prometheus import configure_prometheus

def start_monitoring(app):
    configure_sentry()
    configure_pyroscope()
    configure_prometheus(app)
