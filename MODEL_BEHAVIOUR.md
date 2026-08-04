# Model Behaviour Documentation

## 1. Selected Model

The prediction engine uses a Random Forest Regressor to estimate renewable energy output. The model was selected because it achieved the best overall performance during evaluation and can provide feature importance scores for explainability.


## 2. Evaluation Metrics

The trained Random Forest Regressor achieved the following evaluation results:

- Mean Absolute Error (MAE): 0.1707
- Root Mean Squared Error (RMSE): 9.3771
- R² Score: 0.9822

These results indicate that the model provides highly accurate predictions for the prepared training dataset.


## 3. Most Influential Features

Based on the Random Forest feature importance analysis, the most influential features are:

1. Solar Irradiance (ALLSKY_SFC_SW_DWN) – 0.482404
2. Wind Speed (wind_speed) – 0.270685
3. Power Density (power_density) – 0.217603

These features contribute the most to the model's renewable energy prediction, while features such as elevation, road count, and average pixel value have little or no influence on the current model.



## 4. Limitations and Assumptions

### Limitations
- The model is trained using the currently available datasets and may not generalize to all geographical locations.
- Some input features, such as mean elevation, total roads, and average pixel value, showed little or no contribution in the current model.
- The prediction accuracy depends on the quality and completeness of the input data.

### Assumptions
- The input features are provided in the same format and order used during model training.
- The training data accurately represents the renewable energy conditions for the selected locations.
- The Random Forest model remains valid unless the training data or feature engineering pipeline changes.