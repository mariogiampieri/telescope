
## TODO:
- ~~set up testing environment
- ~~a new virtual environment, to use for the walkthrough; 
- ~~set up the requirements.txt file
- ~~figure out how to handle file access (either through s3 or dropbox or postgis)~~ use boto3 to access kawsay s3 bucket with files
- upload files to s3 (in process; very slow, lots of files which are going to bucket in Sao Paolo)

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
This project will rely heavily on the Python programming language and associated tools to build and use tools to investigate urban areas. It requires a bit of setup, for which I recommend using a virtual environment so as to not accidentally break your system python environment. The following steps will guide you through the Python installation process.

### Pip
Pip is a package manager for Python. It allows you to easily install third-party packages to use with Python. It can be installed using the [instructions on the PyPA website](https://pip.pypa.io/en/stable/installing/). Pip will be used to install the rest of the dependencies for this project

Once pip is installed, we can use it to install all of the Python dependencies required for this project by typing `pip install -r requirements.txt` from the project directory. (This tells pip to read the requirements.txt file, which contains all of the necessary python packages for this project).

### Virtual Environment
`virtualenv` is a pip package that is used to isolate python packages for a specific folder. In some cases, a project will require versions of packages other than ones used by your operating system's copy of python. The same is true of dependencies of packages that a project requires. `virtualenv` allows you to isolate python packages so as to not interfere with your system python. [This guide](https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv) has a great description of the install process, but in a nutshell you can use the following commands:
- `pip install virtualenv`
- `cd telescope`
- `virtualenv telescope` <- this creates a virtual environment within our project folder called 'telescope', although you can name it whatever you want.
- To enable the virtual environment, change into the project directory and type `source telescope/bin/activate`. You should now see `telescope` in your command prompt. 
- When you are finished, type `deactivate`.

You may find it easier/more pleasant to use the pip package `virtualenvwrapper` when working with virtual environments. Installation instructions can be found [here](https://docs.python-guide.org/dev/virtualenvs/#virtualenvwrapper).

### Tippecanoe
Tippecanoe is a Mapbox utility that builds vector tiles datasets from large datasets and is used by label-maker to prepare data for training. It is easy to install on OSX and Linux, but to install on Windows you have to build from source. Let's chat if this is required.

### Jupyter (optional)
[Jupyter notebooks](http://jupyter.org/) is a great way to run smaller chunks of Python code at a time. It is not required (you can run python scripts from the terminal or through a number of interpreters) but is an option. It can be installed with pip or Anaconda as [explained here](http://jupyter.org/install.html).

## Topics
### phase 1
- change over time based on ndvi/edvi/topo/soil/etc.: creating a training set based on characteristics of existing urban areas, how places have urbanized over time, and where places might urbanize next
- using label-maker and tensorflow to identify hi-res buildings and features in the apollo mapping imagery that we already have: https://github.com/developmentseed/label-maker/blob/master/examples/walkthrough-tensorflow-object-detection.md
- it would also be interesting to analyze on a per-unit-area basis the characteristics of different areas of the city- based on osm and/or the city data that we have (what are the characteristics/correlations of good and bad service areas?)

