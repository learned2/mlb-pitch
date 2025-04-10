import requests

url = "http://127.0.0.1:5000/predict"

payload = {
    "stand": 1,
    "balls": 2,
    "strikes": 1,
    "inning": 6,
    "outs_when_up": 1,
    "on_1b": 1,
    "on_2b": 0,
    "on_3b": 0,
    "score_diff": -1,
    "pitcher_id": 654321
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Response:", response.json())
