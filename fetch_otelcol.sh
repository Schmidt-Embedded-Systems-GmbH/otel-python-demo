#!/bin/bash

set +x

wget --verbose 'https://github.com/open-telemetry/opentelemetry-collector-releases/releases/download/v0.106.1/otelcol_0.106.1_linux_amd64.tar.gz' -O otelcol.tar.gz

tar -xvzf otelcol.tar.gz otelcol 
