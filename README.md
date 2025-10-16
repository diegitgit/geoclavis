# Clavis Geo - Plataforma de Dados de Mineração

**Clavis Geo** é uma plataforma para coleta, processamento e análise de dados públicos de mineração no Brasil. O objetivo é consolidar informações da Agência Nacional de Mineração (ANM) and do Serviço Geológico do Brasil (SGB/CPRM) em uma base de dados robusta e de fácil acesso.

## Visão Geral

Este repositório contém os scripts e a infraestrutura como código para construir a base de dados da plataforma Clavis Geo. A estratégia adotada é uma arquitetura híbrida que combina downloads diários de dados massivos com consultas em tempo real a APIs públicas.

### Fontes de Dados

-   **ANM - Agência Nacional de Mineração:**
    -   **Microdados do Cadastro Mineiro (SCM):** Dados tabulares completos (processos, eventos, titulares).
    -   **SIGMINE Shapefiles:** Dados geoespaciais (polígonos dos processos minerários).
    -   **API REST do SIGMINE:** Consultas dinâmicas e dados em tempo real.
-   **SGB/CPRM - Serviço Geológico do Brasil:**
    -   **GeoSGB:** Dados geológicos e de recursos minerais.
    -   **OGC API:** Acesso moderno a dados geoespaciais.

## Estrutura do Projeto

```
.
├── scripts/
│   └── download_anm.py   # Script para download e extração dos dados da ANM (Fase 1)
├── .gitignore            # Ignora arquivos desnecessários (ex: a pasta /data)
├── LICENSE               # Licença de uso do projeto (MIT)
├── README.md             # Esta documentação
└── requirements.txt      # Dependências Python do projeto
```

## Como Começar

### Pré-requisitos

-   Python 3.8+
-   Git

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/diegitgit/geoclavis.git
    cd geoclavis
    ```

2.  **Crie um ambiente virtual e instale as dependências:**
    ```bash
    # Crie o ambiente virtual
    python -m venv venv

    # Ative o ambiente (Windows )
    .\venv\Scripts\activate
    # Ative o ambiente (Linux/macOS)
    source venv/bin/activate

    # Instale as bibliotecas necessárias
    pip install -r requirements.txt
    ```
        # 1. Vá para a pasta do projeto
        cd Documents/geoclavis

        # 2. Ative o ambiente virtual
        source venv/bin/activate
        # 3. python3 scripts/coletor_geo_anm.py



### Executando a Coleta de Dados

Para executar a primeira fase (download dos dados da ANM), rode o script principal:

```bash
python scripts/download_anm.py
```

O script irá baixar e descompactar os dados nas pastas `data/tabular` e `data/geo`.

## Próximos Passos

-   [ ] **Fase 1.B:** Criar scripts para carregar os dados baixados em um banco de dados PostgreSQL/PostGIS.
-   [ ] **Fase 2:** Desenvolver módulos para consultas dinâmicas nas APIs da ANM.
-   [ ] **Fase 3:** Integrar dados geológicos do SGB/CPRM.
-   [ ] **Automação:** Configurar GitHub Actions para executar a coleta de dados diariamente.
-   [ ] **Containerização:** Criar um `Dockerfile` para facilitar o deploy da aplicação.
