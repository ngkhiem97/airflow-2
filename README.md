# airflow-2

The following git stores the related information after performing the Principal Component Analysis on given CFD Results dataset. The related information includes:

1. Data: Original and preprocessed dataset.
2. Figures: Visualization graph extracted from the Python notebooks.
3. Notebooks: Python notebooks.
4. Reports: Resulting data (trained models, eigenvalues, conclusions).

## Details:

### 1. data

- data/CFD_Results: holds the original dataset with its definition in file *definitions_of_CFD_inputs_and_outputs.docx*
- data/preprocessed: The original dataset in *data/CFD_Results* is splitted to multiple files for the same room. For example, in conference_room folder, the training data is splitted to three files (training_MRT.csv, training_T.csv, training_T.csv). These file has the same first 13 columns with the diffences are only in the MRT, T and V columns. For this reason, data is preprocessed, combined and stored in this folder.

### 2. figures

- heatmap_...: correlation heatmaps of each room data.
- hist_...: distribution of dataset's features.
- hist_pca_...: distribution of dataset's features after performing PCA.
- evr_...: explained variance ratio of the PCA.

### 3. notebooks

- preprocessing.ipynb: notebook holds Python code for preprocessing the original data in *data/CFD_Results* to the preprocessed data in *data/preprocessed*.
- eda.ipynb: Exploratory Data Analysis with visualization of preprocessed data.
- pca_...: perform PCA and evaluate its affect on Machine Learning models.

### 4. reports

- data: eigenvectors and training times from PCA and its evaluation.
- models: trained model used in evaluation. Pickle is used to store the Linear Regression models. For the Neural Network models, they just used the save function from Keras.
- pca_...: pdf file generated from Python notebooks.
- Conclusion.odt and Conclusion.pdf: conlusion from the notebooks and data.
