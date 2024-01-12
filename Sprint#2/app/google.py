
import os
import pandas as pd
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity
import base64

df_restaurante = pd.read_excel("info_restaurante.xlsx")
df_foodie = pd.read_excel("info_influencer.xlsx")


# Sidebar con opciones
st.sidebar.image("innovaLogo.jpeg", width=300)
sidebar_option = st.sidebar.radio("Selecciona una opción", ["Inicio", "Decido yo", "Decide el mejor"])



#Fondo del sidebar
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #FFFFFF;
    }
</style>
""", unsafe_allow_html=True)


# Divide la columna de género en columnas separadas (usando get_dummies para la codificación one-hot)
df_genre = df_restaurante['Categoria'].str.get_dummies(sep=',')
# Combina el DataFrame original con el DataFrame de género
df_restaurante = pd.concat([df_restaurante, df_genre], axis=1)
features = df_genre.columns
similarity_matrix = cosine_similarity(df_restaurante[features], df_restaurante[features])


#se escribe aca el codigo de recomendacion y luego se visualiza mas adelante

def obtener_recomendaciones(categoria, similarity_matrix, df_restaurante, n=2):
    indice_referencia = df_restaurante[df_restaurante['Categoria'] == categoria].index[0]
    similitud_pelicula_referencia = similarity_matrix[indice_referencia]
    puntuaciones_similitud = list(enumerate(similitud_pelicula_referencia))
    puntuaciones_similitud = sorted(puntuaciones_similitud, key=lambda x: x[1], reverse=True)
    recomendaciones = puntuaciones_similitud[1:n+1]
    nombres_recomendados = [df_restaurante.iloc[i]['Restaurante'] for i, _ in recomendaciones]
    return nombres_recomendados


#sección recomendación atributo

def recommend_atributo():
    #options = st.multiselect('Selecciona a continuación que debemos   \
    #tener en cuenta para darte la mejor opción del dia de hoy'\
    #    , ['Tipo de comida', 'Ubicación','Tendencia' ,'Precio'])
    
    container = st.container()
    all = st.checkbox("Selecciona todos")
 
    if all:
        selected_options = container.multiselect("Selecciona a continuación que debemos   \
    tener en cuenta para darte la mejor opción del dia de hoy:",
             ['Categoria','Rating','Ubicacion','Precio'],['Categoria','Rating','Ubicacion','Precio'])
        
        col1, col2, col3, col4 = st.columns(4)
        
        categoria = col1.selectbox("Tipo de comida", df_restaurante['Categoria'].unique())
        rating = col2.selectbox("Tendencia", df_restaurante['Rating'].unique())
        ubicacion = col3.selectbox("Barrio", df_restaurante['Ubicacion'].unique())
        precio = col4.selectbox("Nivel", df_restaurante['Precio'].unique())
    else:
        selected_options =  container.multiselect("Selecciona a continuación que debemos   \
    tener en cuenta para darte la mejor opción del dia de hoy:",
            ['Categoria', 'Rating','Ubicacion','Precio'])
        
        col1, col2, col3, col4 = st.columns(4)
        if 'Categoria' in selected_options:
            categoria = col1.selectbox("Tipo de comida", df_restaurante['Categoria'].unique())
        
        if 'Rating' in selected_options:
            rating = col2.selectbox("Tendencia", df_restaurante['Rating'].unique()) 
            
        if 'Ubicacion' in selected_options:
            ubicacion = col3.selectbox("Barrio", df_restaurante['Ubicacion'].unique())
        
        if 'Precio' in selected_options:
            precio = col4.selectbox("Nivel", df_restaurante['Precio'].unique())
        
            # Botón para generar recomendaciones
        if st.button("Generar Recomendaciones"):
            if categoria:
                # Corregir el cálculo de recomendaciones
                recomendaciones = obtener_recomendaciones(categoria, similarity_matrix, df_restaurante)
                # Crear una tabla para mostrar las recomendaciones
                table_data = []
                
                for recomendacion in recomendaciones:
                    info_adicional = df_restaurante[df_restaurante['Restaurante'] == recomendacion][['Rating', 'Precio',\
                    'Ubicacion']].values
                    
                    # Asegurarse de que info_adicional es un array unidimensional
                    if len(info_adicional) > 0:
                        info_adicional = info_adicional[0]

                    # Añadir datos a la tabla
                        table_data.append({
                            'Nombre': recomendacion,
                            'Tendencia': info_adicional[0],
                            'Precio': info_adicional[1],
                            'Ubicacion': info_adicional[2]
                        })
                                   
                if table_data:
                # Intentar crear el DataFrame
                    df_table = pd.DataFrame(table_data)

                # Mostrar la tabla
                    st.table(df_table[['Nombre', 'Tendencia', 'Precio', 'Ubicacion']])
                else:
                    st.write("No se encontraron recomendaciones.")
    
#sección recomendación influencer
def recommend_foodie():
# Crear un menú desplegable con la lista de películas para el sistema de recomendación
    influencer_referencia = st.selectbox('Seleccion un influencer de referencia', df_foodie['Infuencer'].unique())  
    
# Contenido principal
if sidebar_option == "Inicio":

    st.title("Bienvenido a InnovaAI Analytics!")

    #st.markdown("Explora restaurantes y descubre nuevas recomendaciones.")
    
    new_title = '<p style="font-family:Source Sans Pro; color:Black; font-size: 36px;">Explora y descubre nuevos lugares.</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("https://i.postimg.cc/xjMxCsnc/pexels-codioful-formerly-gradienta-7130497.jpg");
    background-size: cover;
    background-position: center center;
    background-repeat: no-repeat;
    background-attachment: local;
    }}
    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

    st.image("foto_1.jpg", width=650)
    
elif sidebar_option == "Decido yo":
    recommend_atributo()

elif sidebar_option == "Decide el mejor":
    recommend_foodie()   





# -- Create three columns
#_, col2, col3 = st.columns([5, 5, 25])
# -- Put the image in the middle column
# - Commented out here so that the file will run without having the image downloaded
#with col3:
#   st.image("innovaLogo.jpeg", width=300)


#with col3:
#    st.header("Bienvenidos")


#with col3:
#    st.subheader("Que te gustaría comer hoy?")
    
#options = st.multiselect('Selecciona a continuación que debemos   \
#    tener en cuenta para darte la mejor opción del dia de hoy'\
#        , ['Tipo de comida', 'Ubicación','Tendencia' ,'Precio'])


#displaying the selected options

#st.write('You have selected:', options)