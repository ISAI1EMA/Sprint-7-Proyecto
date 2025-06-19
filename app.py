import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración inicial de la página
st.set_page_config(page_title="Análisis de Vehículos", layout="wide")

# Título principal
st.title("🚗 Análisis Exploratorio de Vehículos - Dr. D")

# Carga de datos
@st.cache_data 
def load_data():
    return pd.read_csv("/data/vehicles_us.csv")

df = load_data()

# Sidebar con controles
st.sidebar.header("🔧 Controles de Visualización")
chart_type = st.sidebar.radio(
    "Elige el tipo de gráfico:",
    ("Histograma", "Gráfico de Dispersión")
)

# Encabezado de sección
st.header("📊 Visualización Interactiva")

# Gráficos dinámicos
if chart_type == "Histograma":
    st.write("### Distribución de Precios (Histograma)")
    column = st.selectbox("Selecciona la columna:", df.select_dtypes(include='number').columns)
    fig = px.histogram(df, x=column, nbins=50, title=f"Distribución de {column}")
    st.plotly_chart(fig, use_container_width=True)

elif chart_type == "Gráfico de Dispersión":
    st.write("### Relación entre Variables (Scatter Plot)")
    col_x = st.selectbox("Eje X:", df.select_dtypes(include='number').columns)
    col_y = st.selectbox("Eje Y:", df.select_dtypes(include='number').columns, index=1)
    fig = px.scatter(df, x=col_x, y=col_y, color="fuel", hover_name="model", 
                     title=f"{col_y} vs {col_x}")
    st.plotly_chart(fig, use_container_width=True)
