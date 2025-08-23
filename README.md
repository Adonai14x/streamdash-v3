# Car Sales Dashboard

## What is this?
A simple **Streamlit web app** to explore car sales data. You can check car prices, compare brands, and see market trends with interactive charts.

## Features
- Histogram of car prices by year and brand
- Scatter plot: year vs. price
- Bar chart: average price by brand
- Option to view the raw dataset

## Tools Used
- **Streamlit** → makes the web app
- **Pandas** → handle data
- **Plotly Express** → create charts
- **NumPy** → math support

## Data
The app uses **vehicles_us.csv** with 51,525 car listings. Some columns:
- price, year, model, condition
- cylinders, fuel, odometer
- transmission, type, color, 4WD
- days listed

## How to Run (Beginner Friendly)

1. **Clone the repo**
   ```bash
   git clone <repo-url>
   cd streamdash-v3-1
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   ```
   - On Windows: `venv\Scripts\activate`
   - On Mac/Linux: `source venv/bin/activate`

3. **Install packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the app**
   ```bash
   streamlit run app.py
   ```

5. **Open in browser**
   - Usually opens automatically.
   - If not, go to: `http://localhost:8501`

## Files
```
streamdash-v3-1/
├── app.py              # Streamlit app
├── vehicles_us.csv     # Dataset
├── requirements.txt    # Needed packages
├── notebooks/EDA.ipynb # Data analysis
└── README.md           # This file
```

## Notes
This was built as a **course project**. Great for learning basics of Streamlit, data analysis, and visualization.

