#region imports
from fastapi import FastAPI
from model import Model
#endregion imports

app = FastAPI()

@app.post("/")
def root(body: Model):
  """Function that will receive all requests"""
  print(f"Request head: {body.head}")
  print(f"Request body: {body.body}")
  body.body = "Wellcome to WhatsApp chatbot!"
  return body
