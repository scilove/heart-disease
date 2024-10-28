import requests
import os
import pandas
import zipfile
from abc import ABC, abstractmethod
from requests import Response


class DataIngestor(ABC):
    """
    Abstract class to create a DataIngestor.
    """
    @abstractmethod
    def ingest_data(self, data_source: str) -> None:
        """
        Abstract method to ingest data from a data source.
        """
        pass
    
class CSVIngestor(DataIngestor):
    """
    A class to ingest `csv` data from a data source.
    
    Methods
    -------
    ingest_data(self, data_source_uri: str)
        Ingests data from a data source and saves it in the `datasets` directory.s
    """
    def ingest_data(self, data_source_uri: str) -> pandas.core.frame.DataFrame:
        """
        If not already saved in the `datasets` directory, this method ingests a `csv`
        file from a data sourse and saves it in the `datasets` directory.
        
        Parameters
        -----------
        data_source_uri : str
            The `uri` of the data source.
        
        Returns
        -------
        df : pandas.core.frame.DataFrame
            The DataFrame containing the ingested data.
        """
        filename: str = data_source_uri.split('/')[-1]
        foldername: str = "datasets"
        if not os.path.exists(foldername):
            os.makedirs(foldername)
            
        file_path: str = os.path.join(foldername, filename)
        
        if os.path.exists(file_path):
            print(f"\033[32mFile '{filename}' already exists in '{foldername}'. Download skipped.\033[0m]")
            return
        
         # Download the file
        try:
            response: Response = requests.get(data_source_uri)
            if response.status_code == 200:
                with open(file_path, "wb") as file:
                    file.write(response.content)
                    print(f"\033[34mFile '{filename}' downloaded successfully.\033[32m")
            else:
                print(f"\033[31mFailed to download file. Status code: {response.status_code}\033[0m")
        except Exception as e:
            print(f"An error occured in connecting to the specified uri: {e}")

class ZipFileIngestor(DataIngestor):
    """
    A class to ingest `zip` data from a data source.
    """
    def ingest_data(self, data_source_uri: str) -> pandas.core.frame.DataFrame:
        """
        If not already saved in the `datasets` directory, this extracts the contents of a `zip` file
        and saves it in the datasets directory.
        """
        filename: str = data_source_uri.split('/')[-1][:-3] + "csv"
        filename = filename.replace("+", "_")
        foldername: str = "datasets"
        if not os.path.exists(foldername):
            os.makedirs(foldername)
            
        file_path: str = os.path.join(foldername, filename)
        
        
        if os.path.exists(file_path):
            print(f"File '{filename}' already exists in '{foldername}'. Download skipped.")
            return 
        try:
            response: Response = requests.get(data_source_uri)
            if response.status_code == 200:
                with open ("temp_zip_file.zip", "wb") as temp_file:
                    temp_file.write(response.content)
                    print(f"\033[32mFile downloaded successfully.\033[0m]") 
                with zipfile.ZipFile("temp_zip_file.zip", "r") as zip_ref:
                    zip_ref.extractall("datasets")
                    
                os.remove("temp_zip_file.zip")
            else:
                print(f"Failed to download file. Status code: {response.status_code}")
        except Exception as e:
            print(f"\033[31mAn error occured in connecting to the specified uri: {e}\033[0m")
        
         # Download the file
        

class DataIngestorFactory:
    @staticmethod
    def get_ingestor(data_source_uri: str) -> DataIngestor:
        """
        Factory method to get an instance of the appropriate ingestor based on the data source.
        
        Parameters
        ----------
        data_source_uri : str
            The `uri` of the data source.
        
        Returns
        -------
        ingestor : DataIngestor
            The instance of the appropriate ingestor.
        """
        if data_source_uri.endswith(".csv"):
            return CSVIngestor()
        elif data_source_uri.endswith(".zip"):
            return ZipFileIngestor()
        else:
            raise ValueError(f"Unsupported data source: {data_source_uri}")
        
# if __name__ == "__main__":
#     uri: str = "https://archive.ics.uci.edu/static/public/519/heart+failure+clinical+records.zip"
#     data_ingestor = DataIngestorFactory.get_ingestor(uri)
#     data_ingestor.ingest_data(uri)
    