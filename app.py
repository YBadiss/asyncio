from flask import Flask
import time

app = Flask(__name__)

@app.route("/<int:times>")
def hello(times):
    sleep_time = 0.01 * times
    print(f"Sleeping for {sleep_time} secs...")
    time.sleep(sleep_time)
    return f"Hello World! Slept {sleep_time} secs"

