![banner_tipster](https://github.com/cistelsa/Commerce_Data_Analysis_and_Recommendations/assets/17438992/5972fc1a-725d-43b7-9d7b-6cd76f0ad165)


# <h1 align=center> **COMMERCE DATA ALALYSIS AND RECOMMENDATIONS** <img src="5. Sources/Images/tipster.jpg" width="50px"/></h1>



-----

# <font color='#307A71'>**Tabla de Contenido**</font>

- [El Repositorio](#el-repositorio)
- [Autores](#autores)
- [Introducción](#introducción)
- [Entendimiento de la Situación Actual del Sector](#entendimiento-de-la-situación-actual-del-sector)
- [Objetivos y Alcance](#objetivos-y-alcance)
- [Key Performance Indicators - KPI's](#key-performance-indicators---kpis)
- [Stack Tecnologico - Pipeline](#stack-tecnológico---pipeline)
- [Metodología de Trabajo](#stack-tecnológico---pipeline)
- [Datos](#datos)
- [Modelo de Recomendación](#modelo-de-recomendacion)
-----


-----
# <font color='#307A71'>**El Repositorio**<a name="repo"></a></font>

En el repositorio se encuentran los siguientes archivos:

- `1. ETL`: Archivos en los cuales se documenta el proceso de ETL (Extract, Transform, Load).
- `2. Datasets`: Contiene el conjuntos de datos normalizados, respecto del origen, para ser utilizados en el proyecto y que no provienen de API's.
- `3. EDA`: Archivos en los cuales se documenta el proceso de EDA (Exploratory Data Analysis).
- `4. Model ML`: Jupyter Notebooks con pruebas para el desarrollo del Modelo de Machine Learning para el proyecto.
- `5. Sources`: Aquí se encuentra los archivos anexos como imágenes, videos y demás recursos necesarios para el desarrollo del proyecto.
- `6. Documentation`: Documentos relacionados al desarrollo del proyecto.
-----


-----
# <font color='#307A71'>**Autores** <a name="autores"></a></font>

# <h1 align=center> <img src="5. Sources/Images/equipo.png" width="900px"/></h1>


|Nombre               | Rol                     | Correo                     | GitHub                                          | Linkedin|
|---------------------|-------------------------|----------------------------|-------------------------------------------------|---------|
|Leydy Lucena Peñaloza Rojas |Technical Project Managet, Data Engineer, Data Scientist |leydy.penaloza@gmail.com    |[leydypenaloza](https://github.com/leydypenaloza)    |[leydy-penaloza](www.linkedin.com/in/leydy-penaloza)|
|Edisson Camilo Ortiz López  |Data Analyst, Data Engineer, Visual Designer |eortiz@cistelsa.com   |[cistelsa](https://github.com/cistelsa)            |[camilo-ortiz-cistelsa](https://www.linkedin.com/in/camilo-ortiz-cistelsa)|
|Aldemar Bohorquez Rodriguez |Data Engineer, Data Scientist, Machine Learning Engineer|abr942010@gmail.com   |[aldemarbr94](https://github.com/aldemarbr94)            |[aldemar-bohorquez-rodriguez](https://www.linkedin.com/in/aldemar-bohorquez-rodriguez/)|
|Mayren Gabriela Silva Basto |Data Analyst, Data Engineer, Machine Learning Engineer  |mayrensilva95@gmail.com     |[MayrenS95](https://github.com/MayrenS95)        |[mayren-gabriela-silva-basto](https://www.linkedin.com/in/mayren-gabriela-silva-basto-67b645181/)|
|Yesica Milagros Leon Ccahuana |Data Analyst, Data Engineer, Data Scientist|agrostopo@gmail.com|[yesicamilagros](https://github.com/yesicamilagros)|[yesica-leon-ccahuana](https://www.linkedin.com/in/yesica-leon-ccahuana-1706a7216/)|

-----

-----
# <font color='#307A71'>**Introducción**<a name="introduccion"></a></font>


Como consultores de datos, centrados en el análisis del mercado del turismo estadounidense, presentamos a continuación el desarrollo de este proyecto. Nuestra misión es proporcionar a los clientes finales herramientas que les permitan mejorar sus campañas de marketing, tomar decisiones informadas sobre inversiones y ofrecer recomendaciones basadas en experiencias previas para sus usuarios.

El mercado del turismo en Estados Unidos es dinámico y competitivo. Nuestro proyecto aborda la necesidad de comprender mejor este mercado y aprovechar sus oportunidades; con este objetivo en mente, hemos desarrollado un conjunto de herramientas y análisis que ayudarán a nuestros clientes a optimizar sus estrategias.

En este repositorio, encontrará detalles sobre nuestra metodología, análisis de datos, modelos de machine learning y visualizaciones que respaldan nuestras recomendaciones. Esperamos que este proyecto brinde claridad y valor a nuestros clientes, mejorando la toma de decisiones y las experiencias de sus usuarios en el mercado del turismo norteamericano.

-----

-----
# <font color='#307A71'>**Entendimiento de la Situación Actual del Sector**<a name="entendimiento"></a></font>

En la actualidad la opinión de los usuarios se ha convertido en un insumo importante para la toma de decisiones en las organizaciones. Sin importar el tamaño de las mismas, la experiencia que proporciona un producto y/o servicio se ha venido transformando con el paso del tiempo y el uso de las tecnologías, pues estas permiten el estar más interconectados, indistintamente del lugar en el que nos encontremos.

“El 52% de los usuarios a nivel global creen que las empresas deben tomar acciones para mejorar a partir del feedback de sus clientes”, según Microsoft. Las empresas son conscientes de lo anterior y del nivel de afectación que conlleva la facilidad con la que hoy día los usuarios comunican sus experiencias y como esto influye en las decisiones de posibles clientes, permitiendo el reaccionar, transformarse, anticiparse a diversas acciones del usuario, incluso fidelizar al mismo.

Por tanto, existen plataformas en la web que permiten recopilar esta información, como Yelp, que es una plataforma de reseñas de todo tipo de negocios, restaurantes, hoteles, servicios entre otros. Los usuarios utilizan el servicio y luego suben su reseña según la experiencia que han recibido; asimismo, Google posee una plataforma de reseñas de todo tipo de negocios, restaurantes, hoteles, servicios, entre otros integrada en su servicio de localización y mapas, Google Maps.

Sin embargo, toda esta información no es de utilidad sin el procesamiento y manejo adecuado, por ello, gracias al avance de la ciencia enfocada en el análisis de datos, se pueden usar herramientas que permiten identificar el estado actual, tendencias, pronósticos y supuestos en diversos escenarios, para finalmente tomar las decisiones pertinentes que permitan aumentar la satisfacción del cliente, posicionar la marca y utilidad de la organización.

-----

-----
# <font color='#307A71'>**Objetivos y Alcance**<a name="objetivos"></a></font>

## **_♦ Objetivo General_**

Proporcionar al cliente un análisis detallado de la opinión de sus usuarios en distintas plataformas con el fin de planificar nuevas estrategias.

## **_♦ Objetivos Específicos_**

* Recopilar, depurar y disponibilizar la información en un Data Warehouse (proceso de ETL) de forma estática y dinámica.
* Analizar el conjunto de datos cargados en el Data Warehouse y resumir sus principales características (proceso del EDA).
* Entrenar y poner en producción un modelo de Machine Learning que permita predecir cuáles son los rubros del negocio que más crecerán o decaerán y dónde es conveniente emplazar nuevos locales del negocio.
* Generar a través de Machine Learning un sistema de recomendación del negocio para los usuarios con el propósito de que estos puedan conocer nuevas temáticas basados en sus experiencias previas.

## **_♦ Alcance_**

* Se seleccionarán otras plataformas de información, además de Yelp y Google Maps, que contengan información pertinente y permitan complementar el proceso de ETL y EDA.
* Se usarán diversas herramientas tecnológicas, como Micfrosoft Fabric, para llevar a cabo el proceso de ETL y EDA.
* Se facilitará un informe y dashboard al cliente con los procesos de ETL, EDA, predicción del comportamiento de los rubros y sistema de recomendación del negocio a través de una API o aplicación.
-----

-----
# <font color='#307A71'>**Key Performance Indicators - KPI's**<a name="kpi"></a></font>

 KPIs propuestos :

+ <font color='##74A608'>**Índice de satisfacción del cliente :**</font> La opinión inmediata de los clientes tras finalizar la interacción con la empresa es una
buena forma de conocer su percepción sobre el servicio brindado .

   numero_de_clientes_satisfechos/total_de_clientes_encuestados*100  
  Es decir, el nivel de puntuación de satisfacción del cliente de la empresa que utilizamos en este ejemplo es del 72,5%.
  

+ <font color='##74A608'>**NPS(net promoter score) Puntuación Neta del Promotor:**</font> evalúa el grado en que un cliente recomienda un cierto rubro (si un cliente aprecia un servicio lo suficiente como para recomendarla a otros)
% Detractores - % Promotores = NPS

+ <font color='##74A608'>**Índice de Penetración del Mercado (MPI):**</font> la penetración del mercado se centra en reforzar la relación e interacción de los clientes con el servicio a fin de aumentar el compromiso o engagement de las personas con el servicio prestado. % MPI = Clientes que accedieron al servicio / tamaño total de mercado para este servicio

+ <font color='##74A608'>**El Coste de Adquisición del Cliente o CAC:**</font> cuánto dinero has utilizado para capturar a nuevos clientes .CAC = (Marketing + Ventas) / Clientes Adquiridos ,

+ <font color='##74A608'> <strong>- tasa de retencion del cliente </strong>

Se trata de un porcentaje que mide cuántos clientes conserva una empresa al final de un plazo determinado, después de comparar la adquisición de nuevos clientes contra el número de clientes que se perdieron.

${Clientes\quad al \quad final \quad de \quad un \quad periodo - clientes \quad nuevos \quad adquiridos \quad durante \quad el \quad periodo \over clientes \quad al \quad comienzo \quad del \quad periodo}*100$


# <font color='#307A71'>**Stack Tecnológico - Pipeline**<a name="pipeline"></a></font>

Son diversas herramientas las cuales nos van a ayudar a cumplir nuestros objetivos a nivel Técnico y Profesional, a continuación se detallan de la mejor forma:

<img src="5. Sources/Images/logo_fabric.png" width="25px"/><font color='##74A608'>**Microsoft Fabric:**</font> Es un todo en uno de data, se integran todas las herramientas para ETL, EDA y DA.
Se propuso esta herramienta con el fin de adelantarnos a la tendencia, ya que se encuentra en fase Beta y pronto saldrá la versión Oficial, viniendo de Microsoft y la inversión que ha realizado los ultimos años en herramientas de data posicionandose en segundo lugar, tendremos la mejor experiencia en un entorno muy Profesional y nos ayudará para futuros proyectos en diferentes empresas.

<img src="5. Sources/Images/logo_jupyter.png" width="30px"/><font color='##74A608'>**NoteBooks:**</font> Trabajaremos con esta herramienta conectada a Python, SQL y Apache Spark
Data Factory: Esta herramienta nos ayuda a tener un flujo de datos entre areas y automatización de tareas, tambien es muy importante para la ingesta de datos en el Data WareHouse.

<img src="5. Sources/Images/logo_spark.jpeg" width="30px"/><font color='##74A608'>**Apache Spark:**</font> Hadoop y Spark nos ayuda para el procesamiento de grandes cantidades de datos en forma de nodos, paralelizando el trabajo y siendo más eficiente de acuerdo su configuración y el tipo de archivo que se use, lo podremos gestionar con Python o con SQL.

<img src="5. Sources/Images/logo_scikit.png" width="30px"/><font color='##74A608'>**Scikit Learn:**</font> Lo usaremos para crear nuestros modelos de ML, también con una herramienta "Experiment" la cual realizamos un seguimiento del desarrollo a los modelos de ML y validar las hipotesis.

<img src="5. Sources/Images/logo_powerbi.png" width="50px"/><font color='##74A608'>**Power Bi:**</font> Aprovecharemos esta herramienta para realizar, el analisis y la vizualización de datos creando un Dashboard muy profesional y en la web.

<img src="5. Sources/Images/logo_matplotlib.png" width="30px"/><font color='##74A608'>**MatPlotlib:**</font> Es indispensable para crear el mejor informe EDA para que nuestros clientes puedan acceder a él de la forma más legible e intuitivo, será necesario traer nuestros modelos de ML allí y exponerlos.

<img src="5. Sources/Images/logo_kusto.png" width="30px"/><font color='##74A608'>**Kusto (KQL):**</font> Muy posiblemente usaremos streaming de datos, no es algo seguro pero lo proponemos desde el inicio.

<img src="5. Sources/Images/logo_azure.png" width="30px"/><font color='##74A608'>**Microsoft Azure:**</font> Usaremos la nube de Microsoft para apoyarnos respecto a Bases de datos de SQL Server de ser necesarias, también para realizar el deploy de la aplicación para nuestros clientes a través de Fast API, usando Docker.

## **_♦ Pipeline_**

El diagrama de Pipeline se encuentra a continuación:

<img src="5. Sources/Images/pipeline.gif" width="900px"/>

[def]: #stack-tecnológico---pipeline
