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

![datawarehouse]()


## Modelo ER

![erinicial](https://github.com/mreliflores/PF-Henry/blob/main/assets/DiagramaER.png?raw=true)

![erpersonalizado]()


## Diccionario de Datos

| Reviews | Descripción |
| --- | --- |
| `user_id` | Id de usuario de Google Maps. |
| `name` | Nombre de usuario de Google Maps. |
| `time_normalizado` | Fecha y hora de registro de la calificación y/o comentario. |
| `gmap_id` | Id de localización del establecimiento, presente en tabla metadatos-sitio. |
| `rating` | Calificación hecha por el usuario. |
| `text` | Comentario hecho por el usuario. |
| `review` | Comentario tokenizado, para análisis de Machine Learning. |

## Metadatos-Sitios 

| Campo | Valor | Descripción | Tipo |
| --- | --- | --- | --- |
| name | San Soo Dang | El nombre del lugar | object |
| address | "San Soo Dang, 761 S Vermont Ave, Los Angeles, CA 90005" | La dirección del lugar | object |
| gmap_id | 0x80c2c778e3b73d33:0xbdc58662a4a97d49 | El identificador único de Google Maps para el lugar | object |
| latitude | 34.0580917 | Las coordenadas geográficas del lugar | float64 |
| longitude | -118.2921295 | Las coordenadas geográficas del lugar | float64 |
| category | ["Korean restaurant"] | La categoría del lugar | object |
| avg_rating | 4.4 | La calificación promedio del lugar basada en las reseñas de los usuarios | float64 |
| num_of_reviews | 18 | El número total de reseñas que los usuarios han dejado | int64 |
| price | "$" | El rango de precios del lugar | int64 |
| hours | [["Thursday","6:30AM–6PM"]] | El horario de apertura del lugar para cada día de la semana | object |
| state | "Open • Closes 6PM" | El estado actual del lugar, por ejemplo, si está abierto o cerrado | object |
| relative_results | ["0x80c2c78249aba68f:0x35bf16ce61be751d"] | Otros lugares relacionados sugeridos por Google Maps | object |
| url | "https://shre.ink/rKZM" | El enlace a la página de Google Maps del lugar | object |
| Service options | ["Takeout","Dine-in","Delivery"] | Las opciones de servicio disponibles, como para llevar, comer en el lugar o entrega a domicilio | object |
| Accessibility | ["Wheelchair accessible entrance"] | Las características de accesibilidad del lugar | object |
| Offerings | ["Comfort food"] | Lo que ofrece el lugar | object |
| Amenities | ["Good for kids"] | Las comodidades disponibles | object |
| Atmosphere | ["Casual"] | El ambiente del lugar | object |
| Payments | ['NFC mobile payments'] | Los métodos de pago aceptados | object |
| Popular for | ['Dinner', 'Solo dining'] | Para qué es popular el lugar | object |
| Dining options | ['Lunch', 'Dinner'] | Las opciones de comedor disponibles | object |
| Crowd | ['Groups'] | El tipo de multitud que frecuenta el lugar | object |
| Highlights | ['LGBTQ friendly', 'Transgender safespace'] | Los aspectos más destacados del lugar | object |
| is_food_related | True | Indica si el lugar está relacionado con la comida | object |
| rating_group | [4, 5) | grupo del rating | float64 |


## Workflow

![workflow](https://github.com/mreliflores/PF-Henry/blob/main/assets/Workflow.png?raw=true)


## MVP Machine Learning

![MVP](https://github.com/mreliflores/PF-Henry/blob/main/assets/MVP.png?raw=true)

## MVP Data Analytics

![Reviews_analytics](https://github.com/JuanPa2608/PF-Henry/blob/main/assets/portada_DataAnalytics.jpg)
