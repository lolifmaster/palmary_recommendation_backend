import pandas as pd
import numpy as np
import tensorflow as tf

products_encoded = pd.read_csv(r"C:\Users\chare\PycharmProjects\palmary_recommendation\static\products_encoded.csv")
index = pd.read_csv(r"C:\Users\chare\PycharmProjects\palmary_recommendation\static\products_new.csv")
# Load the model from the file
model = tf.keras.models.load_model(r"C:\Users\chare\PycharmProjects\palmary_recommendation\static\my_model.h5")


# Use the loaded model for inference
def predict(p1, p2, p3):
    data = {
        'Column1': [p1],
        'Column2': [p2],
        'Column3': [p3]
    }
    data = pd.DataFrame(data)
    # Define different combinations of features and targets
    x1 = data.iloc[:, [0, 1]].to_numpy()

    x2 = data.iloc[:, [0, 2]].to_numpy()

    x3 = data.iloc[:, [1, 2]].to_numpy()

    x4 = data.iloc[:, [1, 0]].to_numpy()

    x5 = data.iloc[:, [2, 0]].to_numpy()

    x6 = data.iloc[:, [2, 1]].to_numpy()

    # Concatenate the feature sets vertically using NumPy
    x = np.vstack([x1, x2, x3, x4, x5, x6])
    # Convert x and y back to DataFrames
    x_df = pd.DataFrame(x, columns=["Feature1", "Feature2"])
    # Merge dataset1 with products based on 'product_1_id'
    x_df_marged = x_df.merge(products_encoded, left_on='Feature1', right_on='id', how='left',
                             suffixes=('', '_feature1'))

    # Drop the 'id' column as it's no longer needed
    x_df_marged = x_df_marged.drop(columns=['id'])

    # Repeat the same process for 'product_2_id'
    x_df_marged = x_df_marged.merge(products_encoded,
                                    left_on='Feature2', right_on='id', how='left',
                                    suffixes=('', '_feature2'))

    # Drop the 'id' column as it's no longer needed
    x_df_marged = x_df_marged.drop(columns=['id', 'Feature1', 'Feature2'])

    # Make predictions using the model
    predictions = model.predict(x_df_marged)

    # Find the indices of the top 11 classes with the highest probability for each prediction
    top11_indices = np.argsort(predictions, axis=1)[:, -11:][:, ::-1]
    predicted_indices = top11_indices.transpose().flatten()

    predicted_indices = np.unique(predicted_indices)
    predicted_indices = predicted_indices[predicted_indices != p1]
    predicted_indices = predicted_indices[predicted_indices != p2]
    predicted_indices = predicted_indices[predicted_indices != p3]

    # Map the predicted indices to product names using the product mapping DataFrame
    predicted_product_names = index.loc[predicted_indices, 'real_name'].values
    predicted_product_image = index.loc[predicted_indices, 'image'].values

    # Create a new DataFrame with the predicted product names
    predicted_df = pd.DataFrame({
        'id': predicted_indices,
        'name': predicted_product_names,
        'image': predicted_product_image})

    return predicted_df[:8]
