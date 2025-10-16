# Conteúdo para: scripts/download_anm.py
import requests
import zipfile
import io
import os
import pandas as pd
import geopandas as gpd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

BASE_OUTPUT_DIR = "data"
TABULAR_DIR = os.path.join(BASE_OUTPUT_DIR, "tabular")
GEO_DIR = os.path.join(BASE_OUTPUT_DIR, "geo")

MICRODADOS_URL = "https://app.anm.gov.br/dadosabertos/SCM/microdados/microdados-scm.zip"
SHAPEFILE_URL = "https://app.anm.gov.br/dadosabertos/SIGMINE/PROCESSOS_MINERARIOS/BRASIL.zip"

def download_and_extract_data(url, extract_dir, data_type ):
    """Função genérica para baixar e extrair dados."""
    os.makedirs(extract_dir, exist_ok=True)
    logging.info(f"Iniciando download dos dados de {data_type} de: {url}")
    
    try:
        response = requests.get(url, timeout=600)
        response.raise_for_status()
        
        logging.info("Download concluído. Descompactando arquivos...")
        with zipfile.ZipFile(io.BytesIO(response.content)) as z:
            z.extractall(extract_dir)
        logging.info(f"Arquivos de {data_type} extraídos em: '{extract_dir}'")
        return True
    except requests.exceptions.RequestException as e:
        logging.error(f"Falha no download dos dados de {data_type}: {e}")
        return False

if __name__ == "__main__":
    logging.info("--- INICIANDO COLETA DE DADOS PARA O GEOCLAVIS ---")
    
    download_and_extract_data(MICRODADOS_URL, TABULAR_DIR, "tabular")
    download_and_extract_data(SHAPEFILE_URL, GEO_DIR, "geoespacial")
    
    logging.info("--- PROCESSO DE COLETA CONCLUÍDO ---")
