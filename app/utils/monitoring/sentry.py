# app/utils/monitoring/sentry.py
import os
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration


def traces_sampler(sampling_context):
    # Customize your sampling logic here if needed
    # return a number between 0 and 1 or a boolean
    return 1.0


def configure_sentry():
    sentry_sdk.init(
        dsn=os.getenv("SENTRY_DSN"),
        integrations=[FlaskIntegration()],
        traces_sample_rate=1.0,
        traces_sampler=traces_sampler  # Optional if you want dynamic sampling
    )
