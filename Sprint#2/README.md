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



## Workflow

![workflow](https://github.com/mreliflores/PF-Henry/blob/main/assets/Workflow.png?raw=true)


## MVP Machine Learning



## MVP Data Analytics