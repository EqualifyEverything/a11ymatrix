# app/utils/monitoring/prometheus.py
from .logger import logger
from prometheus_client import Counter, Histogram, Gauge


def configure_prometheus(app):
    http_request_duration_seconds = Histogram(
        'http_request_duration_seconds', 'HTTP request latencies',
        ['endpoint']
    )
    http_requests_total = Counter(
        'http_requests_total', 'Total HTTP requests',
        ['method', 'endpoint', 'status']
    )
    in_flight_requests = Gauge(
        'in_flight_requests', 'In-flight HTTP requests',
        multiprocess_mode='livesum'
    )