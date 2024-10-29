from abc import ABC, abstractmethod
import pandas as pd
import numpy as np

class DataInspectionStrategy(ABC):
    """
    A common interface for data inspection strategies.
    """
    @abstractmethod
    def inspect(self, data: pd.DataFrame) -> None:
        """
        Inspects the data.
        
        Parameters
        ----------
        data : `pd.DataFrame`
            The data to inspect.
            
        Returns
        -------
        `None`
        """
        pass
    
class DataTypeInspection(DataInspectionStrategy):
    """
    Concrete strategy for data type inspection.
    """
    def inspect(self, data: pd.DataFrame) -> None:
        """
        Inspects the data.

        Parameters
        ----------
        data : `pd.DataFrame`
            The data to inspect.

        Returns
        -------
        `None`
        """
        print("\nData Types and Non-NULL counts:")
        print(data.info())
        
        
class SummaryStatisticsInspection(DataInspectionStrategy):
    """
    Concrete strategy for summary statistics analysis.
    """
    def inspect(self, data: pd.DataFrame) -> None:
        """
        Prints the summary statistics for `numerical` and `categorical` columns
        in the given dataframe.
        
        Parameters
        ----------
        data : `pd.DataFrame`
            The dataframe to analyze for summary statistics.
            
        Returns
        -------
        `None`
        """
        print("\nSummary statistics for `numerical` features:")
        print(data.describe())
        print("\nSummary statistics for `categorical` features:")
        try:
            print(data.describe(exclude=np.number))
        except ValueError as e:
            if str(e) ==  "No objects to concatenate":
                print("`data` does not contain categorical features.")
        
        
class DataInspector:
    """
    Context class that uses a `DataInspectionStrategy`.
    This class allows you to switch between `DataInspectionStrategies`.
    """
    def __init__(self, strategy: DataInspectionStrategy):
        """
        Initializes the `DataInspector` with a strategy.
        
        Parameters
        ----------
        strategy : `DataInspectionStrategy`
            The strategy to use for data inspection.
            
        Returns
        -------
        `None`
        """
        self._strategy = strategy
        
        
    def set_strategy(self, strategy: DataInspectionStrategy) -> None:
        """
        Set a new strategy for the `DataInspector`.
        
        Parameters
        ----------
        strategy : `DataInspectionStrategy`
            The strategy to use for data inspection.
            
        Returns
        -------
        `None`
        """
        self._strategy = strategy
        
        
    def inspect(self, data: pd.DataFrame) -> None:
        """
        Execute the data inspection using the current inspection strategy.
        
        Parameters
        ----------
        data : `pd.DataFrame`
            The data to inspect against the current inspection strategy.
        """
        self._strategy.inspect(data)
        
        
# Example Usage
if __name__ == "__main__":
    df: pd.DataFrame = pd.read_csv("datasets\\heart_failure_clinical_records_dataset.csv")
    
    inspector: DataInspector = DataInspector(DataTypeInspection())
    inspector.inspect(df)
    
    # Switch between strategies
    inspector.set_strategy(SummaryStatisticsInspection())
    inspector.inspect(df) 
    