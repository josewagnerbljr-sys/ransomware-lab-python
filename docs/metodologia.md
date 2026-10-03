# Metodologia do projeto

## 1. Levantamento

O desafio propõe um criptografador e um descriptografador em Python, acompanhados de documentação e publicação em GitHub.

## 2. Escopo seguro

O projeto foi estruturado como laboratório fechado. O diretório alvo é fixo, arquivos de teste são sintéticos e os scripts não possuem recursos para atuar fora da área definida.

## 3. Criptografia

AES-GCM foi escolhido por fornecer confidencialidade e autenticação. O nonce de 12 bytes é gerado aleatoriamente para cada arquivo.

O payload gravado segue a forma:

```text
MAGIC | NONCE | CIPHERTEXT+TAG
```

## 4. Descriptografia

A rotina valida o marcador do formato, extrai nonce e ciphertext e usa a mesma chave de laboratório para autenticar e recuperar o conteúdo.

## 5. Validação

A suíte de testes executa o ciclo completo e verifica também a rejeição de caminhos que não pertençam ao laboratório.

## 6. Decisões técnicas

A retenção do arquivo original foi intencional para permitir comparação antes e depois e evitar destruição de dados. A chave fica no próprio laboratório apenas porque o objetivo é demonstrar o ciclo criptográfico, não ensinar gerenciamento inseguro de segredos.
