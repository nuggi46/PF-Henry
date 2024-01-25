# <div align="center">**Data Analytics & ML**</div>

## Maching Learning

### Introducción

El contenido de esta carperta son todos aquellos necesarios para realizar el deploy del sistema de recomendación en Streamlit. La app de Streamlit utiliza el código google_final.py y este a la vez se encuentra conectado al data lake de google cloud. Por lo cual no se requiere incluir dentro de la carpeta la base de datos, ya se encuentra disponibilizado en la nube.

Para acceder a la plataforma, ingrese al siguiente [link](https://foodies.streamlit.app)

### SISTEMA DE RECOMENDACION

#### **Tipos de sistema de recomendación:**

**Basados en Contenido**: Estos sistemas analizan las características y atributos de los elementos recomendados y los comparan con las preferencias previas del usuario. Por ejemplo, en un sistema de recomendación de películas, si a un usuario le gustaron películas de ciencia ficción en el pasado, el sistema podría sugerirle más películas dentro de ese género.

**Filtrado Colaborativo**: Este enfoque se basa en el comportamiento y las elecciones de múltiples usuarios. Si dos usuarios tienen preferencias similares en el pasado, es probable que sus recomendaciones coincidan. El filtrado colaborativo puede ser «basado en usuarios» (recomendar en función de usuarios similares) o «basado en elementos» (recomendar elementos similares a los que el usuario ha interactuado antes).

Actualmente se encuentran disponibles dos sistemas de recomendacion y ambos son filtrado colaborativo, ya que surgen de las multitudes de experiencias de usuarios que se encuentran en google. 

#### Modelo 1

En el primer modelo, usuario puede elegir entre 1 a 4 inputs:

1. Categoria: el tipo de comida que le gustaria comer
2. Estado: si se encuentra en Pennsylvania o Florida
3. Ciudad: en que ciudad exactamente prefiere ir.
4. Tendencia: si prefiere elegir lugares que fueron comentados positivamente o no en promedio.

Este modelo se encuentra basado previamente en un análisis de sentimientos de los usuarios de google reviews y en base a ello se genera el modelo.

![modelo_1](https://github.com/mreliflores/PF-Henry/blob/main/Sprint%233/streamlit/modelo_1.png?raw=true)

#### Modelo 2

El segundo modelo parte de la selección del usuario de mayor preferencia y automáticamente recomienda los restaurantes basados en su experiencia personal y usuarios similares. El mismo se encuentra basado en el metodo de coseno similud.

![modelo_2](https://github.com/mreliflores/PF-Henry/blob/main/Sprint%233/streamlit/modelo_2.png?raw=true)

## Analytics