"""
Core module for descriptive statistics calculations.
"""
import numpy as np
from typing import Union, List, Tuple

class DescriptiveStats:
    @staticmethod
    def mean(data: Union[List[float], np.ndarray]) -> float:
        """Calculate the arithmetic mean of the data."""
        return np.mean(data)

    @staticmethod
    def median(data: Union[List[float], np.ndarray]) -> float:
        """Calculate the median of the data."""
        return np.median(data)

    @staticmethod
    def mode(data: Union[List[float], np.ndarray]) -> Union[float, List[float]]:
        """Calculate the mode(s) of the data."""
        return float(stats.mode(data, keepdims=False).mode)

    @staticmethod
    def variance(data: Union[List[float], np.ndarray], ddof: int = 1) -> float:
        """Calculate the variance of the data."""
        return np.var(data, ddof=ddof)

    @staticmethod
    def std_dev(data: Union[List[float], np.ndarray], ddof: int = 1) -> float:
        """Calculate the standard deviation of the data."""
        return np.std(data, ddof=ddof)
