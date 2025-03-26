# Statistical Analysis Toolkit

A comprehensive Python library for statistical analysis and data science.

## Features

- Descriptive Statistics
- Probability Distributions
- Correlation Analysis
- Regression Analysis
- Hypothesis Testing
- Data Visualization

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

```python
from stat_toolkit.core.descriptive import DescriptiveStats

data = [1, 2, 3, 4, 5]
mean = DescriptiveStats.mean(data)
std_dev = DescriptiveStats.std_dev(data)
```

## Development

1. Clone the repository
2. Create a virtual environment
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run tests:
   ```bash
   pytest tests/
   ```

## Project Structure

```
stat_toolkit/
├── docs/               # Documentation
├── examples/           # Example notebooks
├── stat_toolkit/       # Main package
│   ├── core/          # Core statistical functions
│   └── __init__.py
├── tests/             # Test suite
├── README.md
└── requirements.txt
```

## License

MIT License
