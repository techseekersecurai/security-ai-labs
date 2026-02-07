#!/bin/bash

set -e #stop if any command fails


TARGET=$1
LOG_FILE=$2

echo "==========================="
echo " Security Automation Check"
echo "==========================="


echo ""
echo ">>> Running Port Scan"

cd tools/portscanner
poetry run portscan $TARGET


echo ""
echo ">>> Running Log Scan"

cd ../logscan
poetry run logscan data/$LOG_FILE

echo ""
echo ">>> Done"





