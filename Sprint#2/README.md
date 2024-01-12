# <div align="center">**Data Engineering**</div>


## ETL Completo

Se realizó la extracción de datos desde su origen, transformación y limpieza para su uso en las áreas de analytics y ML. El proceso de ETL se detalla en dos archivos [ETL_Yelp]() (ETL de los datos proporcionados por la plataforma Yelp) y [ETL_Maps]() (datos proporcionados por Google Maps)


## Data Lake

En la plataforma GCP se utilizó Cloud Storage en donde se establecieron 2 buckets:

- `yelp-and-maps-data-lake`  Se encuentran los datos crudos y proporcionados por el cliente.

- `yelp-and-maps-data-processed` Se encuentra toda la data limpia después del ETL completo

![datalake](https://github.com/mreliflores/PF-Henry/blob/main/assets/Datalake.png?raw=true)


## Data Warehouse

Para el data warehouse se utilizó BigQuery, el cual recibe los archivos del bucket `yelp-and-maps-data-processed` en dos esquemas: **Google_tables** y **Yelp_tables** a través de los cuales, se puede extraer la información con SQL.

![datawarehouse](https://github.com/mreliflores/PF-Henry/blob/main/assets/datawarehouse.png?raw=true)


## Modelo ER

![erinicial](https://github.com/mreliflores/PF-Henry/blob/main/assets/DiagramaER.png?raw=true)


## Diccionario de Datos


### `review_estado`

| Fila | Descripción |
| --- | --- |
| **user_id** | Id de usuario de Google Maps. |
| **name** | Nombre de usuario de Google Maps. |
| **time** | Fecha y hora de registro de la calificación y/o comentario. |
| **gmap_id** | Id de localización del establecimiento, presente en tabla metadatos-sitio. |
| **rating** | Calificación hecha por el usuario. |
| **text** | Comentario hecho por el usuario. |
| **review** | Comentario tokenizado, para análisis de Machine Learning. |

### `metadatos_restaurantes`

| Fila | Descripción |
| --- | --- |
| **address** | Ubicación del negocio. |
| **avg_rating** | Promedio de todas las puntuaciones hechas por los usuarios. |
| **category** | Categorías con las que está registrado el restaurante. |
| **gmap_id** | Id de localización del establecimiento proporcionado por google maps. |
| **latitude** | Latitud de la coordenada. |
| **longitude** | Longitud de la coordenada. |
| **name** | Nombre del restaurante. |
| **num_of_reviews** | Cantidad de reseñas hechas por los usuarios. |
| **Accessibility** | Características de los tipos de acceso al establecimiento. |
| **Amenities** | Servicios que ofrece el establecimiento. |
| **Atmosphere** | Tipo de entorno que ofrece el restaurante. |
| **Crowd** | Tipos de multitudes admitidas |
| **Dining_options** | Opciones gastronómicas |
| **Highlights** | Servicios destacados |
| **Offerings** | Ofertas |
| **Payments** | Opciones de pago |
| **Planning** | Opciones de planificación |
| **Popular_for** | Público objetivo del restaurante |
| **Service_options** | Opciones de servicios |


## Workflow

![workflow](https://github.com/mreliflores/PF-Henry/blob/main/assets/Workflow.png?raw=true)


## MVP Machine Learning

![MVP-ML](https://github.com/mreliflores/PF-Henry/blob/main/assets/MVP.png?raw=true)

## MVP Data Analytics

![MVP-DA](https://github.com/JuanPa2608/PF-Henry/blob/main/assets/portada_DataAnalytics.jpg?raw=true)

