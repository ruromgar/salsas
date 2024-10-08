import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


data = {
    'Salsa': [
        'Holandesa', 'Bechamel', 'Tomate', 'Mayonesa', 'Barbacoa',
        'Yogur', 'Vinagreta', 'Boloñesa', 'Pimienta', 'Queso',
        'Pesto', 'Ketchup', 'Mojo', 'Romesco', 'Cabrales',
        'Alioli', 'Brava'
    ],
    'Clara': [6, 10, 5, 8, 6, 7, 6, 8, 2, 6, 7, 9, 6, 8, 9, 7, 2],
    'Rubén': [7, 10, 7, 9, 6, 6, 6, 9, 7, 9, 5, 6, 7, 8, 8, 9, 7]
}

df = pd.DataFrame(data)


st.title("Salsas")


st.write('## Notas por salsa')
df_line = df.set_index('Salsa')
st.line_chart(df_line)


st.write('## Spider Plot')
df_melted = df.melt(id_vars='Salsa', value_vars=['Clara', 'Rubén'], var_name='Person', value_name='Rating')
df_radar = df.copy()
df_radar['Salsa'] = df_radar['Salsa'].str.title()
fig = px.line_polar(df_melted, r='Rating', theta='Salsa', color='Person', line_close=True)
st.plotly_chart(fig)


st.write('## Notas por persona')
st.write('(Seleccionar ambos realiza una suma)')
person = st.selectbox('Selecciona una persona:', ['Ambos', 'Clara', 'Rubén'])
if person == 'Ambos':
    data_to_plot = df_line
else:
    data_to_plot = df_line[[person]]
st.bar_chart(data_to_plot)


st.write('## Ordenar por nota')
sort_person = st.selectbox('Ordenar según notas de:', ['Clara', 'Rubén'])
df_sorted = df.sort_values(by=sort_person, ascending=False)
df_melted_sorted = df_sorted.melt(id_vars='Salsa', value_vars=['Clara', 'Rubén'], var_name='Person', value_name='Rating')
fig_sorted, ax_sorted = plt.subplots(figsize=(10, 6))
sns.barplot(x='Salsa', y='Rating', hue='Person', data=df_melted_sorted, ax=ax_sorted)
plt.xticks(rotation=45)
st.pyplot(fig_sorted)


st.write('## Y, finalmente, nota media')
df['Average'] = df[['Clara', 'Rubén']].mean(axis=1)
df_avg_sorted = df.sort_values(by='Average', ascending=False)
fig_avg, ax_avg = plt.subplots(figsize=(10, 6))
sns.barplot(x='Salsa', y='Average', data=df_avg_sorted, palette='viridis', ax=ax_avg)
plt.xticks(rotation=45)
plt.xlabel('Salsa')
plt.ylabel('Nota media')
plt.title('Nota media por salsa')
st.pyplot(fig_avg)


st.write('## Anexo: Datos en crudo')
st.dataframe(df)