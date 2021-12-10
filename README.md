# Using Deep Learning to Find Stock Price Patterns in ETFs

## File Structure
- [Project Paper](https://github.com/chpr1410/MSDS696-Practicum/blob/main/Project%20Paper.pdf)
- [Project Slide Deck](https://github.com/chpr1410/MSDS696-Practicum/blob/main/Project%20Deck.pptx)
- [Interactive Dash App](http://chpr1410.pythonanywhere.com/)
- [Video Presentation](https://www.youtube.com/watch?v=vN2vqtyfdkA)
- [Code Pt. 1: Working With the Data](https://github.com/chpr1410/MSDS696-Practicum/blob/main/1.%20Data%20Download%2C%20Cleaning%2C%20Feature%20Engineering%2C%20Processing.ipynb)
- [Code Pt. 2: Building the Models](https://github.com/chpr1410/MSDS696-Practicum/blob/main/2.%20Data%20Generator%20and%20Model%20Training.ipynb)
- [Code Pt. 3: EDA and Visualization](https://github.com/chpr1410/MSDS696-Practicum/blob/main/3.%20Exploratory%20Data%20Analysis%20and%20Visualizing%20Some%20Results.ipynb)

## Project Overview

In this project, I use deep learning methods to find stock price patterns in the stocks of Exchange Traded Funds (ETFs).  I focus particularly on finding intra-day patterns, dividing each trading week into 30-minute windows.

I focus on a selection of 54 ETFs and acquire the minute-by-minute trading data for the most recent two years.  I trained a Recurrent Neural Network (RNN) on each dataset.  

This deep learning problem is structured as a binary classification one, where the model input is the most recent 3 days worth of trading data and the output is a prediction of whether the stock price will be higher or not at the end of the subsequent 30-minute period. 

Each trading day begins at 9:30 AM and ends at 4:00 PM.  Within this day, there are 13 30-minute windows.  I evaluate each model's results overall, but also on the more granular basis of each 30-minute window.

*As a disclaimer, this project is for academic purposes only and should not be taken as financial advice.*

## Data Acquisition and Processing

Stock price data was acquired from [Alpha Vantage](https://www.alphavantage.co/) via API calls.  The data for each minute for each stock included open, close, high, and low prices, as well as trading volume.  In total 493 trading days, or 192,270 minutes were included the dataset for each ETF.  Pricing data was transformed to make it stationary. Also, features were scaled for consistency.

## Feature Engineering

Each dataset contained 57 features.  The raw pricing data for the stock was included as well as the following technical indicators, which are common in quantitative trading:

- [Bollinger Bands](https://www.investopedia.com/terms/b/bollingerbands.asp)
- [Relative Strength Index (RSI)](https://www.investopedia.com/terms/r/rsi.asp)
- [Moving Average Convergence Divergence (MACD)](https://www.investopedia.com/terms/m/macd.asp) 

Additional features were added to represent economic indicators.  Stock market performance depends in large part to different factors of economic performance – such as economic growth, inflation, unemployment, business confidence, and housing.  From the 54 selected ETFs, I chose ones to serve as proxies for these economic indicators.   
- Economic Growth: SPY - SPDR S&P 500 ETF
- Inflation: TLT - iShares 20+ Year Treasury Bond ETF
- Unemployment: VXX - iPath Series B S&P 500 VIX Short-Term Futures ETN
- Business Confidence: XLY - Consumer Discretionary Select Sector SPDR Fund
- Housing: VNQ - Vanguard Real Estate Index Fund

Below are the graphs of clsing prices for the proxies over the last two years: 

![Test Image 4](https://github.com/chpr1410/MSDS696-Practicum/blob/main/App/Static/Images/proxy_pricing.jpg)

While not perfect representations of economic indicators, these proxies track similar enough indicators and their pricing data was accessible in a consistent manner to the rest of the selection. 

I added features for the proxies' pricing data as well as their technical indicators.  I used the same technical indicators as above. 

Finally, I added features to the dataset for time.  These included features for  hour, minute, and day of the week.  

## Recurrent Neural Network (RNN)

The deep learning models were constructed using Keras/Tensorflow and the architecture consisted of two stacked LSTM layers.  Both dropout and recurrent dropout parameters were included.  

70% of the data was used in training, 20% in validation, and 10% was withheld for testing. Early stopping and patience parameters were determined the number of training epochs. 

## Result Evaluation and Visualization 

Model results on the test set were evaluated and logged after training.  I evaluated the models overall (on all window), and also more granularly on a window-by-window basis.

Overall, 18 of the 54 models achieved ROC scores greater than 50%.

![Test Image 4](https://github.com/chpr1410/MSDS696-Practicum/blob/main/App/Static/Images/roc_scores_by_ticker.jpg)

Investing in these ETFs for all periods according to model predictions would provide a slightly positive return, and one that improves on a passive strategy.

![Test Image 4](https://github.com/chpr1410/MSDS696-Practicum/blob/main/App/Static/Images/good_roc_stocks_dropdown.jpg)

![Test Image 4](https://github.com/chpr1410/MSDS696-Practicum/blob/main/App/Static/Images/good_roc_stocks_returns.jpg)

However, it is more insightful to view the models performances on a window-by-window basis.  Here are the models percentage returns by window, averaged:

![Test Image 4](https://github.com/chpr1410/MSDS696-Practicum/blob/main/App/Static/Images/all_stocks_return_by_window.jpg)

When averaged all together, the models have mixed performances, both positive and negative returns on investment.  Here are the ROC Scores and percentage returns by individual ticker:

![Test Image 4](https://github.com/chpr1410/MSDS696-Practicum/blob/main/App/Static/Images/roc_scores_by_ticker_by_Window.jpg)

![Test Image 4](https://github.com/chpr1410/MSDS696-Practicum/blob/main/App/Static/Images/model_return_by_window_by_ticker.jpg)

Clearly, the models for some stocks are better at predicting price change than others.  Prediction quality depends both on the stock and on the trading window.

I created a Plotly Dash application to help choose models by their performance on certain windows.  The application can be interacted with [here](http://chpr1410.pythonanywhere.com/).  Scroll to the section 'DataTable For Portfolio Selection' to choose a portfolio and view the results below.  Can you find a profitable strategy?

As an example, I chose a strategy where I hypothetically invested in all ETF-Window pairs where the model achieved an ROC Score greater than 80%.  

Here, you can see that the model achieves positive returns for most of the periods. 

![Test Image 4](https://github.com/chpr1410/MSDS696-Practicum/blob/main/App/Static/Images/80_percent_portfolio_returns.jpg)

Contrast the model's performance with the passive one (investing in the ETFs for  the window indiscriminately, not just when the  model suggests it).

![Test Image 4](https://github.com/chpr1410/MSDS696-Practicum/blob/main/App/Static/Images/80_percent_portfolio_passive.jpg)

There are more negative returns in the passive strategy and lower positive returns.  The model seems to be working in this example.  It achieves 4.63% average returns per week, compared to the -0.06% of the passive strategy.

![Test Image 4](https://github.com/chpr1410/MSDS696-Practicum/blob/main/App/Static/Images/80_percent_portfolio_summary.jpg)

## Conclusion

Overall, my deep learning models achieved satisfactory accuracy scores on one third of the ETF datasets.  Furthermore, when evaluated on individual trading windows throughout the week, the models were indeed able to find some patterns in the datasets with higher accuracy.  Following the models’ predictions – on the 10-week testing sample at least – would have provided positive returns well above a passive strategy.  

It seems that deep learning can use ETF stock pricing data to find patterns in different trading windows throughout the day.  But, past performance is not a guarantee of future returns.  

Things can and will change quickly in today’s fast paced stock market.  It is impossible to know for how long discovered patterns will stay the same.  The risk of patterns changing before the next investing decision will always require traders to tread carefully.
