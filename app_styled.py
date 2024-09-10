import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pyodbc
import pandas as pd
import plotly.graph_objs as go
from data import get_weather_data
from layout import create_layout

# Загрузка данных
query = "SELECT * FROM dbo.moscow_weather_data_last_10_years"
df = get_weather_data(query)

# Проверяем, загрузились ли данные
if df is not None:
    print("Данные на месте")
else:
    print("Нет данных")

# Изменим формат входных данных
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
for row in ['Max_Temperature_C', 'Min_Temperature_C', 'Precipitation_mm',
            'Wind_Speed_m_s', 'Solar_Radiation_Index']:
    df[row] = pd.to_numeric(df[row])
    df[row] = df[row].round(2)

# Создание Dash-приложения
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])

# Layout приложения
app.layout = create_layout(df)

# Коллбэк для обновления графика на основе выбранного года
@app.callback(
    Output('temperature-graph', 'figure'),
    [Input('year-dropdown', 'value')]
)
def update_graph(selected_year):
    filtered_data = df[df['Date'].dt.year == selected_year]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=filtered_data['Date'], y=filtered_data['Max_Temperature_C'],
                             mode='lines', name='Max Temperature'))
    fig.add_trace(go.Scatter(x=filtered_data['Date'], y=filtered_data['Min_Temperature_C'],
                             mode='lines', name='Min Temperature'))

    fig.update_layout(title=f'Температурные данные за {selected_year} год',
                      xaxis_title='Дата', yaxis_title='Температура (°C)', template="plotly_dark")
    return fig


@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('year-dropdown_1', 'value')]
)
def update_scatter_plot(selected_year):
    filtered_df = df[df['Date'].dt.year == selected_year]
    filtered_df['month'] = filtered_df['Date'].dt.month
    filtered_df = filtered_df.groupby(['month']).agg(
        mean_max_t=pd.NamedAgg(column="Max_Temperature_C", aggfunc="mean"),
        mean_solar_radiation=pd.NamedAgg(column="Solar_Radiation_Index", aggfunc="mean"),
        max_wind_speed=pd.NamedAgg(column="Wind_Speed_m_s", aggfunc="max"),
        sum_precipitation=pd.NamedAgg(column="Precipitation_mm", aggfunc="sum")).reset_index()

    fig = px.scatter(filtered_df, x='mean_solar_radiation', y='mean_max_t',
                     color='max_wind_speed', size='sum_precipitation',
                     title=f'Корреляция между солнечной радиацией и максимальной температурой для {selected_year} года',
                     labels={'mean_solar_radiation': 'Индекс солнечной радиации',
                             'mean_max_t': 'Макс. температура (°C)'},
                     hover_data=['month'])
    fig.update_layout(xaxis_title='Индекс солнечной радиации', yaxis_title='Усредненная максимальная температура (°C)', template="plotly_dark")
    return fig


# Функция для обновления диаграммы роза ветров
@app.callback(
    Output('wind-rose-plot', 'figure'),
    Input('wind-rose-plot', 'id')
)
def update_wind_rose(_):
    # Округление скорости ветра и группировка по категориям
    df['Wind_Speed_Category'] = pd.cut(df['Wind_Speed_m_s'], bins=[0, 5, 10, 15, 20, 25],
                                       labels=['0-5', '5-10', '10-15', '15-20', '20-25'])
    wind_data = df.groupby('Wind_Speed_Category').size().reset_index(name='Count')

    # Построение полярной диаграммы
    fig = px.bar_polar(wind_data, r='Count', theta='Wind_Speed_Category', template="plotly_dark",
                       title='Роза ветров по категориям скорости ветра')
    fig.update_layout(template="plotly_dark")
    return fig


# Функция для обновления графика температуры
@app.callback(
    Output('temperature-plot', 'figure'),
    Input('temperature-plot', 'id')
)
def update_temperature_plot(_):
    # Группировка данных по годам и месяцу
    temp_data = df.groupby(df['Date'].dt.year)['Max_Temperature_C'].mean().reset_index(name='Avg_Max_Temperature')

    # Построение графика средней температуры по годам
    fig = px.line(temp_data, x='Date', y='Avg_Max_Temperature', title='Средняя максимальная температура по годам')
    fig.update_layout(template="plotly_dark", xaxis_title='Дата', yaxis_title='Усредненная Макс. Температура (°C)',)
    return fig


# Функция для обновления графика корреляции максимальной температуры и солнечной радиации
@app.callback(
    Output('temp-radiation-scatter', 'figure'),
    Input('year-dropdown_corr', 'value')
)
def update_temp_radiation_scatter(selected_year):
    filtered_df = df[df['Year'] == selected_year]

    # Построение графика корреляции
    fig = px.scatter(filtered_df, x='Max_Temperature_C', y='Solar_Radiation_Index',
                     title=f'Корреляция между максимальной температурой и солнечной радиацией за {selected_year}',
                     labels={'Max_Temperature_C': 'Максимальная Температура',
                             'Solar_Radiation_Index': 'Индекс Солнечной Радиации'})
    fig.update_traces(marker=dict(size=10, opacity=0.6))
    fig.update_layout(template="plotly_dark")
    return fig


# Функция для обновления графика осадков по месяцам
@app.callback(
    Output('precipitation-bar', 'figure'),
    Input('year-dropdown-precipitation', 'value')
)
def update_precipitation_bar(selected_year):
    filtered_df = df[df['Year'] == selected_year]
    precipitation_data = filtered_df.groupby('Month')['Precipitation_mm'].sum().reset_index()

    # Построение графика осадков по месяцам
    fig = px.bar(precipitation_data, x='Month', y='Precipitation_mm',
                 title=f'Суммарные осадки по месяцам за {selected_year}',
                 labels={'Month': 'Месяц', 'Precipitation_mm': 'Суммарные Осадки (мм)'})
    fig.update_layout(template="plotly_dark")
    return fig


# Запуск приложения
if __name__ == '__main__':
    app.run_server(debug=True)
