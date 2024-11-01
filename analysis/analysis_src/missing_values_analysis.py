from abc import ABC, abstractmethod
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class MissingValuesAnalysisTemplate(ABC):
    """
    Abstract base class for missing values analysis.
    This class defines a template for missing values analysis.
    Subclasses must implement `identity_missing_values`, `analyze_missing_values
    and `visualize_missing_values` methods.
    """
    def analyze(self, data: pd.DataFrame) -> None:
        """
        Perform a complete missing values analysis by identifying and
        analyzing missing values.
        """
        self.identity_missing_values(data)
        self.analyze_missing_values(data)
        self.visualize_missing_values(data)
        
        
    @abstractmethod
    def identity_missing_values(self, data: pd.DataFrame) -> None:
        """
        Identify missing values in the dataframe.
        
        Parameters
        ----------
        data : `pd.DataFrame`
            The dataframe to be analyzed for missing values.
            
        Returns
        -------
        `None`
        """
        pass
    
    
    @abstractmethod
    def analyze_missing_values(self, data: pd.DataFrame) -> None:
        """
        Prints the percentage for missing values for each columns.
        
        Parameters
        ----------
        data : `pd.DataFrame`
            The dataframe to be analyzed for missing values.
            
        Returns
        -------
        `None`
        """
        pass
    
    
    def visualize_missing_values(self, data: pd.DataFrame) -> None:
        """
        Visualizes missing values in the dataframe.
        
        Parameters
        ----------
        data : `pd.DataFrame`
            The dataframe to visualize for missing values.
            
        Returns
        -------
        `None`
        """
        pass
    
    
class SimpleMissingValuesAnalysis(MissingValuesAnalysisTemplate):
    """
    Concrete class for missing values identification.
    This class implements methods to identify and visualize missing values in the dataframe.
    """
    def identity_missing_values(self, data: pd.DataFrame) -> None:
        """
        Prints the count of missing values for each column in the dataframe.
        
        Parameters
        ----------
        data : `pd.DataFrame`
            The dataframe to analyze for missing values.
            
        Returns
        -------
        `None`
        """
        print("\nMissing values count by columns:")
        missing_values = data.isnull().sum()
        print(missing_values[missing_values > 0])
        
        
    def analyze_missing_values(self, data: pd.DataFrame) -> None:
        """
        Prints the percentage of missing values in each column in the dataframe.
        
        Parameters
        ----------
        data : `pd.DataFrame`
            The dataframe from which to visualize missing values.
            
        Returns
        -------
        `None`
        """
        print("\nMissing values percentages by column")
        missing_values_pct = (100 * data.isnull().sum() / len(data)).round(2)
        print(missing_values_pct)
        
        
    def visualize_missing_values(self, data: pd.DataFrame) -> None:
        """
        Create a heatmap to visualize the missing values in the dataframe.
        
        Parameters
        ----------
        data : pd.DataFrame
            The dataframe from which the missing values are drawn.
            
        Returns
        -------
        `None`
        """
        print("Visualizing missing values . . .")
        plt.figure(figsize=(12, 8))
        sns.heatmap(data.isnull(), cmap="coolwarm")
        plt.title("Missing values Heatmap")
        plt.show()
        

# Example Usage
# if __name__ == "__main__":
#     df: pd.DataFrame = pd.read_csv("datasets/heart_failure_clinical_records_dataset.csv")
#     missing_values_analyzer: SimpleMissingValuesAnalysis = SimpleMissingValuesAnalysis()
#     missing_values_analyzer.analyze(df)   