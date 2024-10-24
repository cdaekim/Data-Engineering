# League of Legends End-to-End Data Engineering and Data Science Project

## Project Overview
In this project, I led a team in designing and implementing an end-to-end data science project for CSE6242 at Georgia Tech. The project followed these key stages:

1. **Data Ingestion**: Developed Python scripts to ingest raw data from the Riot Games REST API, managing API calls, authentication, and retrieving data in JSON format.
2. **Transformation and Loading**: Transformed the extracted data into structured CSV format using Python, ensuring data consistency and usability for analysis. The data was then hosted on Google Drive for accessibility.
3. **Data Analysis**: Implemented apriori association rule learning (market basket analysis) and community detection. The market basket analysis was hand-coded without using external libraries.
4. **Data Visualization**: Built an interactive data visualization tool using D3.js to display analytical insights.

As the **project manager** and **team lead** of a six-person group, I directed the project vision, scope, and task allocation while ensuring that the project reinforced course objectives. The project was designed to be self-contained, aligning with class content, so all team members could contribute confidently. I specifically handled coding the data transformation and analysis parts of the pipeline. The focus was on creating an end-to-end solution data science pipeline, including data wrangling, custom algorithm implementation, and visualization.

## Table of Content

- [Dataset Used](#dataset-used)
- [Technologies](technologies)
- [Data Pipeline Architecture](#data-pipeline-architecture)
- [Date Modeling](#data-modeling)
- [Step 1: ETL](#step-1-etl)
- [Step 2: Storage](#step-2-storage)
- [Step 3: Analytics](#step-3-analytics)
- [Step 4: Visualization](#step-4-visualization)

## Dataset Used

This project uses the [Canisback Matchlist](https://canisback.com/matchId/) dataset, which contains match IDs from all available regions, serving as identifiers for querying data from the Riot Games API. We extracted player IDs, corresponding match IDs, and match data from this dataset, which were used for our analysis.

For more information on the Riot Games API, visit the documentation for the League of Legends endpoint:
- Website: https://developer.riotgames.com/docs/lol

## Technologies

The following technologies are used to build this project:
- Language: Python, JavaScript
- Packages: request, http.client, Pandas, NumPy, NetworkX
- Extraction and transformation: Jupyter Notebook
- Storage: Google Drive
- Visualization: [D3.js](https://d3js.org/)
## Data Pipeline Architecture

![screenshot](https://private-user-images.githubusercontent.com/50489425/379817576-6d818706-be21-447b-bfc5-9b020a6a588d.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mjk3ODEwMzksIm5iZiI6MTcyOTc4MDczOSwicGF0aCI6Ii81MDQ4OTQyNS8zNzk4MTc1NzYtNmQ4MTg3MDYtYmUyMS00NDdiLWJmYzUtOWIwMjBhNmE1ODhkLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDEwMjQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMDI0VDE0Mzg1OVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWI5MjY5MDM2OTU0MjcwMTAwNTFmMWUwMjQ3MmExOTM4NTk1MDIwZDBjMzVmNTNkNGQ2YWFiMzcxMzU2MGMwNTgmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.PL-C5FH5ySYEKyX4ulVlJsRXLYJHv0ytq52tM4Z2Iyo)
