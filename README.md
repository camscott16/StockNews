# Stock News Sentiment Analysis

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A Python-based application that fetches financial news articles from Financial Modeling Prep's API, analyzes the sentiment of each article using TextBlob, and visualizes the results for informed decision-making. This project streamlines data collection, analysis, and visualization for financial insights.

## Features

- **Financial News Aggregation**: Fetches the latest financial articles using Financial Modeling Prep's API.
- **Sentiment Analysis**: Classifies articles as positive, negative, factual, or opinion-based using TextBlob.
- **Data Visualization**: Generates graphical representations of sentiment distributions with Matplotlib.
- **Modular and Efficient Codebase**: Implements decorators for streamlined data processing and modularity.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/camscott16/StockNews.git
   cd src
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your API key:
   - Obtain an API key from [Financial Modeling Prep](https://financialmodelingprep.com/).
   - Add it to the script or set it as an environment variable:
     ```bash
     export API_KEY="your_api_key"
     ```

## Usage

Run the script to fetch financial news, analyze sentiment, and visualize the data:

```bash
python3 stockNews.py
```

### Example Output

- **Sentiment Analysis**: Aggregated data is saved in a pandas DataFrame for further processing.
- **Visualization**: Displays sentiment distribution graphs for actionable insights.

## Code Overview

- **Data Fetching**: Integrates Financial Modeling Prep's API to pull news data.
- **Text Analysis**: Uses BeautifulSoup to process raw HTML and TextBlob for sentiment classification.
- **Data Visualization**: Employs Matplotlib for plotting sentiment distributions.
- **Efficiency**: Decorators are used to modularize HTML extraction and sentiment analysis.

## Dependencies

- [Requests](https://docs.python-requests.org/en/master/) - For API interaction.
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) - For HTML parsing.
- [TextBlob](https://textblob.readthedocs.io/en/dev/) - For sentiment analysis.
- [pandas](https://pandas.pydata.org/) - For data aggregation.
- [Matplotlib](https://matplotlib.org/) - For data visualization.

Install all dependencies using:

```bash
pip install -r requirements.txt
```

## Contribution

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any questions or suggestions, feel free to reach out or open an issue on GitHub.
