
## TODO:##
- set up testing environment
- a new virtual environment, to use for the walkthrough; 
- set up the requirements.txt file
- figure out how to handle file access (either through s3 or dropbox or postgis)

## Objetivos Generales:
A nivel global un tercio de los residentes urbanos vive en asentamientos informales, en condiciones muy precarias, muchas veces sin acceso a servicios básicos como agua, saneamiento y electricidad. Mientras tanto, miles de organizaciones –empresariales, civiles y de gobierno- trabajan para proveer estos servicios a través de soluciones alternativas, asequibles y sostenibles de micro-infraestructura. Sin embargo, la mayoría de ellas coincide en tener un gran obstáculo: el acceso a información relevante, precisa y oportuna que pueda ser utilizada para tomar decisiones estratégicas, llegar con servicios a nuevas comunidades necesitadas, y monitorear su impacto a través del tiempo.

El objetivo general del proyecto es explorar las dinámicas físicas, geológicas y sociales de asentamientos humanos informales en relación al cambio climático, y como estas son afectadas por este último. El objetivo final es generar un sistema de análisis de riesgo y resiliencia utilizando herramientas de procesamiento de datos, inteligencia artificial (Ai) y algoritmos de aprendizaje, para áreas periféricas urbanas.

## Specific Objectives (from the submitted proposal)
1. Generar un sistema de procesamiento de imágenes satelitales multibanda para diferenciar patrones de desarrollo, áreas de riesgo, pendientes inhabitables y diferentes zonas ecológicas.
  - process LANDSAT imagery over time using NDVI, EDVI, SAVI, etc.

2. Explorar algoritmos de aprendizaje que puedan preveer el crecimiento poblacional y morfología urbana en base a imágenes históricas satelitales e información demográfica.
  - label-maker, tensorflow

3. Reporte sobre las diferentes maneras en las que los asentamientos humanos son afectados por el cambio climático.
  - Census based work? Census data over time?
  
4. Reporte de recomendaciones para estas áreas afectadas.
  - bringing it all together
  
## Getting Started
This project will rely heavily on the Python programming language and associated tools to build and use tools to investigate urban areas. It requires a bit of setup, for which I recommend using a virtual environment so as to not accidentally break your system python environment.
- pip
- virtualenv
- create virtualenv for python 3.x
- make requirements.txt (rasterio, tippecanoe, pandas, geopandas, label-maker, gdal, shapely)

## Topics
### phase 1
- change over time based on ndvi/edvi/topo/soil/etc.: creating a training set based on characteristics of existing urban areas, how places have urbanized over time, and where places might urbanize next
- using label-maker and tensorflow to identify hi-res buildings and features in the apollo mapping imagery that we already have: https://github.com/developmentseed/label-maker/blob/master/examples/walkthrough-tensorflow-object-detection.md
- it would also be interesting to analyze on a per-unit-area basis the characteristics of different areas of the city- based on osm and/or the city data that we have (what are the characteristics/correlations of good and bad service areas?)

