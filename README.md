## Mapeando la Lima periférica con data ##
*UTEC Proyecto Interdiscipinario III, Primavera 2018*

*Dr. Jorge Abad, Mario Giampieri, Sofia Garcia*


![Lima 1984 - present](./img/lima_gif_02s.gif)
*Lima Sur, 1984-present*

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
**Start by cloning this repository on your local machine** (using `git clone  https://github.com/mariogiampieri/telescope.git`).
This project will rely heavily on the Python programming language and associated tools to build and use tools to investigate urban areas. It requires a bit of setup. The following steps will guide you through the Python installation process.

### Anaconda
Anaconda is a great development environment for python, and makes installing certain packages much easier than using pip alone: https://www.anaconda.com/download/. It also makes it easy to manage and switch between python 2.* and python 3.*. Install the Python 2.7 version.

- create virtual env using anaconda
- `activate telescope`
- `conda install gdal pandas geopandas shapely fiona boto3`
- enter 'y' when prompted to confirm installation of packages and their dependencies.

We are now ready to begin programming! Type `jupyter notebook` from the command prompt and navigate to the python_notebooks folder.

## Topics
### phase 1
- change over time based on ndvi/edvi/topo/soil/etc.: creating a training set based on characteristics of existing urban areas, how places have urbanized over time, and where places might urbanize next
- using label-maker and tensorflow to identify hi-res buildings and features in the apollo mapping imagery that we already have: https://github.com/developmentseed/label-maker/blob/master/examples/walkthrough-tensorflow-object-detection.md
- it would also be interesting to analyze on a per-unit-area basis the characteristics of different areas of the city- based on osm and/or the city data that we have (what are the characteristics/correlations of good and bad service areas?)

## TODO
- pre-identify images that have acceptible cloud cover and remove all others.
- move log files in s3 into folder so things aren't so disorganized.
- make file with utec connection parameters and add to root dir for use with boto3
- start python library and write function that auto-connects to s3 bucket using utec connection parameters. place this function at the beginning of any python notebook template files.
