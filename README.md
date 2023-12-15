# Proyecto de InnovaAI Analytics

<div align="center">
  <img src="assets\innovaLogo.jpeg">

  <p align="center">
    Análisis de datos para restaurantes en EE. UU.
    <br />
  </p>
</div>

## Situación actual

En la era digital actual, las opiniones de los usuarios se han convertido en una fuente invaluable de información. Las plataformas de reseñas como Yelp y Google Maps permiten a los usuarios compartir sus experiencias sobre diversos negocios, incluyendo restaurantes, hoteles y otros servicios relacionados con el turismo y el ocio.

InnovaAI, nuestra consultora de análisis de datos, ha desarrollado un sistema de recomendación de restaurantes que utiliza técnicas avanzadas de Inteligencia Artificial, Aprendizaje Automático y Big Data para extraer información valiosa de las reseñas de los usuarios. Este sistema está diseñado para ayudar a los foodies, instagramers, youtubers o influencers a aumentar su audiencia al seleccionar de manera eficiente los lugares a los que deben ir para estar siempre en tendencia.

¿Sabías que si uno quisiera visitar todos los restaurantes de Nueva York, se requerirían 22 años para poder conocerlos todos? ¿O acaso sabías que si quisieras degustar un vino en Mendoza, existen cerca de 640 bodegas a tu disposición? Y ni hablar si deseas disfrutar de un plato de pasta en Roma, donde hay alrededor de 4000 opciones gastronómicas. La oferta es prácticamente ilimitada, pero nuestro tiempo no lo es. Por eso, nuestra aplicación está diseñada para ayudar a los amantes de la comida, los foodies, a optimizar su tiempo. Les permitirá descubrir de manera eficiente los mejores lugares, conocer nuevas oportunidades y mantener siempre la misma calidad de contenido. En un mundo donde la oferta gastronómica es abrumadora, nuestra aplicación se convierte en el aliado perfecto para aquellos que buscan estar siempre en tendencia.


## Objetivos

### Objetivo General

Desarrollar, implementar y comercializar un sistema de recomendación de restaurantes mediante la creación de una plataforma integral, basado en un análisis de sentimiento de los reviews de clientes en las plataformas de Yelp y Google Maps. Este sistema estará específicamente diseñado para los estados de Pennsylvania y Florida en los Estados Unidos, empleando técnicas de IA, Big Data y Machine Learning.



### Objetivo Especificos

<div>
  <ul>
    <li>
      1.	Análisis de Sentimientos: Utilizaremos técnicas de procesamiento de lenguaje natural para analizar las reseñas de los restaurantes y determinar las tendencias actuales.
    <li>
      2.	Descubrimiento de Restaurantes: Identificaremos restaurantes con altas calificaciones pero con pocas reseñas, ya que estos son potenciales lugares por descubrir.
    <li>
      3.	Recomendaciones Confiables: Recomendaremos restaurantes que han demostrado consistentemente un alto nivel de calidad a lo largo del tiempo, proporcionando así recomendaciones confiables a nuestros usuarios.
    </li>
  </ul>
</div>

### MPV  
El Producto Mínimo Viable (MVP) es una plataforma de recomendación de restaurantes que proporciona las siguientes características:
La interacción de nuestro cliente con la plataforma tendría la siguiente estructura:
<div>
  <ul>
    <li>
      **Inicio de sesión**: Los clientes pueden acceder a la plataforma utilizando sus credenciales personales.
    </li>
    <li>
      Selección de criterio de restaurantes: Los clientes pueden seleccionar el tipo de restaurantes que desean descubrir. Pueden optar por los mejores restaurantes, lugares por descubrir o restaurantes que garantizan calidad.
    </li>
    <li>
      Visualización de resultados: La plataforma proporcionará una lista de tres restaurantes basada en el criterio seleccionado por el cliente. Estos restaurantes serán seleccionados utilizando un modelo de recomendación basado en datos de Google Maps y Yelp.
    </li>
    <li>
      Retroalimentación del usuario: Los clientes tendrán la opción de proporcionar retroalimentación sobre la precisión de las recomendaciones de la plataforma. Esta retroalimentación será utilizada para mejorar y refinar el modelo de recomendación a lo largo del tiempo.

Este MVP ofrece una solución integral para descubrir restaurantes, proporcionando recomendaciones personalizadas basadas en tendencias actuales, descubrimientos emergentes y restaurantes confiables. Al mismo tiempo, permite a los clientes proporcionar retroalimentación, lo que ayuda a mejorar la precisión y relevancia de las recomendaciones a lo largo del tiempo.

 </li>
  </ul>
</div>

## Alcance

El alcance de este proyecto se extiende a varios aspectos clave, atendiendo a cuatro puntos fundamentales dentro del desarrollo de la arquitectura: extracción de datos, análisis de datos, visualización y sistema de recomendación.

**Cobertura Geográfica**: El sistema se centrará específicamente en los locales de comida en los estados de Pennsylvania y Florida en los Estados Unidos, donde la cantidad de restaurantes, la población y la afluencia turística sean las mayores en proporción a la población total. Sin embargo, el marco subyacente puede ser escalado para incluir otras regiones en el futuro.

**Extracción de Datos**: Recopilaremos y utilizaremos datos de plataformas de reseñas como Google Maps y Yelp.

**Análisis de Datos**: El sistema utilizará técnicas avanzadas de Inteligencia Artificial, Aprendizaje Automático y Big Data para analizar las reseñas de los usuarios. Este análisis permitirá al sistema identificar tendencias, descubrir nuevos restaurantes y recomendar lugares que consistentemente reciben altas calificaciones.

**Visualización y Sistema de Recomendación**: El sistema proporcionará una interfaz de usuario intuitiva que permite a los usuarios iniciar sesión, seleccionar su criterio de restaurantes, visualizar los resultados de la recomendación y proporcionar retroalimentación.

**Iteración y Mejora**: Con la retroalimentación de los usuarios, el sistema será iterado y mejorado continuamente para satisfacer mejor las necesidades de los usuarios.

**Beneficio para los Usuarios**: El objetivo final del sistema es ayudar a los usuarios a descubrir nuevos restaurantes y mantenerse al día con las últimas tendencias gastronómicas, permitiéndoles aprovechar al máximo su tiempo y disfrutar de la mejor gastronomía que el mundo tiene para ofrecer.

Por lo tanto, el alcance de este proyecto abarca desde la extracción y análisis de datos hasta la interacción del usuario, con el objetivo de proporcionar una solución integral para la recomendación de restaurantes.

## Fuera de alcance

**Datos en tiempo real**: Dependiendo de las limitaciones de las API de Google Maps y Yelp, puede que no podamos obtener datos en tiempo real. Esto podría afectar la capacidad del sistema para identificar las tendencias más recientes.

**Análisis de Imágenes**: Aunque las reseñas de texto pueden proporcionar mucha información, las imágenes también son una parte importante de las reseñas de los restaurantes. Sin embargo, el análisis de imágenes podría estar fuera del alcance de este proyecto.

**Personalización profunda**: Si bien podemos personalizar las recomendaciones basándonos en las reseñas, puede que no podamos personalizarlas en función de las preferencias dietéticas individuales o las restricciones alimentarias de los usuarios.

**Cobertura Global**: Aunque el sistema está diseñado para escalar y cubrir otras regiones, la implementación inicial se limitará a Pennsylvania y Florida. La expansión a nivel global podría estar fuera del alcance inicial del proyecto.

**Interacción en tiempo real con los usuarios**: Dependiendo de las limitaciones técnicas y de recursos, puede que no podamos proporcionar características como el chat en vivo o el soporte en tiempo real a los usuarios.

Es importante tener en cuenta estas limitaciones al planificar y ejecutar el proyecto para asegurar que se establezcan expectativas realistas y se entregue un producto de alta calidad.


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
\mathrm{KPI}=\dfrac{TotalR_{actual}^{+}}{TotalR_{actual}}\cdot100
$$
**Justificación:** Este indicador analiza de cómo los sentimientos expresados en las reseñas han cambiado con el tiempo. Identifica patrones y cambios en las percepciones de los clientes a lo largo del tiempo. Si los restaurantes no mantienen una tendencia positiva en el tiempo impacta directamente en la predisposición de las personas a asistir a esos lugares.

**METODOLOGIA DEL TRABAJO**


**Sprint 1 - Comprensión del Negocio y de los Datos**: En este sprint, como consultora de datos, definiremos los objetivos y requisitos del proyecto desde una perspectiva empresarial durante la reunión de planificación. Identificaremos claramente el problema que se va a resolver, que en este caso es desarrollar un sistema de recomendación de restaurantes para los estados de Pennsylvania y Florida en los Estados Unidos. Luego, recopilaremos los datos utilizando los conjuntos de datos de Yelp y Google Maps. Nos familiarizaremos con los datos, identificaremos problemas de calidad de datos, descubriremos las primeras ideas y definiremos hipótesis iniciales.

**Sprint 2 - Preparación de los Datos y Modelado**: Durante este sprint, realizaremos todas las actividades necesarias para construir el conjunto de datos final. Esto puede implicar la limpieza de datos, la integración de datos de varias fuentes, la selección de variables relevantes, la transformación de datos, etc. Luego, seleccionaremos y aplicaremos diversas técnicas de modelado, como el análisis de sentimientos, los modelos predictivos y los sistemas de recomendación. Cada técnica requerirá la configuración de parámetros que pueden ser específicos para los datos.

**Sprint 3 - Evaluación y Despliegue**: En este sprint, construiremos un proceso para evaluar la calidad de los modelos basados en los KPIs definidos. Revisaremos los pasos ejecutados para construir el modelo, para asegurarnos de que se cumplan los objetivos del negocio. En el despliegue, generaremos un informe e implementaremos el sistema de recomendación en un entorno de producción.

Además, cada día se realizarán reuniones diarias de seguimiento (Daily Standup) de 45 minutos con el mentor, para discutir el progreso diario y posibles inconvenientes. Al finalizar cada sprint, se realizará una demo (sprint review meeting) en la que se hará una demostración de los entregables desarrollados, esperando una retroalimentación por parte del mentor.

Esta metodología, que integra el enfoque de Scrum con el proceso estándar de minería de datos (CRISP-DM), asegura un enfoque sistemático y basado en datos para el desarrollo del sistema de recomendación de restaurantes, y permite la iteración y mejora continua basada en la retroalimentación del mentor. Como consultora de datos, nuestro objetivo es proporcionar una solución integral que sea precisa, relevante y útil para los usuarios.





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
