# Análise de segurança

## Riscos representados

Um ransomware real pode combinar criptografia, interrupção da disponibilidade, persistência, movimentação lateral e extorsão. Este laboratório reproduz apenas a parte criptográfica e o fluxo local de arquivos sintéticos.

## Controles de contenção

O projeto contém controles deliberados:

- diretório alvo fixo em `lab_data/`;
- validação de caminho canônico;
- exclusão da chave do conjunto de arquivos elegíveis;
- nenhuma conexão de rede;
- nenhuma execução automática;
- nenhuma persistência;
- nenhuma elevação de privilégio;
- nenhum apagamento do arquivo original;
- nenhum acesso a diretórios do usuário.

## O que observar durante a execução

A análise pode ser feita com ferramentas como Process Monitor, strace ou auditoria de sistema em uma máquina de laboratório. O objetivo é observar abertura, leitura e escrita dos arquivos sintéticos e identificar os artefatos gerados.

## Lições defensivas

Indicadores úteis em detecção incluem alterações anômalas em grande volume de arquivos, extensões novas, picos de escrita, processos que acessam muitos documentos e falhas de autenticação ou integridade. Em um ambiente corporativo, controles de endpoint, princípio do menor privilégio, segmentação, backups offline e testes de restauração são camadas complementares.
