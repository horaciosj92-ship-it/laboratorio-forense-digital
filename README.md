# Laboratório de Análise Forense Digital

**Projeto educacional de portfólio | Python | SHA-256 | Inventário de arquivos | CSV**

Este projeto demonstra um fluxo inicial e reproduzível para inventariar arquivos de uma pasta de amostras e registrar hashes SHA-256. Foi desenvolvido para fins educacionais, usando arquivos de teste autorizados.

## Objetivos

- Enumerar arquivos dentro de uma pasta de amostras.
- Registrar nome, caminho relativo, extensão, tamanho e datas disponíveis.
- Calcular SHA-256 para apoiar verificações futuras de integridade.
- Exportar um relatório CSV.
- Documentar limitações e preservar os arquivos originais.

## Requisitos

- Python 3.10 ou superior
- Nenhuma biblioteca externa necessária

## Como executar

Na pasta do projeto, execute:

```bash
python main.py --source amostras --output relatorios/inventario.csv
```

No Windows, se `python` não funcionar, tente:

```powershell
py main.py --source amostras --output relatorios/inventario.csv
```

O programa cria o relatório CSV no caminho informado. Coloque somente arquivos de teste próprios ou autorizados dentro de `amostras/`.

## Estrutura

```text
laboratorio-forense-digital/
├── amostras/             # Arquivos de teste autorizados
├── relatorios/           # Relatórios gerados
├── tests/
│   └── test_main.py      # Testes automatizados
├── main.py               # Ferramenta de inventário e hash
├── README.md
└── .gitignore
```

## Limitações e cautelas

- O hash SHA-256 ajuda a comparar o conteúdo de um arquivo em momentos diferentes; sozinho, não prova autenticidade, autoria ou cadeia de custódia.
- As datas dependem do sistema de arquivos e podem mudar quando arquivos são copiados. Não são, isoladamente, prova de quando um evento ocorreu.
- Esta versão não bloqueia alterações nos arquivos de origem. Para uma investigação real, trabalhe em cópias verificadas e siga procedimentos institucionais de preservação e cadeia de custódia.
- Não use arquivos pessoais, corporativos ou de terceiros sem autorização.

## Próximas melhorias

1. Extrair metadados com ExifTool em uma etapa separada.
2. Adicionar logs e tratamento de erros mais detalhado.
3. Criar testes para arquivos vazios, subpastas e erros de leitura.
4. Gerar também um relatório JSON.

## Contexto profissional

Projeto demonstrativo para estudo de Python, integridade de arquivos e documentação técnica aplicada à Informática Forense e Cibersegurança.
