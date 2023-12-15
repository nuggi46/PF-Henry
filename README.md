# Proyecto de InnovaAI Analytics

<div align="center">
  <img src="assets\innovaLogo.jpeg">

  <p align="center">
    Análisis de datos para restaurantes en EE. UU.
    <br />
  </p>
</div>

## Situación actual

En la era digital actual, las opiniones de los usuarios se han convertido en una fuente de información valiosa para todos. Las plataformas de reseñas como Yelp y Google Maps permiten a los usuarios compartir sus experiencias sobre diversos negocios, incluyendo restaurantes, hoteles y otros servicios relacionados con el turismo y el ocio. 

Considerando la situación actual presenta una oportunidad emocionante para utilizar la ciencia de datos (IA, ML, Big Data) para extraer información valiosa de las reseñas de los usuarios y ayudar a los clientes a tomar decisiones basada en datos que mejoren su negocio. Nuestra consultora InnovaAI ha desarrollado una aplicación destinada a todos aquellos que se consideren foodies, instagramer,youtuber o influencers y deseen aumentar su audiencia a través de un sistema de recomendación que les ayuda a seleccionar de forma eficiente a que lugares ir para estar siempre en tendencia.

Sabias que si uno quisiera visitar todos los restaurantes de Nueva York, se requieren 22 años para poder conocerlos todos? O acaso sabias que si quisieras tomar un vino en Mendoza, existen cerca de 640 bodegas? Y ni te digo si queres ir a comer un plato de pasta en Roma, hay alrededor de 4000 opciones de comida. Por lo tanto la oferta es ilimitada pero el tiempo no, y nuestra aplicación ayudará a los foodies a asistir de manera eficiente a los mejores lugares, conocer nuevas oportunidades y mantener siempre la misma calidad de contenido.


## Objetivos

### Objetivo General

Desarrollar un sistema de recomendación de restaurantes basada en la información proveida por Google Maps y Yelps para Estados Unidos, especificamente para los estados de Pennsylvania y Florida.

### Objetivo Especificos

<div>
  <ul>
    <li>
      Recomendar restaurantes en tendencia basados en un analisis de sentimientos.
    <li>
      Recomendar restaurantes listos para ser descubiertos.
    <li>
      Recomendar restaurantes que nunca te van a fallar.
    </li>
  </ul>
</div>

### MPV

La interacción de nuestro  cliente con la plataforma tendría la siguiente estructura:
<div>
  <ul>
    <li>
      Inicio de sesión: El cliente inicia sesión en la plataforma utilizando sus credenciales.
    <li>
      Selección de criterio de selección de restaurantes: Si quiere los mejores restaurantes, lugares por descubrir o asegurarse calidad.
    <li>
      Visualización de resultados: proveerá una opción de 3 lugares para disfrutar el arte de comer.
    </li>
      Retroalimentación del usuario: El cliente tiene la opción de proporcionar retroalimentación sobre la precisión de la plataforma para evaluar posibles mejores del modelo a futuro.
    </li>
  </ul>
</div>

## Alcance

El proyecto atiende a cuatro puntos fundamentales dentro del desarrollo de la arquitectura: extracción de datos, análisis de datos, visualización y sistema de recomendación.

Se basará especificamente en locales de comida y en los estados de Estados Unidos en los cuales la cantidad de restaurantes, población y afluencia turistica sean las mayores en proporción a la población total.

## Fuera de alcance

**Análisis en Tiempo Real:** Aunque nuestro sistema de análisis de sentimientos y modelo predictivo proporcionará información valiosa, no será capaz de analizar las reseñas en tiempo real. Esto se debe a las limitaciones técnicas y al tiempo necesario para procesar y analizar los datos.

**Integración con Otras Plataformas de Reseñas:** Nuestro enfoque actual se centra en Yelp y Google Maps. La integración con otras plataformas de reseñas podría proporcionar una visión más completa, pero está fuera de nuestro alcance actual.
Estas limitaciones representan oportunidades para la continuidad y expansión del proyecto en el futuro.


## KPIs a evaluar:

### 🎯 KPI N°1: Aumento del numero de visitas a los locales

**Objetivo:** Incrementar en al menos 5% el número de reseñas emitidas por los consumidores para el proximo año en los locales analizados.

**Formula:**

$$
\mathrm{KPI}=\dfrac{R_{nuevas} - R_{pasadas}}{R_{pasadas}}\cdot100
$$

**Justificación:** Este indicador mide la variación de la captación de nuevos consumidores en intervalo interanual, con el puede medirse el exito de las campañas de marketing.

### 🎯 KPI N°2: Aumento del nivel de satisfacción del consumidor

**Objetivo:** Incrementar en al menos 5% el número de reseñas positivas para el proximo año en los locales analizados.

**Formula:**

$$
\mathrm{KPI}=\dfrac{R_{nuevas}^{+} - R_{pasadas}^{+}}{R_{pasadas}^{+}}\cdot100
$$

**Justificación:** Este indicador mide la variación de la satisfacción del consumidor en un intervalo anual, un valor positivo indica un incremento de la satifacción.

### 🎯 KPI N°3: Aumento el rating promedio del negocio.

**Objetivo:** Incrementar en al menos 2% puntos el rating medio del negocio en un intervalo interanual.

**Formula:**

$$
\mathrm{KPI}
=\dfrac{\mathrm{Rating_{actual}}-\mathrm{Rating_{previo}}}{\mathrm{Rating_{previo}}}\cdot100
$$

**Justificación:** Este indicador mide la variación de la popularidad del negocio según sus consumidores, mientras mas alto sea mas alta la probabilidad de obtener nuevos consumidores.

### 🎯 KPI N°4: Tendencias de Sentimientos a lo largo del tiempo.

**Objetivo:** Mantener una tendencia positiva en el tiempo basados en el promedio de sentimientos y la desviación estandar.

**Formula:**

$$
\mathrm{KPI}
=\dfrac{\mathrm{TotalR^{+}_{actual}}}{\mathrm{TotalR_{actual}}}\cdot100
$$


**Justificación:** Este indicador analiza de cómo los sentimientos expresados en las reseñas han cambiado con el tiempo. Identifica patrones y cambios en las percepciones de los clientes a lo largo del tiempo. Si los restaurantes no mantienen una tendencia positiva en el tiempo impacta directamente en la predisposición de las personas a asistir a esos lugares.

## Cronograma del proyecto

Se plantea el siguiente cronograma para cumplir con los objetivos del proyecto

<a href="https://lucid.app/lucidspark/3cb5c4c0-dee3-4f20-aa8b-1d86bae6bbe0/edit?invitationId=inv_6c32f21b-0efb-4471-a583-939fc376e67f&page=0_0#"><img src="assets\cronograma.png"></a>

## Stack tecnologico

<div style="display: flex; justify-content: space-between; flex-wrap:wrap; width: 100%">
    <img src="https://api.iconify.design/vscode-icons:file-type-python.svg" 
        style="width: 40px; margin-right:40px"/>
    <img src="https://api.iconify.design/devicon:pandas.svg" 
        style="width: 40px; margin-right:40px"/>
    <img src="https://api.iconify.design/devicon:matplotlib.svg" 
        style="width: 40px; margin-right:40px"/>
    <img src="https://api.iconify.design/logos:seaborn-icon.svg" 
        style="width: 40px; margin-right:40px"/>
    <img src="https://api.iconify.design/devicon:googlecloud.svg" 
        style="width: 40px; margin-right:40px"/>
    <img src="https://api.iconify.design/logos:apache-spark.svg" 
        style="width: 40px; margin-right:40px"/>
    <img src="https://api.iconify.design/simple-icons:polars.svg" 
        style="width: 40px; margin-right:40px"/>
</div>

## Colaboradores

<div>
  <ul>
    <li>
      Monica Molinas: <b>Data Scientist</b> 👩🏻‍🔬
    </li>
    <li>
      Alexis Palacio: <b>Data Scientist</b> 👨🏻‍🔬
    </li>
    <li>
      Piero Li: <b>Data Enginner</b> :construction_worker:
    </li>
    <li>
      Juan Pablo Espinoza: <b>Data Analyst</b> :chart_with_upwards_trend:
    </li>
    <li>
      Nelly Molina: <b>Data Analyst</b> :chart_with_upwards_trend:
    </li>
    <li>
      Elí Flores: <b>Data Analyst</b> :chart_with_upwards_trend:
    </li>
  </ul>
</div>

## Enlaces a datasets

<b>Florida:</b>

[reviews-Florida](https://drive.google.com/file/d/1-5AFCLJbYRE1r8q0QWu0zdqABiHp8ioq/view?usp=sharing)

[reviews-token-Florida](https://drive.google.com/file/d/1w2qPs3wvMgQ2wU5cmQj8NbKvOXOq7LRv/view?usp=sharing)


<b>Pennsylvania:</b>

[reviews-Pennsylvania](https://drive.google.com/file/d/1-5Vj2VEUJWiZhWMW6x6sKrVeaZZmv3WD/view?usp=sharing)

[reviews-token-Pennsylvania](https://drive.google.com/file/d/128HUtLuHcc_VGBQKlBPjm1twTYx8ckk1/view?usp=sharing)


<b>Utah:</b>

[reviews-Utah](https://drive.google.com/file/d/1_C_1bQnJxdftrvz6QVv9HylbdB6rvzil/view?usp=sharing)

[reviews-token-Utah](https://drive.google.com/file/d/1FlAbcVyPDXldOQRYsDaGAJJbTpmG12nl/view?usp=sharing)
