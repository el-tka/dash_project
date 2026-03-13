# Weather Analytics Dashboard

An interactive analytics dashboard for exploring **Moscow weather data over the last 10 years**.

The project is built using **Python, Dash and Plotly** and provides an intuitive interface for analyzing climate indicators such as temperature, precipitation, wind speed and solar radiation.

The dashboard enables interactive exploration of weather patterns and relationships between different meteorological variables.

---

# Features

The dashboard includes several interactive visualizations:

- Temperature trend analysis
- Correlation between temperature and solar radiation
- Wind speed distribution (wind rose)
- Monthly precipitation analysis
- Interactive year filtering

All visualizations update dynamically using **Dash callbacks**.

---

# Tech Stack

Python  
Dash  
Plotly  
Pandas  
SQL Server  
PyODBC  
Docker  

---

# Project Architecture

The project follows a modular architecture to improve maintainability and scalability.
ry for weather data analysis and visualisation.
```
dash_project
│
├── app
│ ├── app.py # Dash application entry point
│ │
│ ├── layout
│ │ └── layout.py # dashboard layout
│ │
│ └── assets
│ └── style.css # dashboard styling
│
├── data
│ └── database.py # database interaction layer
│
├── config
│ └── config.py # application configuration
│
├── utils
│ └── logger.py # logging system
│
├── notebooks # exploratory analysis notebooks
│
├── .env # environment variables (not committed)
├── .env.example # example configuration
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# Data Source

The dashboard retrieves data from a **Microsoft SQL Server database**.

Main table used:


```moscow_weather_data_last_10_years```


Key fields include:

- Date
- Max_Temperature_C
- Min_Temperature_C
- Precipitation_mm
- Wind_Speed_m_s
- Solar_Radiation_Index

---

# Visualizations

## 1. Daily Temperature Trends

A line chart displaying daily maximum and minimum temperatures for the selected year.

This visualization helps identify:

- seasonal patterns

- short-term fluctuations

- extreme temperature periods

## 2. Average Maximum Temperature by Year

A yearly trend line showing the average maximum temperature across the dataset.

This chart is useful for:

- comparing years

- identifying long-term climate tendencies

- spotting warmer and cooler periods over time

## 3. Correlation Analysis: Temperature and Solar Radiation

A scatter plot showing the relationship between maximum temperature and solar radiation index.

This visualization supports:

- correlation analysis between meteorological variables

- pattern detection across the selected year

- exploratory analysis of possible climate dependencies

## 4. Wind Rose

A polar bar chart representing the distribution of wind speed across predefined categories.

This chart helps analyze:

- wind intensity distribution

- frequency of different wind speed ranges

## 5. Monthly Precipitation Analysis

A bar chart showing total monthly precipitation for the selected year.
This allows users to compare precipitation intensity across different months and seasons.
---

# Installation

### 1 Clone the repository

```
git clone https://github.com/your_username/weather-analytics-dashboard.git

cd weather-analytics-dashboard
```

---

### 2 Create a virtual environment

```
python -m venv venv
```

Activate the environment.

Windows:

```
venv\Scripts\activate
```

Mac / Linux:

```
source venv/bin/activate
```

---

### 3 Install dependencies

```
pip install -r requirements.txt
```

---

# Database Configuration

Create a `.env` file in the root directory.

Example configuration:

```
DB_SERVER=localhost
DB_DATABASE=WeatherDB
DB_USER=sa
DB_PASSWORD=your_password
DB_DRIVER=ODBC Driver 17 for SQL Server
```

The `.env` file is excluded from version control for security reasons.

---

# Running the Application

Run the dashboard from the project root:

```
python app/app.py
```

The application will start at:


http://127.0.0.1:8050


---

# Running with Docker

Build the container:

```
docker build -t weather-dashboard .
```

Run the container:

```
docker run -p 8050:8050 weather-dashboard
```

---

# Logging

The project includes a centralized logging system.

Logging helps track:

- database connections
- data loading
- runtime errors

---
