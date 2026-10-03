# Texto para o campo "Entregar Projeto" — DIO Cybersecurity

## Descrição do Projeto

Projeto de Cybersecurity em Python desenvolvido para o desafio da DIO, com foco no estudo do fluxo de criptografia e recuperação de arquivos em uma **simulação controlada de ransomware**.

O projeto entrega os dois artefatos exigidos pelo desafio — `encrypter.py` e `decrypter.py` — implementados com **AES-256-GCM** (confidencialidade + autenticação), além de uma suíte de testes automatizados com `unittest`, documentação técnica detalhada e pipeline de CI/CD no GitHub Actions.

## Por que Simulador e não Ferramenta Real?

A implementação foi **deliberadamente limitada** a arquivos sintéticos dentro do diretório `lab_data/`. Não há persistência, rede, elevação de privilégio, propagação, execução automática ou exclusão de arquivos originais.

Essa decisão reflete a responsabilidade de publicar código em repositório público (Open Source): ferramentas de ataque funcionais publicadas abertamente tornam-se vetores de dano real independentemente da intenção original do autor, violam os Termos de Uso do GitHub e podem caracterizar crime nos termos da Lei nº 12.737/2012. O modelo de laboratório isolado atende **todos os objetivos educacionais** do desafio sem criar risco operacional.

## Estrutura Entregue

- `encrypter.py` — criptografador com sandbox de caminho e AES-256-GCM
- `decrypter.py` — descriptografador com validação de magic bytes
- `tests/test_simulacao.py` — 4 testes automatizados (round-trip, chave 256-bit, path escape, integridade)
- `docs/metodologia.md` — metodologia e decisões técnicas
- `docs/analise_de_seguranca.md` — análise de riscos e lições defensivas
- `.github/workflows/tests.yml` — CI automático no GitHub Actions
- `README.md` completo com arquitetura, controles de segurança e justificativa ética

## Link do Repositório

https://github.com/josewagnerbljr-sys/ransomware-lab-python
