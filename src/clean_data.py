from abc import ABC, abstractmethod
import pandas as pd
import numpy as np

class DataCleaningTemplate(ABC):
    """
    Abstract class to create a data cleaning template.
    """
    def clean_data(self, data: pd.DataFrame, head: bool = False) -> pd.DataFrame:
        """
        Perforn a dataframe cleanup, by settinng all values to the right format.
        """
        cleaned_data: pd.DataFrame = self.prepare_data(data)
        if head:
            print(cleaned_data.head())
        return cleaned_data
    
    
    @abstractmethod
    def prepare_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Abstract method to clean the data.
        
        Parameters
        ----------
        data : `pd.DataFrame`
            The data to be cleaned.
            
        Returns
        -------
        df : `pd.DataFrame`
            A cleaned dataFrame.
        """
        pass
    

class SimpleDataCleaner(DataCleaningTemplate):
    """
    A simple data cleaning class that extends the `DataCleaningTemplate`.
    
    Methods
    -------
    `def clean_data(self, data: pd.DataFrame) -> pd.DataFrame`
        Method to call on the raw data to clean it. It returns the cleaned data.
    """
    def prepare_data(self, data: pd.DataFrame) -> None:
        """
        Cleans the data by setting each feature into its appropriate format for analysis.
        
        Parameters
        ----------
        data : `pd.DataFrame`
            Tha dataframe to clean for analysis.
            
        Returns
        -------
        df : `pd.DataFrame`
            A cleaned dataframe.
        """
        data["anaemia"] = np.where(data["anaemia"] == 0, "No", "Yes")
        data["diabetes"] = np.where(data["diabetes"] == 0, "No", "Yes")
        data["high_blood_pressure"] = np.where(data["high_blood_pressure"] == 0, "No", "Yes")
        data["sex"] = np.where(data["sex"] == 0, "Woman", "Man")
        data["smoking"] = np.where(data["smoking"] == 0, "No", "Yes")
        
        data.rename(columns={"DEATH_EVENT": "death_event"}, inplace=True)
        return data
        

# Example Usage
# if __name__ == "__main__":
#     df: pd.DataFrame = pd.read_csv("datasets/heart_failure_clinical_records_dataset.csv")
#     cleaner: SimpleDataCleaner = SimpleDataCleaner()
#     cleaned_df: pd.DataFrame = cleaner.clean_data(df)
#     print(cleaned_df.head())
        
        
        