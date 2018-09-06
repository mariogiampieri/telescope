## Mapeando la Lima periférica con data

### Descripción
A nivel global un tercio de los residentes urbanos vive en asentamientos informales, en condiciones muy precarias, muchas veces sin acceso a servicios básicos como agua, saneamiento y electricidad. Mientras tanto, miles de organizaciones –empresariales, civiles y de gobierno- trabajan para proveer estos servicios a través de soluciones alternativas, asequibles y sostenibles de micro-infraestructura. Sin embargo, la mayoría de ellas coincide en tener un gran obstáculo: el acceso a información relevante, precisa y oportuna que pueda ser utilizada para tomar decisiones estratégicas, llegar con servicios a nuevas comunidades necesitadas, y monitorear su impacto a través del tiempo.

El objetivo general del proyecto es explorar las dinámicas físicas, geológicas y sociales de asentamientos humanos informales en relación al cambio climático, y cómo estas son afectadas por este último. El objetivo final es generar un sistema de análisis de riesgo y resiliencia utilizando herramientas de procesamiento de datos, inteligencia artificial (Ai) y algoritmos de aprendizaje, para áreas periféricas urbanas.


### Objectivos Específicos y Actividades
### 1. Desarrollar sistemas de análisis para identificar las características de asentamientos informales de Villa Maria del Triunfo (VMT) y San Juan de Miraflores (SJM)  

  **1.1. Escribir algoritmos de Python para acceder a data de LANDSAT y Copernicus desde “Amazon s3 bucket”**  
    1.1.1. Instalar python, numpy, gdal, boto3, and git  
    1.1.2. Usar boto3 para acceder a archivos alojados en s3  
    1.1.3. Leer y escribir archivos desde s3 satisfactoriamente  
    **1.2. Usar algoritmos NDVI y SAVI para identificar cambios de uso de suelo a lo largo del tiempo**    
    1.2.1. Probar diferentes algoritmos para ejecutar procesos NDVI / SAVI (se puede hacer usando gdal o tbtoolbox en c ++) utilizando las diferentes bandas de imagen provistas en las imágenes satelitales  
    1.2.2. Test different processes to discern things like slope, land use, and ecosystem types from satellite and other capas  
    1.2.3. Probar diferentes algoritmos para discernir elementos como la pendiente, el uso del suelo y los tipos de ecosistemas de imágenes satelitales y otras capas de información  
    1.2.4. Automatizar y guardar los resultados a s3  
    **1.3 Desarrollar algoritmos de aprendizaje automatizado para identificar asentamientos informales y viviendas**  
    1.3.1 Utilizar los conjuntos de datos y parámetros identificados en 1.2 (junto con las imágenes satelitales) como entradas para los algoritmos de aprendizaje automatizado  
    1.3.2 Iterar usando diferentes características, en diferentes períodos de tiempo, para probar la fortaleza del modelo a través del espacio (en diferentes condiciones geográficas) y el tiempo (diferentes momentos climáticos, políticos, económicos); verificar la capacidad del modelo para predecir en base a diferentes puntos en el tiempo para la data que tenemos disponible
  ### 2. Interpretar los resultados y proponer soluciones para mejorar la calidad de vida de estos asentamientos.
  **2.1. Analizar los resultados del modelo y desarrollar reportes sobre los asentamientos humanos en SJM y VMT**  
  2.1.1. Identificar y analizar las principales características / patrones de crecimiento de las comunidades de SJM y VMT en relación a otros indicadores socioeconómicos  
  2.1.2. Identificar los principales hotspots de vulnerabilidad frente a riesgos tales como deslizamientos y sismos. (áreas de riesgo reconocidas y que pueden ser predecidas de acuerdo al modelo desarrollado)  
  2.1.3. Identificar las oportunidades existentes para el desarrollo de infraestructura alternativa (atrapanieblas, energía alternativa, bosques productivos, etc.)  
  **2.2. Desarrollar recomendaciones para las áreas investigadas**  
  2.2.1.  Discutir sobre las limitaciones que tienen SJM y VMT para soportar un mayor crecimiento urbano / poblacional, y cuáles son las áreas de mayor riesgo y las que tienen características buenas para el desarrollo urbano -basado en el modelo y percepción personal.  
  2.2.2.  Desarrollar un reporte de recomendaciones sobre el potencial de crecimiento urbano que al mismo tiempo reduzca los riesgos de las comunidades analizadas.  
  2.2.3.  Desarrollar recomendaciones para potenciar el acceso de ambas comunidades a servicios e infraestructura alternativa teniendo en cuenta sus condiciones socioeconómicas, urbanas y de riesgo previamente analizadas.

### Course Schedule
*8/23*

Introduction to the project and the overarching themes (listed above). What are the conditions of growth in Lima? What are the issues currently faced in informal settlements today?

#### *8/30*

**Diseño del plan de trabajo (Fase 1)**


What are the specific questions we are trying to answer? What are the tools and datasets we have at our disposal? What are the limitations to these methods, and how might these limitations be addressed separately?

We will discuss together strategies for addressing the research questions we have set out together and create a work plan for the following weeks.

#### *9/6*
**Introduction to the software development environment / project setup.**
1.1.1 Instalar python, numpy, gdal, boto3, and git

#### *9/13*

**Discussion of LANDSAT best practices; discuss initial results; adjust workflow as necessary**

Tarea:

_come prepared with software environment set up_
- _1.1.2 Usar boto3 para acceder a archivos alojados en s3_
- _1.1.3 Leer y escribir archivos desde s3 satisfactoriamente_

Go over algorithms developed for data processing and retrieval plan out next steps in terms of using machine learning to further explore and predict urban patterns.
Introduction to raster processing

1.2.1 Probar diferentes algoritmos para ejecutar procesos NDVI / SAVI (se puede hacer usando gdal o tbtoolbox en c ++) utilizando las diferentes bandas de imagen provistas en las imágenes satelitales


#### *9/20*

**Preliminary Design (Fase 1) Review**

1.2.2 Test different processes to discern things like slope, land use, and ecosystem types from satellite and other capas

1.2.3 Probar diferentes algoritmos para discernir elementos como la pendiente, el uso del suelo y los tipos de ecosistemas de imágenes satelitales y otras capas de información

1.2.4 Automatizar y guardar los resultados a s3


#### *9/27*

**1.3 Desarrollar algoritmos de aprendizaje automatizado para identificar asentamientos informales y viviendas**

Tarea: 
- Make sure machine learning tools are set up properly

1.3.1 Utilizar los conjuntos de datos y parámetros identificados en 1.2 (junto con las imágenes satelitales) como entradas para los algoritmos de aprendizaje automatizado


#### *10/4*

1.3.2 Iterar usando diferentes características, en diferentes períodos de tiempo, para probar la fortaleza del modelo a través del espacio (en diferentes condiciones geográficas) y el tiempo (diferentes momentos climáticos, políticos, económicos); verificar la capacidad del modelo para predecir en base a diferentes puntos en el tiempo para la data que tenemos disponible

#### *10/11*

**Fase 1 Presentations: Review results from machine learning tests, as well as NDVI and SAVI**

#### *10/18*

2.1.1 Identificar y analizar las principales características / patrones de crecimiento de las comunidades de SJM y VMT en relación a otros indicadores socioeconómicos

2.1.2 Identificar los principales hotspots de vulnerabilidad frente a riesgos tales como deslizamientos y sismos. (áreas de riesgo reconocidas y que pueden ser predecidas de acuerdo al modelo desarrollado)

#### *10/25*

Tarea: 
- 2.1.3 Identificar las oportunidades existentes para el desarrollo de infraestructura alternativa (atrapanieblas, energía alternativa, bosques productivos, etc.)

2.2.1 Discutir sobre las limitaciones que tienen SJM y VMT para soportar un mayor crecimiento urbano / poblacional, y cuáles son las áreas de mayor riesgo y las que tienen características buenas para el desarrollo urbano -basado en el modelo y percepción personal.


#### *11/01*

2.2.2 Desarrollar un reporte de recomendaciones sobre el potencial de crecimiento urbano que al mismo tiempo reduzca los riesgos de las comunidades analizadas 

2.2.3 Desarrollar recomendaciones para potenciar el acceso de ambas comunidades a servicios e infraestructura alternativa teniendo en cuenta sus condiciones socioeconómicas, urbanas y de riesgo previamente analizadas.

**Final review of analysis and recommendations. Preparation for final presentations the following week.**

**Discussion of synthesis of results: what can our results help decision makers learn about the periphery of Lima? How can these results be used to improve the quality of life in peripheral areas? What is missing from our analysis?**

#### *11/08*

**Final Presentations at UTEC**
