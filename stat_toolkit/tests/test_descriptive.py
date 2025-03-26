"""
Tests for descriptive statistics module.
"""
import pytest
import numpy as np
from stat_toolkit.core.descriptive import DescriptiveStats

def test_mean():
    data = [1, 2, 3, 4, 5]
    assert DescriptiveStats.mean(data) == 3.0

def test_median():
    data = [1, 2, 3, 4, 5]
    assert DescriptiveStats.median(data) == 3.0

def test_std_dev():
    data = [1, 2, 3, 4, 5]
    assert abs(DescriptiveStats.std_dev(data) - 1.5811388300841898) < 1e-10
