<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

<h1 align="center"> PROYECTO INDIVIDUAL N°1</h1>
<hr>

 
<h2 align="center">Machine Learning Operations (MLOps)</h2>
  <hr>
<h3 align="center">Sistema de recomendación de películas</h3>



## Resumen 📃 
<p align="justify">
  En este proyecto es un sistema de recomendacion de peliculas. Toma la informacion de peliculas para identificar y recomendar periculas que le podrian gustar al usuario.

  El proyecto utiliza dos datasets relacionados con películas y actores, llamados "movies_dataset" y "credits" estos datasets se encuentran en la seccion de **Fuente de datos**. A lo largo del proyecto, abordaremos tareas como ETL, EDA, Machine Learning y el despliegue de una aplicación.

</p>



## Requerimientos para el proyecto

<p align="justify">

  Crear una carpeta con el nombre de **dataset** ahi es donde se guardaran y exportaran los csv

  🐍**Python**:  Es un lenguaje de programación de alto nivel, interpretado, versátil y de propósito general que se caracteriza por su simplicidad y legibilidad. 

  💻**Numpy**: Biblioteca en Python que proporciona soporte para arreglos multidimensionales y funciones matemáticas para trabajar con estos arreglos. 

  🐼**Pandas**: Biblioteca de análisis de datos en Python que proporciona estructuras de datos flexibles y herramientas para manipular y analizar datos de manera eficiente.

  📈**Matplotlib**:  Biblioteca de visualización de datos en Python que permite crear gráficos y visualizaciones de manera efectiva.

  📊 **Scikit Learn**: Biblioteca de aprendizaje automático (machine learning) en Python que proporciona herramientas sencillas y eficientes para desarrollar y aplicar una variedad de algoritmos de aprendizaje automático.

  📳**FastAPI**: Es un marco de desarrollo de Python de código abierto diseñado para crear APIs web de manera rápida y eficiente.

  📳**uvicorn**: Es un servidor ASGI (Asynchronous Server Gateway Interface) de alto rendimiento para aplicaciones web escritas en Python..

  🌐**Render**: Plataforma utilizada para el despliegue del modelo y la aplicación.


  tambien se cuenta con un archivo yml donde contiene todo el hambiente que se utilizo para este proyecto ( [ YML ](https://github.com/gdelrio0410/PI_1_Recomendaciones_de_peliculas_ML_OPS/blob/main/environment.yml))

</p>


## Pasos del proyecto 📚
### 1. Extracción, Transformación, Carga ( [ ETL ](https://github.com/gdelrio0410/PI_1_Recomendaciones_de_peliculas_ML_OPS/blob/master/ETL.ipynb))

<p align="justify">

  En esta etapa inicial, se ha realizado el proceso de Extracción, Transformación y Carga (ETL), que involucra la obtención de datos, su procesamiento para asegurar su calidad y la incorporación de la información contenida en los archivos CSV "movies_dataset" y "credits". Estos datos se han extraído y limpiado para luego ser exportados a la carpeta **dataset**.

</p>



### 2. Creacion de funciones( [ Funciones  ](https://github.com/gdelrio0410/PI_1_Recomendaciones_de_peliculas_ML_OPS/blob/master/funciones.ipynb))

<p align="justify">
  En esta seccion se crearan 6 funciones para los endpoints que se consumirán en la API, las funciones son:

+ def **peliculas_idioma( *`Idioma`: str* )**

+ def **peliculas_duracion( *`Pelicula`: str* )**

+ def **franquicia( *`Franquicia`: str* )**

+ def **peliculas_pais( *`Pais`: str* )**

+ def **productoras_exitosas( *`Productora`: str* )**

+ def **get_director( *`nombre_director`* )**
  

</p>



### 4. Implementación de API´s ( [ Main ](https://github.com/gdelrio0410/PI_1_Recomendaciones_de_peliculas_ML_OPS/blob/master/main.py))


<p align="justify">
  se crea un archivo main principal mente con la biblioteca fastAPI y uvicorn bibliotecas necesarias para la creacion de la API, una vez instaladas las bibliotecas se subiran las funciones que se crearon anterior mente y poder disponer de manera local en la web.

  La siguiente es la url que se pondra en el navegador para poder disponer de ella local mente:
  http://127.0.0.1:8000 <br> como se menciono solo funcionara local mente y siempre y cuando el servidor este activado

</p>



### 3. Análisis Exploratorio de Datos( [ EDA ](https://github.com/gdelrio0410/PI_1_Recomendaciones_de_peliculas_ML_OPS/blob/master/EDA.ipynb))

<p align="justify">
  En esta etapa se desarrollara un analizis exploratorio y se visualizaran los datos, esto nos ayudara a entender de una mejor manera el modo en que los datos estan relacionados entre ellos y dandonos la informacion crucial que será de utilidad en las próximas etapas del proyecto.

</p>


### 5. Desarrollo del Modelo de Machine Learning ( [ ML ](https://github.com/gdelrio0410/PI_1_Recomendaciones_de_peliculas_ML_OPS/blob/master/ML.ipynb))


<p align="justify">
  En esta crucial etapa de desarrollo, una vez que hemos adquirido un profundo entendimiento de los datos mediante el análisis y la exploración, estamos listos para avanzar hacia la creación de una funcion que tenga un modelo de recomendación de películas. Utilizaremos las herramientas y técnicas proporcionadas por la biblioteca scikit-learn, una de las más conocidas en el campo del aprendizaje automático.

</p>


### 6. Implemantacion del ML al archivo main ( [ Main ](https://github.com/gdelrio0410/PI_1_Recomendaciones_de_peliculas_ML_OPS/blob/master/main.py))


<p align="justify">
  En esta etapa se implementara la funcion que se creo en el archivo main.py y peuda ser ejecutada en el API.

</p>

### 7. Deployment ( [ Render ](https://pi-recomendacione-peliculas-api-guillermo.onrender.com/docs))


<p align="justify">
  En esta etapa se usara Render para poder permitir que la API pueda ser consumida desde la web.

</p>


## **Links**
+ [despliegue de la aplicación (Render)](https://pi-recomendacione-peliculas-api-guillermo.onrender.com/docs)

+ [Main GitHub](https://github.com/gdelrio0410)

+ [Video (Youtube)]()


## **Fuente de datos**

+ [Dataset](https://drive.google.com/drive/folders/1mfUVyP3jS-UMdKHERknkQ4gaCRCO2e1v): Carpeta con los 2 archivos con datos que requieren ser procesados (movies_dataset.csv y credits.csv), tengan en cuenta que hay datos que estan anidados (un diccionario o una lista como valores en la fila).
<br/>


# Contacto 📱
[Guillermo Del Rio](https://www.linkedin.com/in/guillermo-delrio-807311122/)