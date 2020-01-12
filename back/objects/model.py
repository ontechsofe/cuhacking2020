from google.cloud import automl

class Model(object):
    def __init__(self, MODEL_CONFIG):
        self.project_id = MODEL_CONFIG['project_id']
        self.model_id = MODEL_CONFIG['model_id']
        self.client = automl.PredictionServiceClient()        
    
    def predict(self, text):
        try:
            prediction_client = automl.PredictionServiceClient()  
            model_full_id = prediction_client.model_path(
                self.project_id, 'us-central1', self.model_id
            )

            text_snippet = automl.types.TextSnippet(
                content=text,
                mime_type='text/plain')  # Types: 'text/plain', 'text/html'
            payload = automl.types.ExamplePayload(text_snippet=text_snippet)

            response = prediction_client.predict(model_full_id, payload)
            return response.payload
        except Exception as error:
            print(error)
