from abc import ABC, abstractmethod
import pandas

class DataInspectionStrategy(ABC):
    """
    A common interface for data inspection strategies.
    """
    def inspect(self, data: pandas.core.frame.DataFrame) -> None:
        """
        Inspects the data.
        
        Parameters
        ----------
        data : `pandas.core.frame.DataFrame`
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
def inspect(self, data: pandas.core.frame.DataFrame) -> None:
    """
    Inspects the data.
    
    Parameters
    ----------
    data : `pandas.core.frame.DataFrame`
        The data to inspect.
    
    Returns
    -------
    `None`
    """
    print("-"*80)
    print("Data Types and Non-NULL counts")
    print("="*80)
    print(data.info()) 
    print("-"*80)