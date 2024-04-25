```mermaid
graph TD
apresentacao --> alternativas
  alternativas --> reclamacao
    reclamacao --> transito
      transito --> identificacao
    reclamacao --> comportamento
      comportamento --> identificacao
  alternativas --> enaltecer
    enaltecer --> empresa
      empresa --> identificacao
    enaltecer --> colaborador
      colaborador --> identificacao
identificacao --> observacao
observacao --> finalizacao
```