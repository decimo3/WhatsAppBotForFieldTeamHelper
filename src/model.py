from pydantic import BaseModel

class Model(BaseModel):
  head: str
  body: str