# Philadelphia Crime and Heat: “Heat on Aggression”

# Overview

- __PROJECT TEAM:__ Joseph Trybala, Miko Wieczorek, Max Song
- __DATE CREATED:__ 2023-03-16

## Crime Data

Crime data is stored in one .csv file `analysis_df.csv` that is organized chronologically. Each row corresponds to a singular dispatch from a law enforcement dispatcher. Details include time, general crime type determined at time of call, which dispatch center is responding, and approximated locational data (latitude and longitude).

The chronological limits of our data are 2006-2022. The start date was chosen due to the completeness of data available.

## Weather Data

WEather data is stored in one .csv file ‘PFI Weather Data.csv’ that documents the daily summaries of weather data from the Franklin Institute's Weather Data Collection Point, the data is organized chronologically. Details are regarding Precipitation, Temperature Max, and Temperature Min. 

The chronological limits of our data are from 2006 to 2022.

## Access Rights and Distributions Approach

We have acquired, pre-processed, and deployed our final datasets from two publicly available sources of data, as elucidated earlier.

Philadelphia Crime Data is freely available through the OpenDataPhilly Project, on the website https://www.opendataphilly.org/dataset/crime-incidents, it is provided by the Philadelphia Police Department through the Pennsylvania Police Uniform Crime Reporting system (https://www.ucr.pa.gov/PAUCRSPUBLIC/Home/Index).
Weather data has been freely available to the public through multiple avenues including through the NOAA web portal which is where we obtained our cleaned datasets.

Our analysis and combined dataset is released publicly under a Creative Commons 4.0 Attribution (CC BY 4.0) license, on Github titled [Philly Crime and Heat](https://github.com/bluemaw/philly-crime-and-heat) for use by any interested parties.

# About Project Directory

The following summarizes contents of the project directory:

## data (Types of Data)

### rawdata

-	analysis_df.csv - Stitched together data from the 17 ‘crime_incidents’ .csv files as well as the ‘PFI Weather Data.csv’ file. Columns include time of dispatch, general crime code, locational data, and the relevant daily weather summary data.
-	crime_incidents_2006.csv - Crime Incidents data from the UCR project authored by the Philadelphia Police Department of the year 2006.
-	crime_incidents_2007.csv - “ “
-	crime_incidents_2008.csv - “ “
-	crime_incidents_2009.csv - “ “
-	crime_incidents_2010.csv - “ “
-	crime_incidents_2011.csv - “ “
-	crime_incidents_2012.csv - “ “
-	crime_incidents_2013.csv - “ “   
-	crime_incidents_2014.csv - “ “  
-	crime_incidents_2015.csv - “ “
-	crime_incidents_2016.csv - “ “  
-	crime_incidents_2017.csv - “ “  
-	crime_incidents_2018.csv - “ “  
-	crime_incidents_2019.csv - “ “ 
-	crime_incidents_2020.csv - “ “   
-	crime_incidents_2021.csv - “ “
-	crime_incidents_2022.csv - “ “
-	'PFI 2006-2007.csv’ - Weather data from the Franklin Institute NOAA Weather Data Collection Point of the years 2006 and 2007.
-	'PFI 2007-2010.csv' - “ “
-	'PFI 2010-2013.csv' - “ “
-	'PFI 2013-2016.csv' - “ “
-	'PFI 2016-2019.csv' - “ “
-	'PFI 2019-2023.csv' - “ “

### processed

-	analysis_df.csv - Stitched together data from the 17 ‘crime_incidents’ .csv files as well as the ‘PFI Weather Data.csv’ file. Columns include time of dispatch, general crime code, locational data, and the relevant daily weather summary data.
-	PFI Weather Data.csv - Stitched together data from the 6 ‘PFI’ .csv files.
-	Crime_types.csv - Custom Categorization data based on both FBI Violent Crimes reports and Pennsylvania General Assembly Guidelines.
-	daily_aggregated_df.csv - A aggregated form of ‘analysis_df.csv’ utilizing daily counts instead of by-dispatch data points.
-	dictionary_analysis_df.csv - Data dictionary that explains the details of analysis_df.csv
-	dictionary_daily_aggregated_df.csv - Data dictionary that explains the details of daily_aggregated_df.csv.

## python

- `data_processing.py`: Python script with custom data pre-processing and cleaning functions
- `modeling.py`: Python script with helper modeling functions
- `plots.py`: Python script with helper plotting functions

## virtualenv

We used virtualenv to isolate Python dependencies. The `requirements.txt` lists all Python packages used in order to reproduce our results. After repo is cloned, run the following to restore the requirements into your local project space:

- `virutalenv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`

## presentation

Our presentation with more details on this project can be found here: **`Phase 2 Presentation - Philly Crime and Heat: “Heat on Aggression”.pptx`**.
Additional visualizations can be found on [Tableau Public](https://public.tableau.com/views/HeatonAggressionPhiladelphiaSpecial/HeatonAggressionTakeaways?:language=en-US&:display_count=n&:origin=viz_share_link)

### figures

This is the destination directory for presentation-ready figures written from 04- Jupyter Notebooks.

## images

This folder contains images used in EDA output from the Tableau story (link provided above).

## references
This folder contains pdfs of various documents that have been referenced in our reporting.

# Running Code

Jupyter notebook files are used as orchestrators to manage data retrieval, processing, cleaning, writing, modeling, and generating plots. Make sure that your current working directory is the project root. 

-	01-weather_stiching.ipynb: takes in raw weather data files, merges and outputs cleaned dataset to data/processed/PFI\Weather\Data/csv
-	02-EDA.ipynb: this is our main EDA where we clean and merge crime data files and add in the temperature data (we use helper module python/data_processing.py). Final datasets are outputted to data/processed/daily_aggregated_df.csv and data/processed/analysis_df.csv
-	03-glmnb.ipynb: in this notebook, we are fitting negative binomial models for our 3 outcomes, using the processed daily_aggregated_df.csv file (we use python/modeling.py helper module)
-	04-presentation_plots1.ipynb: this notebook creates presentation-ready visualizations (uses python/plots.py helper module)
-	04-presentation_plots2.ipynb: this notebook creates presentation-ready visualizations 
-	05-other_exploratory_plots.ipynb: this notebook explored more visualizations and trends post-EDA in our preparation for the presentation



# GitHub Repo

Please click link to our GitHub Repository titled [Philly Crime and Heat](https://github.com/bluemaw/philly-crime-and-heat).

# Limitations

Crime Data Limitations

A heavy limitation regarding the crime data we have is already inherent in the data we are using. This data is specifically crime incident-reporting data. From our perspective, there are three major limitations from this:
-	A crime has to be noticed to be reported, not all crimes are reported as some are considered "victimless" crimes. For these crimes, there would be no reporter. Hence, our data would not include it.
-	Time of incident-report. A crime is reported when it is noticed. For this reason the likelihood of late night crimes being under-reported is high. Two example scenarios would be: a burglary of a business or a theft from a vehicle. Those crimes would likely be reported in the morning when they are noticed, but the crime itself would have been committed the night prior.
-	Crime reporting rate versus actual crime rate. Our crime data does not include conviction data. A crime may be reported that did not occur; just as conversely, a crime may occur that does not get reported. There are likely many cases where we will encounter a crime report (data-point) and it does not accurately represent that incident.
Temperature Data Limitations
-	Not accurate enough. Firstly, more granular temperature data could be added. In addition, we are only utilizing the highs and lows of the day; weather data is more nuanced than two data points, hourly or more accurate temperatures could lead to more specific inferences--stronger correlations.
-	Single source of info. We are only investigating the crime data with regards to the temperature localized on a single weather station. The temperature should be used as a reference and not as an exact indicator of the temperature at the time of the dispatch.
-	Single point of failure. By only using one weather station's reported temperature data, this approach could lead to holes in our data. For example, certain days in which the station did not report the weather, for various reasons, our dataset had no results (missing values) for certain days

Human Bias
-	A crime is reported when it is noticed. For this reason the likelihood of late night crimes being underreported is high.  



