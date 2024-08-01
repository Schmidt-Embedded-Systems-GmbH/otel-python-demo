#!/bin/bash

./otelcol-contrib --config otelcol.yaml & 
otelcol_pid=$?

source .venv/bin/activate && \
export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true && \
opentelemetry-instrument \
    --traces_exporter otlp \
    --metrics_exporter otlp \
    --logs_exporter otlp \
    --service_name dice-server \
    flask run -p 8080
    
kill -9 $otelcol_pid
