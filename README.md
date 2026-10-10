# Laboratório de Análise Forense Digital

**Projeto de portfólio | Python | SHA-256 | Inventário de arquivos | Relatórios CSV**

Projeto educacional que demonstra um fluxo básico de inventário de arquivos e verificação de integridade por meio de hashes SHA-256. A ferramenta percorre uma pasta de amostras, coleta informações dos arquivos e exporta os resultados para um relatório CSV.

## Objetivos

- Inventariar arquivos de uma pasta, incluindo subpastas.
- Registrar o nome, o caminho relativo, a extensão e o tamanho dos arquivos.
- Registrar a data de modificação informada pelo sistema de arquivos.
- Calcular o hash SHA-256 de cada arquivo acessível.
- Exportar os resultados para um relatório CSV.
- Registrar erros de leitura encontrados durante o processamento.

## Requisitos

- Python 3.10 ou superior.
- Bibliotecas da biblioteca padrão do Python: `argparse`, `csv`, `hashlib`, `datetime` e `pathlib`.
- Testes automatizados com `unittest`.

Não são necessárias bibliotecas externas.

## Estrutura do projeto

```text
laboratorio-forense-digital/
├── amostras/
│   └── amostra_sintetica.txt
├── main.py
├── test_main.py
├── README.md
└── .gitignore
```

A pasta `relatorios/` é criada automaticamente quando o programa gera o arquivo CSV.

## Como executar

Abra o terminal na pasta do projeto e execute:

```bash
python main.py --source amostras --output relatorios/inventario.csv
```

No Windows, se o comando `python` não funcionar, tente:

```bash
py main.py --source amostras --output relatorios/inventario.csv
```

O programa exibirá a quantidade de arquivos encontrados, os processados com sucesso, os eventuais erros e o caminho do relatório gerado.

## Como executar os testes

Na pasta do projeto, execute:

```bash
python -m unittest -v test_main
```

No Windows, se necessário:

```bash
py -m unittest -v test_main
```

Os testes verificam o cálculo do SHA-256, a inclusão de arquivos em subpastas e a criação do relatório CSV.

## Limitações e cuidados forenses

- O SHA-256 permite comparar o conteúdo de arquivos em momentos diferentes. Isoladamente, não comprova autoria, origem, data de criação ou cadeia de custódia.
- A data de modificação é obtida dos metadados disponibilizados pelo sistema de arquivos e não deve ser considerada prova independente da data de um evento.
- A ferramenta não impede alterações nos arquivos de origem.
- Este projeto é educacional e não substitui ferramentas ou procedimentos forenses validados.
- Para atividades reais, trabalhe com autorização, preserve os arquivos originais e documente os procedimentos de coleta e análise.

## Próximas melhorias

1. Adicionar testes para arquivos vazios e erros de leitura.
2. Implementar exportação adicional para JSON.
3. Integrar a extração de metadados com o ExifTool.
4. Melhorar os registros de erros e a documentação dos resultados.

## Contexto profissional

Projeto demonstrativo de estudos em Python, integridade de arquivos e documentação técnica aplicada à Informática Forense e à Cibersegurança.
