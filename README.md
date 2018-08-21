# telescope

## TODO: set up testing environment, a new virtual environment, to use for the walkthrough; set up the requirements.txt file; figure out how to handle file access (either through s3 or dropbox or postgis)

## Getting Started
This project will rely heavily on the Python programming language and associated tools to build and use tools to investigate urban areas. As such, it
- pip
- virtualenv
- create virtualenv for python 3.x
- create virtualenv for python 3
- make requirements.txt (rasterio, tippecanoe, pandas, geopandas, label-maker)

## Topics
### phase 1
- change over time based on ndvi/edvi/topo/soil/etc.: creating a training set based on characteristics of esisting urban areas, how places have urbanized over time, and where places might urbanize next
- using label-maker and tensorflow to identify hi-res buildings and features in the apollo mapping imagery that we already have: https://github.com/developmentseed/label-maker/blob/master/examples/walkthrough-tensorflow-object-detection.md
- it would also be interesting to analyze on a per-unit-area basis the characteristics of different areas of the city- based on osm and/or the city data that we have (what are the characteristics/correlations of good and bad service areas?)
