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

## Temperature Trends

A line chart displaying daily maximum and minimum temperatures.

This allows analysis of:

- seasonal patterns
- extreme temperatures
- long-term trends

---

## Temperature vs Solar Radiation

A scatter plot visualizing the relationship between:

- solar radiation
- maximum temperature
- wind speed
- precipitation levels

---

## Wind Rose

A polar chart showing wind speed distribution across defined categories.

---

## Monthly Precipitation

A bar chart showing the total precipitation by month for the selected year.

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
