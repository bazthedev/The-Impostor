from flask import Flask
from threading import Thread

app = Flask("The Impostor")

@app.route("/")
def home():
  return "<script>window.location.href='https://bazbots.github.io/The-Impostor';</script>"
def run():
  app.run(host="0.0.0.0",port=8080)

def fallback():
  server = Thread(target=run)
  server.start()