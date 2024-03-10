#!/bin/bash

LOG_FILE="usage_log.txt"

echo "Timestamp,CPU Usage (%),Memory Usage (MB)" > $LOG_FILE

while true; do
    TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
    CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | awk -F. '{print $1}')
    MEMORY_USAGE=$(free -m | grep Mem | awk '{print $3}')

    echo "$TIMESTAMP,$CPU_USAGE,$MEMORY_USAGE" >> $LOG_FILE

    sleep 5
done
