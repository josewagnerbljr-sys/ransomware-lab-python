# Ransomware em Python | Simulação Controlada para Estudo

Projeto desenvolvido para o desafio de Cybersecurity da DIO, inspirado no repositório-base indicado no curso.

> **Aviso de segurança:** este projeto é uma simulação educacional e foi deliberadamente projetado para não atuar sobre arquivos arbitrários do sistema. O código trabalha exclusivamente dentro do diretório `lab_data/` do próprio projeto, sem persistência, elevação de privilégio, propagação, exfiltração, exclusão de backups ou acesso à rede.

## Objetivo

Demonstrar, em ambiente de laboratório, os conceitos centrais presentes em um cenário de ransomware:

1. descoberta de arquivos de teste;
2. transformação criptográfica reversível;
3. registro dos artefatos processados;
4. recuperação dos dados por meio da chave correta;
5. validação automatizada do comportamento.

A implementação usa AES-GCM por meio da biblioteca `cryptography`. A proteção adicional está na arquitetura: os scripts possuem um diretório-alvo fixo e recusam qualquer caminho fora do laboratório.

## Estrutura

```text
.
├── decrypter.py
├── encrypter.py
├── teste.txt
├── lab_data/
│   └── README_LAB.txt
├── tests/
│   └── test_simulacao.py
├── docs/
│   ├── metodologia.md
│   └── analise_de_seguranca.md
├── images/
│   └── README.md
├── .github/
│   └── workflows/
│       └── tests.yml
├── .gitignore
├── LICENSE
├── requirements.txt
└── README.md
```

## Requisitos

Python 3.10 ou superior.

Instalação da dependência:

```bash
python -m pip install -r requirements.txt
```

## Execução do laboratório

Primeiro execute o criptografador:

```bash
python encrypter.py
```

Ele cria ou utiliza somente os arquivos de demonstração existentes em `lab_data/`, gera uma chave local para o laboratório e produz arquivos com extensão `.locked`.

Depois execute o descriptografador:

```bash
python decrypter.py
```

A chave do laboratório é lida do arquivo local `lab_key.bin`, e os arquivos `.locked` são restaurados.

Para executar os testes:

```bash
python -m unittest discover -s tests -v
```

## O que foi aprendido

### Criptografia simétrica

O projeto utiliza AES-GCM, que oferece confidencialidade e autenticação dos dados. Cada operação utiliza um nonce diferente. A chave de laboratório possui 256 bits.

### Manipulação segura de arquivos

O projeto não recebe um diretório arbitrário na linha de comando. Todos os arquivos são resolvidos a partir da pasta `lab_data/`, e o código verifica que o caminho final permanece dentro desse diretório.

### Recuperação

Como a chave é necessária para a operação reversa, a descriptografia demonstra a importância de gerenciamento, proteção e recuperação de chaves.

### Testes

Os testes verificam:

- criação de chave;
- criptografia de arquivos de laboratório;
- descriptografia correta;
- rejeição de caminhos fora do laboratório;
- integridade dos dados antes e depois do ciclo.

## Relação com o desafio da DIO

O desafio proposto pelo curso solicita um `encrypter.py`, um `decrypter.py`, um `README.md` detalhado e a publicação do projeto em um repositório público do GitHub. A estrutura deste projeto atende esses requisitos e acrescenta testes e documentação técnica.

O repositório-base indicado no desafio é:

https://github.com/cassiano-dio/cibersecurity-desafio-ransomware

A documentação utiliza Markdown compatível com o GitHub.

## Evidências sugeridas para a entrega

Depois de executar o laboratório, podem ser incluídas capturas de tela mostrando:

1. execução do `encrypter.py`;
2. arquivos `.locked` criados em `lab_data/`;
3. execução do `decrypter.py`;
4. recuperação do conteúdo original;
5. execução da suíte de testes.

As capturas devem mostrar apenas o ambiente de laboratório. Nunca inclua credenciais, chaves pessoais ou dados reais.

## Limitações intencionais

Esta versão não implementa mecanismos normalmente associados a malware operacional, como varredura de discos reais, criptografia indiscriminada de documentos do usuário, execução automática, persistência, evasão, movimento lateral, propagação, coleta de credenciais, exfiltração ou negociação de resgate.

Essas limitações são parte da proposta educacional segura do projeto e não reduzem o valor do laboratório para estudar criptografia, manipulação de arquivos, engenharia de software e controles defensivos.

## Conclusão

O laboratório reproduz o conceito essencial do desafio em uma área isolada e reversível. O resultado é adequado para estudo, demonstração em aula e publicação no GitHub sem transformar o projeto em uma ferramenta de dano real.

## Referências

- Repositório-base da DIO: https://github.com/cassiano-dio/cibersecurity-desafio-ransomware
- Documentação do GitHub Markdown: https://docs.github.com/pt/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
