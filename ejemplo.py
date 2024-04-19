import streamlit as st
import pandas as pd
import plotly.express as px

# Generar datos de muestra
datos = pd.DataFrame({
    'Producto': ['Producto A', 'Producto B', 'Producto C', 'Producto D', 'Producto E'],
    'Categoría': ['Categoría 1', 'Categoría 2', 'Categoría 1', 'Categoría 3', 'Categoría 2'],
    'Ventas': [5000, 3500, 4200, 2800, 4500],
    'Costo': [2500, 1800, 2100, 1400, 2700],
    'Región': ['Región A', 'Región B', 'Región A', 'Región C', 'Región B']
})

# Configurar página
st.set_page_config(page_title="Inteligencia de Negocios", layout="wide")
st.title("Análisis de Ventas - Inteligencia de Negocios")

# Mostrar datos
st.header("Datos de Ventas")
st.write(datos)

# Ventas totales por región
st.header("Ventas Totales por Región")
region_ventas = datos.groupby("Región")["Ventas"].sum().sort_values(ascending=False)
fig = px.bar(x=region_ventas.index, y=region_ventas.values, labels={"x": "Región", "y": "Ventas Totales"})
st.plotly_chart(fig)

# Ventas por categoría de producto
st.header("Ventas por Categoría de Producto")
categoria_ventas = datos.groupby("Categoría")["Ventas"].sum().sort_values(ascending=False)
fig = px.pie(values=categoria_ventas.values, names=categoria_ventas.index, title="Distribución de Ventas por Categoría de Producto")
st.plotly_chart(fig)

# KPIs (Indicadores Clave de Rendimiento)
st.header("Indicadores Clave de Rendimiento")
col1, col2, col3 = st.columns(3)
col1.metric("Ventas Totales", f"${datos['Ventas'].sum():,.2f}")
col2.metric("Costo Total", f"${datos['Costo'].sum():,.2f}")
col3.metric("Ganancia Neta", f"${(datos['Ventas'].sum() - datos['Costo'].sum()):,.2f}")