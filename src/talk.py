class Talk:
  def __init__(self) -> None:
    pass
  def apresentacao(self) -> list[str]:
    return [
      "Bom dia, você está falando com o assistente de atendimento.",
      "Faremos agora um pré-atendimento. Sobre o que deseja falar?",
      "Digite `1` para reclamação ou `2` para eligios."
    ]
  def identificacao(self) -> list[str]:
    return [
      "Por favor, nos conte algum detalhe para que achemos os responsáveis mais facilmente:",
      "Data, local, caracteristicas físicas, nome do colaborador e/ou a placa do veículo."
    ]
  def descrever(self) -> list[str]:
    return [
      "Por favor, nos dê os detalhes",
      "Pode escrever o quanto quiser, mas tente mandar tudo em uma mensagem só.",
      "Mas fique tranquilo(a) que todas as mensagens serão consideradas."
    ]
  def agradecer_finalizacao(self) -> list[str]:
    return [
      "Ficamos felizes que esteja satisfeito com o nosso atendimento.",
      "Prezamos pelo nível de excelência do atendimento dos nossos clientes."
    ]
  def reclamacao_finalizacao(self) -> list[str]:
    return [
      "Lamentamos por qualquer ocorrido desagradável com algum colaborador da nossa empresa.",
      "Faremos o possível para identificar e resolver o problema."
    ]
  def finalizacao_finalizacao(self) -> list[str]:
    return [
      "Se quiser adicionar mais alguma informação, fique a vontade para escrever.",
      "Em breve algum representante nosso entrará em contato contigo."
    ]