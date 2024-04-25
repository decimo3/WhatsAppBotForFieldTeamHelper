CREATE IF NOT EXISTS chat(
  usuario TEXT NOT NULL,
  estagio INT NOT NULL,
  atualizacao DATE NOT NULL
);
CREATE IF NOT EXISTS msgs(
  usuario TEXT NOT NULL,
  estagio INT NOT NULL,
  mensagem TEXT NOT NULL,
  datahora DATE NOT NULL
);
