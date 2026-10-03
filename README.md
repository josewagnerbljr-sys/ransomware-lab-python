# 🔐 Ransomware Simulation Lab · Python · DIO Cybersecurity Challenge

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Cryptography](https://img.shields.io/badge/AES--256--GCM-Criptografia-critical?style=for-the-badge&logo=keybase&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![DIO](https://img.shields.io/badge/DIO-Cybersecurity-E02D27?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyem0tMiAxNWwtNS01IDEuNDEtMS40MUwxMCAxNC4xN2w3LjU5LTcuNTlMMTkgOGwtOSA5eiIvPjwvc3ZnPg==)
![CI](https://img.shields.io/github/actions/workflow/status/josewagnerbljr-sys/ransomware-lab-python/tests.yml?style=for-the-badge&label=CI%20Tests)
![Simulação](https://img.shields.io/badge/Modo-Simulação%20Controlada-orange?style=for-the-badge)

</div>

---

> [!CAUTION]
> **⚠️ AVISO DE SEGURANÇA E ÉTICA**
>
> Este projeto é uma **simulação educacional controlada**.
> O código opera **exclusivamente** sobre arquivos sintéticos dentro do diretório `lab_data/` do próprio repositório.
> Não há acesso à rede, não há persistência, não há elevação de privilégio, não há propagação e não há exclusão de arquivos originais.
> **Proibido utilizar ou adaptar este código para finalidades maliciosas ou fora do contexto educacional.**

---

## 📋 Sumário

- [Sobre o Projeto](#-sobre-o-projeto)
- [Por que um Simulador e não uma Ferramenta Real?](#-por-que-um-simulador-e-não-uma-ferramenta-real)
- [Arquitetura e Decisões Técnicas](#-arquitetura-e-decisões-técnicas)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Requisitos](#-requisitos)
- [Como Executar o Laboratório](#-como-executar-o-laboratório)
- [Suíte de Testes](#-suíte-de-testes)
- [Pipeline de CI/CD](#-pipeline-de-cicd)
- [Controles de Contenção e Modelo de Segurança](#-controles-de-contenção-e-modelo-de-segurança)
- [O que foi Aprendido](#-o-que-foi-aprendido)
- [Relação com o Desafio DIO](#-relação-com-o-desafio-dio)
- [Referências e Recursos](#-referências-e-recursos)
- [Autor](#-autor)

---

## 🎯 Sobre o Projeto

Este repositório contém a entrega do **Desafio de Cybersecurity da DIO — Ransomware em Python**, com foco no estudo dos conceitos centrais de criptografia e recuperação de arquivos em um ambiente de laboratório **completamente isolado e seguro**.

O projeto implementa os dois artefatos exigidos pelo desafio — `encrypter.py` e `decrypter.py` — utilizando **AES-256 no modo GCM** (Galois/Counter Mode), que oferece simultaneamente confidencialidade e autenticação de dados. A implementação vai além do mínimo exigido: conta com uma suíte de testes automatizados, documentação técnica complementar e um pipeline de integração contínua no GitHub Actions.

O projeto foi desenvolvido com foco em **segurança por design**: o código aplica validação de caminho canônico, de modo que qualquer tentativa de processar arquivos fora do diretório de laboratório é rejeitada explicitamente pelo próprio runtime.

---

## 🛡️ Por que um Simulador e não uma Ferramenta Real?

Esta é a decisão mais importante deste projeto — e merece uma explicação técnica e ética rigorosa.

### 1. Responsabilidade em Open Source

Quando um projeto é publicado em um repositório **público** em plataformas como o GitHub, seu código torna-se imediatamente acessível a qualquer pessoa no mundo. Um ransomware funcional — mesmo que desenvolvido com intenção educacional — representa um vetor de dano real: qualquer agente de má-fé pode clonar, adaptar e implantar o código em minutos. A decisão de limitar operacionalmente o projeto é, portanto, uma **obrigação ética do autor**, não uma restrição do desafio.

> *"Com grandes poderes vêm grandes responsabilidades."*
> A publicação aberta de ferramentas de ataque funcionais é, na prática, a criação de uma arma de uso genérico — independentemente da intenção original.

### 2. Valor Educacional Não Depende de Armas Funcionais

O objetivo declarado do desafio é compreender o **fluxo de operação** de um ransomware: descoberta de arquivos, transformação criptográfica, registro de artefatos e recuperação. Todos esses conceitos são completamente estudáveis em um laboratório isolado com dados sintéticos. O `encrypter.py` e o `decrypter.py` deste projeto implementam o **ciclo técnico completo** — o que oferece o mesmo aprendizado sem criar uma ferramenta de dano operacional.

### 3. Conformidade com Políticas de Plataformas e Legislação

A publicação de ferramentas de malware funcional viola os Termos de Uso do GitHub (Acceptable Use Policy, Seção 4), pode caracterizar crime de invasão de dispositivo informático nos termos da **Lei nº 12.737/2012 (Lei Carolina Dieckmann)** e do **Marco Civil da Internet (Lei nº 12.965/2014)**, e expõe o autor a responsabilidade civil e criminal mesmo que o código nunca seja diretamente utilizado por terceiros.

### 4. Modelo de Open Source Responsável

Projetos de cibersegurança publicados em ambiente aberto devem seguir os princípios de **Responsible Disclosure** e **Defensive Security**. A comunidade de segurança distingue claramente entre:

| Categoria | Descrição | Este Projeto |
|---|---|---|
| **PoC (Proof of Concept)** | Demonstra a viabilidade técnica de um ataque | Parcialmente — ciclo criptográfico local |
| **Exploit funcional** | Arma pronta para uso em sistemas reais | ❌ Não implementado |
| **Lab educacional** | Reproduz conceitos em ambiente isolado | ✅ Exatamente o que este projeto é |

### 5. Alinhamento com as Melhores Práticas da DIO

O desafio proposto pela DIO não exige nem incentiva a criação de uma ferramenta maliciosa operacional. O enunciado pede `encrypter.py`, `decrypter.py` e documentação — todos presentes neste projeto. A adoção do modelo de simulação controlada **excede os requisitos** enquanto mantém a integridade ética do portfólio do desenvolvedor.

---

## 🏗️ Arquitetura e Decisões Técnicas

### Algoritmo de Criptografia: AES-256-GCM

O projeto utiliza AES no modo GCM (Galois/Counter Mode), escolhido por três razões:

1. **Confidencialidade** — o bloco de dados é cifrado com uma chave de 256 bits.
2. **Autenticação** — o GCM produz uma tag de autenticação que detecta qualquer adulteração do ciphertext.
3. **Nonce único por arquivo** — cada operação gera um nonce aleatório de 12 bytes, eliminando a reutilização de chave com o mesmo vetor de inicialização.

### Formato do Payload Gravado

Cada arquivo criptografado segue uma estrutura binária determinística:

```
┌─────────────────────────────────────────────────────────────────┐
│  MAGIC (8 bytes)  │  NONCE (12 bytes)  │  CIPHERTEXT + TAG      │
│  "DIO-LAB1"       │  aleatório         │  AES-GCM output        │
└─────────────────────────────────────────────────────────────────┘
```

O prefixo `DIO-LAB1` identifica inequivocamente arquivos do laboratório durante a descriptografia, impedindo a tentativa de descriptografar arquivos arbitrários com formato inválido.

### Sandbox de Caminho

A função `_safe_lab_path()` em ambos os scripts resolve o caminho **canônico** do arquivo alvo e verifica que ele pertence à hierarquia de `lab_data/`. Qualquer tentativa de path traversal (`../`, caminhos absolutos externos, symlinks para fora do diretório) é bloqueada com `ValueError` antes que qualquer I/O ocorra.

```python
def _safe_lab_path(path: Path) -> Path:
    candidate = path.resolve()
    lab_root = LAB_DIR.resolve()
    if candidate == lab_root or lab_root not in candidate.parents:
        raise ValueError("Operação bloqueada: arquivo fora do diretório de laboratório.")
    return candidate
```

### Gerenciamento de Chave

A chave de laboratório (`lab_key.bin`) é gerada uma única vez e reutilizada nas execuções subsequentes. Este comportamento é **intencional para fins educacionais** — permite demonstrar o ciclo completo de criptografia e recuperação. O arquivo de chave está listado no `.gitignore` e **nunca deve ser commitado**.

---

## 📁 Estrutura do Projeto

```text
ransomware-lab-python/
│
├── encrypter.py              # Criptografador de laboratório (AES-256-GCM)
├── decrypter.py              # Descriptografador de laboratório
├── teste.txt                 # Arquivo na raiz — demonstra que o encrypter NÃO toca arquivos fora de lab_data/
│
├── lab_data/                 # 🔒 Diretório de laboratório — único alvo dos scripts
│   └── README_LAB.txt        # Aviso: apenas arquivos sintéticos
│   └── lab_key.bin           # ⚠️ Gerado em runtime — ignorado pelo .gitignore
│
├── tests/
│   └── test_simulacao.py     # Suíte de testes automatizados (unittest)
│
├── docs/
│   ├── metodologia.md        # Metodologia e decisões técnicas detalhadas
│   └── analise_de_seguranca.md  # Análise de riscos, controles e lições defensivas
│
├── images/                   # Capturas de tela da execução do laboratório
│   └── README.md
│
├── .github/
│   └── workflows/
│       └── tests.yml         # Pipeline CI — GitHub Actions (Python 3.11)
│
├── .gitignore                # Exclui lab_key.bin e *.locked
├── LICENSE                   # MIT
├── requirements.txt          # cryptography>=42,<48
└── README.md                 # Este documento
```

> **Por que `teste.txt` está na raiz?**
> Para demonstrar que o `encrypter.py` **ignora arquivos fora de `lab_data/`**. Este arquivo jamais é processado pelos scripts — serve como evidência visual do comportamento do sandbox de caminho.

---

## ⚙️ Requisitos

- **Python 3.10 ou superior** (testado com 3.11)
- Biblioteca `cryptography` (instalada via `requirements.txt`)

Instalar dependências:

```bash
python -m pip install -r requirements.txt
```

---

## 🚀 Como Executar o Laboratório

### Passo 1 — Preparar os arquivos de demonstração

Copie arquivos de texto sintéticos para o diretório `lab_data/`. **Nunca coloque documentos reais nesta pasta.**

```bash
# Exemplo: criar arquivos sintéticos de demonstração
echo "Arquivo de demonstração A" > lab_data/demo_a.txt
echo "Arquivo de demonstração B" > lab_data/demo_b.txt
echo "Conteúdo sintético C"     > lab_data/demo_c.txt
```

### Passo 2 — Executar o Criptografador

```bash
python encrypter.py
```

Saída esperada:

```
=== Simulação de criptografia controlada ===
Diretório permitido: /caminho/para/lab_data
Arquivos encontrados: 3
[OK] demo_a.txt -> demo_a.txt.locked
[OK] demo_b.txt -> demo_b.txt.locked
[OK] demo_c.txt -> demo_c.txt.locked
Chave do laboratório salva em lab_data/lab_key.bin
Nenhum arquivo original foi apagado.
```

O `encrypter.py`:
- Cria ou reutiliza a chave `lab_key.bin`
- Gera um arquivo `.locked` para cada arquivo elegível
- **Preserva os arquivos originais** (nenhum dado é destruído)

### Passo 3 — Verificar os Artefatos

```bash
ls -lh lab_data/
```

Os arquivos `.locked` são visualmente diferentes dos originais em tamanho (sobrecarga do nonce + tag GCM) e conteúdo binário ilegível.

### Passo 4 — Executar o Descriptografador

```bash
python decrypter.py
```

Saída esperada:

```
=== Simulação de recuperação de arquivos ===
[OK] demo_a.txt.locked -> demo_a.txt
[OK] demo_b.txt.locked -> demo_b.txt
[OK] demo_c.txt.locked -> demo_c.txt
Arquivos de demonstração restaurados com a chave do laboratório.
```

### Passo 5 — Capturar Evidências

Após a execução, tire capturas de tela mostrando:

1. Execução do `encrypter.py` com os arquivos `.locked` gerados
2. Estado de `lab_data/` antes e depois
3. Execução do `decrypter.py` e restauração dos arquivos
4. Execução dos testes automatizados

Salve as capturas em `images/` antes de fazer o commit final.

---

## 🧪 Suíte de Testes

Execute todos os testes com:

```bash
python -m unittest discover -s tests -v
```

### Testes Implementados

| Teste | Descrição | O que verifica |
|---|---|---|
| `test_round_trip` | Ciclo completo cifrar → decifrar | Conteúdo recuperado é idêntico ao original |
| `test_key_is_256_bits` | Tamanho e persistência da chave | Chave tem exatamente 32 bytes; reutilizada em chamadas subsequentes |
| `test_path_escape_is_rejected` | Tentativa de path traversal | `ValueError` para arquivos fora de `lab_data/` |
| `test_locked_format_is_not_plaintext` | Integridade da criptografia | Plaintext original não está presente no arquivo `.locked` |

---

## 🔄 Pipeline de CI/CD

O repositório inclui um workflow `.github/workflows/tests.yml` que executa automaticamente toda a suíte de testes a cada `push` e `pull_request`.

```yaml
on:
  push:
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: python -m pip install -r requirements.txt
      - run: python -m unittest discover -s tests -v
```

O status do pipeline é exibido pelo badge na parte superior deste README.

---

## 🔒 Controles de Contenção e Modelo de Segurança

A tabela abaixo documenta todos os controles deliberadamente implementados para garantir que a simulação permaneça segura:

| Controle | Implementação | Status |
|---|---|---|
| Diretório alvo fixo | `LAB_DIR = BASE_DIR / "lab_data"` | ✅ |
| Validação de caminho canônico | `Path.resolve()` + verificação de hierarquia | ✅ |
| Exclusão da chave do conjunto elegível | `path.name == KEY_FILE.name` → rejeitado | ✅ |
| Sem rede | Nenhum socket, nenhuma chamada HTTP | ✅ |
| Sem execução automática | Requer `python encrypter.py` manual | ✅ |
| Sem persistência | Nenhum serviço, nenhuma chave de registro | ✅ |
| Sem elevação de privilégio | Operações exclusivamente em nível de usuário | ✅ |
| Sem exclusão do original | Arquivo original preservado após criptografia | ✅ |
| Sem acesso a diretórios do sistema | Path traversal bloqueado explicitamente | ✅ |
| Chave excluída do versionamento | `.gitignore` inclui `lab_key.bin` e `*.locked` | ✅ |

### O que Este Projeto NÃO Implementa (Por Design)

Esta simulação **não contém** e **nunca deve receber**:

- Varredura de discos reais ou diretórios do usuário
- Conexão com servidor C2 (Command and Control)
- Execução automática via agendador de tarefas ou autorun
- Propagação via rede ou dispositivos removíveis
- Evasão de antivírus ou sandbox
- Exfiltração de dados
- Negociação de resgate
- Exclusão de shadow copies ou backups

---

## 📚 O que foi Aprendido

### Criptografia Simétrica com AES-GCM

AES-GCM combina o modo CTR (que oferece criptografia por fluxo paralelo) com o campo de autenticação Galois, gerando uma tag de integridade que detecta qualquer alteração no ciphertext. Esta propriedade é chamada de **AEAD** (Authenticated Encryption with Associated Data) e é o padrão moderno para criptografia simétrica.

### Importância do Nonce

O nonce (number used once) garante que duas criptografias do mesmo plaintext com a mesma chave produzam outputs diferentes. A reutilização de nonce com AES-GCM é catastrófica: permite recuperar a chave. Por isso, o projeto gera `os.urandom(12)` para cada arquivo individualmente.

### Gerenciamento de Chaves e Recuperação

A descriptografia exige a **mesma chave** utilizada na criptografia. Isso demonstra por que a gestão de chaves é o ponto mais crítico em qualquer sistema de criptografia — perder a chave significa perda permanente dos dados. Em um ambiente corporativo real, isso é abordado com HSMs (Hardware Security Modules), cofres de segredos (HashiCorp Vault, AWS KMS) e processos formais de recuperação.

### Testes em Segurança

Os testes automatizados verificam não apenas o fluxo feliz (happy path), mas também condições adversariais: o teste `test_path_escape_is_rejected` simula um cenário de path traversal e confirma que o sistema rejeita a operação antes de qualquer leitura de arquivo.

### Controles Defensivos Relacionados

Indicadores de comprometimento (IoCs) monitorados por soluções EDR incluem: alteração massiva de extensões de arquivos, picos anômalos de escrita em disco, processos que abrem um número incomum de handles de arquivo e tentativas de deletar volume shadow copies. Esses padrões são diretamente observáveis ao executar o laboratório com ferramentas como Process Monitor, strace ou auditd.

---

## 🎓 Relação com o Desafio DIO

| Requisito do Desafio | Implementação Neste Projeto |
|---|---|
| `encrypter.py` | ✅ Presente — AES-256-GCM com sandbox de caminho |
| `decrypter.py` | ✅ Presente — validação de magic bytes e recuperação completa |
| `README.md` detalhado | ✅ Este documento |
| Repositório público no GitHub | ✅ |
| Arquivos relevantes para compreensão | ✅ `docs/`, `tests/`, `.github/workflows/` |
| Capturas de tela (opcional) | 📁 Pasta `images/` reservada |

**Repositório-base do desafio:** [cassiano-dio/cibersecurity-desafio-ransomware](https://github.com/cassiano-dio/cibersecurity-desafio-ransomware)

---

## 📖 Referências e Recursos

- [Repositório-base DIO — cassiano-dio/cibersecurity-desafio-ransomware](https://github.com/cassiano-dio/cibersecurity-desafio-ransomware)
- [Documentação da biblioteca `cryptography` — PyCA](https://cryptography.io/en/latest/)
- [NIST SP 800-38D — Recommendation for Block Cipher Modes: GCM](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf)
- [GitHub Markdown — Documentação oficial](https://docs.github.com/pt/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Acceptable Use Policy — GitHub](https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies)
- [Lei nº 12.737/2012 — Crimes Cibernéticos (BR)](https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2012/lei/l12737.htm)
- [Lei nº 12.965/2014 — Marco Civil da Internet (BR)](https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12965.htm)
- [Perfil DIO do autor](https://web.dio.me/users/consultoriablanco8)

---

## 👤 Autor

<div align="center">

**José Wagner Blanco Júnior**
Principal AI Systems Architect | Executive Manager
Fundador e Arquiteto Principal — OMNIA ASCENDRA AI Platform

</div>

---

### 📬 Contatos e Presença Online

| Plataforma | Link |
|---|---|
| 📧 **E-mail** | [consultoriablanco8@gmail.com](mailto:consultoriablanco8@gmail.com) |
| 💼 **LinkedIn** | [linkedin.com/in/blancoconsultoria](https://linkedin.com/in/blancoconsultoria) |
| 🐙 **GitHub** | [github.com/josewagnerbljr-sys](https://github.com/josewagnerbljr-sys) |
| 🎓 **DIO** | [web.dio.me/users/consultoriablanco8](https://web.dio.me/users/consultoriablanco8) |
| 🌐 **Site** | [chefblanco.com.br](https://chefblanco.com.br) |
| 🔗 **Beacons** | [beacons.ai/blanco.sys](https://beacons.ai/blanco.sys) |
| 📱 **WhatsApp** | [(44) 99158-5033](https://wa.me/5544991585033) |
| 🛒 **Catálogo** | [wa.me/c/554491585033](https://wa.me/c/554491585033) |
| 📢 **Canal WhatsApp** | [whatsapp.com/channel/0029VbCg8mMHQbS8zrKhyE0W](https://whatsapp.com/channel/0029VbCg8mMHQbS8zrKhyE0W) |
| 🐦 **X (Twitter)** | [x.com/JWBlancoJrSys](https://x.com/JWBlancoJrSys) |
| 📘 **Facebook** | [facebook.com/profile.php?id=61593244118097](https://facebook.com/profile.php?id=61593244118097) |
| 📸 **Instagram** | [instagram.com/chef_j.blanco](https://instagram.com/chef_j.blanco) |
| 🏆 **HubStaff Talent** | [hubstafftalent.net/profiles/jose-wagner-blanco-junior](https://hubstafftalent.net/profiles/jose-wagner-blanco-junior) |
| 📞 **Telefone** | (44) 99158-5033 |

---

<div align="center">

Desenvolvido como parte da **Formação em Cybersecurity** da [Digital Innovation One — DIO](https://www.dio.me)

![Made with Python](https://img.shields.io/badge/Feito%20com-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Made in Brazil](https://img.shields.io/badge/Feito%20no-Brasil%20🇧🇷-009c3b?style=flat-square)

</div>
