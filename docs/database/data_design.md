#Database Design
This document defines the database structure for the renewable Energy Prediction system Project.

##1.Users
Stores user Account info.

**Primary Key:**User_id
**Important Columns**
-User_Id
-Name
-email
-password
-created_at


##2.Project
stores Project details created by the user.

**Primary Key:**Project_Id
**Important Columns**
-project_ID
-user_ID
-project_name
-location
-created_at


##3.Sites
stores location details for Analysis

**Primary Key:**Site_Id
**Important Columns**
-site_Id
-project_Id
-latitude
-Longitude
-State
-elevation


##4.EnvironmentalData
Stores raw enviromental data for each site

**Primary Key:**env_Id
**Important columns**
-env_id
-site_Id
-solar_irradiance
-wind_speed
-temperature
-humidity


##5.SolarPrediction
stores solar energy predictions.

**Primary key:**solar_pred_Id
**Important columns**
-solar_pred_Id
-site_id
-predicated_power
-efficiency
-prediction_date


##6.WindPrediction
stores wind energy predictions.

**Pimary key:**wind_pred_Id
**important columns**
-wind_pred_Id
-site_Id
-predicated_power
-wind_speed
-prediction_date


##7.SuitabilityScore
stores final suitability score for renewable energy installation

**primary key:**score_Id
**important columns**
-score_Id
-site_Id
-solar_score
-wind_score
-overall_score
-recommendation


##8.Reports
store generated analysis reports

**primary key:**report_Id
**Important columns**
-report_id
-project_id
-report_type
-report_data
-generated_at
-file_path