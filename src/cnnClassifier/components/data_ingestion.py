import os
from pathlib import Path
import urllib.request as request
import zipfile
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  

    def extract_zip_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
                )
            logger.info(f"{filename} downloaded with headers:\n{headers}")
            
            with open(filename, 'rb') as f:
                header = f.read(4)
                logger.info(f"First 4 bytes of downloaded file: {header}")
    
        unzip_dir = self.config.unzip_dir 
        os.makedirs(unzip_dir, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_dir)
            logger.info(f"Extracted {self.config.local_data_file} to {unzip_dir}")