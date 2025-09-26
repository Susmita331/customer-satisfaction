import logging 
from zenml.pipelines import pipeline

@pipeline(enable_cache=False)
def train_pipeline(ingest_data, clean_data, model_train, evaluation):
    data = ingest_data()
    cleaned_data = clean_data(data)
    model = model_train(cleaned_data)
    results = evaluation(model, cleaned_data)
