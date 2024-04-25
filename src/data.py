import sqlite3
class Data:
  def __init__(self) -> None:
    self.conecao = sqlite3.connect('base.db')
  def Escrever(self) -> None:
    pass
  def Leitura(self) -> None:
    pass