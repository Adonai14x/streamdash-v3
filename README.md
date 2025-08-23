# Car Sales Dashboard - Streamlit Web Application

## Project Description

This is a **Car Sales Dashboard** built with Streamlit that provides an interactive web interface for exploring and analyzing car sales data. The application allows users to visualize car pricing trends, brand distributions, and market insights through interactive charts and filters.

The dashboard is designed to help users understand:
- Price distributions across different car brands and years
- Market trends and patterns in the automotive industry
- Interactive data exploration with filtering capabilities

## Methods and Libraries Used

### Core Technologies:
- **Streamlit** - Web application framework for data science
- **Pandas** - Data manipulation and analysis
- **Plotly Express** - Interactive data visualization
- **NumPy** - Numerical computing support

### Key Features:
- Interactive histograms showing price distributions
- Scatter plots for year vs. price analysis
- Bar charts for brand comparisons
- Real-time data filtering with checkboxes
- Responsive web interface

## Dataset

The application uses the `vehicles_us.csv` dataset containing:
- **51,525 car listings** with 13 features
- Features include: price, model_year, model, condition, cylinders, fuel, odometer, transmission, type, paint_color, is_4wd, date_posted, days_listed

## Local Setup Instructions

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd streamdash-v3-1
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

5. **Access the dashboard:**
   - Open your web browser
   - Navigate to: `http://localhost:8501`
   - The dashboard will load automatically

## Features

### Interactive Visualizations:
- **Price Distribution Histogram** - Shows car prices by year and brand
- **Brand Price Analysis** - Bar chart comparing prices across brands
- **Year vs Price Scatter Plot** - Relationship between car age and pricing
- **Raw Data Viewer** - Toggle to display the complete dataset

### User Controls:
- Interactive charts with hover information
- Checkbox to show/hide raw data table
- Responsive layout that adapts to screen size

## Deployment

This application is deployed on **Render** and is accessible at:
[Your Render URL will go here once deployed]

### Deployment Configuration:
- **Build Command:** `pip install streamlit && pip install -r requirements.txt`
- **Start Command:** `streamlit run app.py`
- **Port:** 10000 (configured in `.streamlit/config.toml`)

## Project Structure

```
streamdash-v3-1/
├── app.py                 # Main Streamlit application
├── vehicles_us.csv        # Car sales dataset
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── .streamlit/
│   └── config.toml       # Streamlit configuration
└── notebooks/
    └── EDA.ipynb         # Exploratory data analysis
```

## Contributing

This project was created as part of a data science course assignment. Feel free to explore the code and suggest improvements!

## License

This project is for educational purposes.