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
| **address** | Ubicación del negocio |
| **avg_rating** |  |
| **category** |  |
| **gmap_id** |  |
| **latitude** |  |
| **longitude** |  |
| **name** |  |
| **num_of_reviews** |  |
| **Accessibility** |  |
| **Amenities** |  |
| **Atmosphere** |  |
| **Crowd** |  |
| **Dining_options** |  |
| **From_the_business** |  |
| **Highlights** |  |
| **Offerings** |  |
| **Payments** |  |
| **Planning** |  |
| **Popular_for** |  |
| **Service_options** |  |

## Workflow

![workflow](https://github.com/mreliflores/PF-Henry/blob/main/assets/Workflow.png?raw=true)


## MVP Machine Learning

![MVP](https://github.com/mreliflores/PF-Henry/blob/main/assets/MVP.png?raw=true)

## MVP Data Analytics