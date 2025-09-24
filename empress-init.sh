#!/bin/bash
echo "[EMPRESS] Boot sequence triggered. Resurrection loop initializing…" >> ~/empress/logs/boot.log
nohup python ~/empress/throne/session_resurrection_loop.py &>> ~/empress/logs/resurrection.log &
nohup python ~/empress/throne/cloud_sync_trigger.py &>> ~/empress/logs/cloud_sync.log &
