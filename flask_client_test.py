from flask_ml.flask_ml_client import MLClient
from flask_ml.flask_ml_server.constants import DataTypes

url = "http://127.0.0.1:5000/tts_converter"  # The URL of the server
client = MLClient(url)  # Create an instance of the MLClient object

## Update inputs before testing
inputs = [
    {"input": "./tts_flask_ml/test/words_100.txt"},
    {"input": "./tts_flask_ml/test/words_9999.txt"},
]  # The inputs to be sent to the server
data_type = DataTypes.CUSTOM  # The type of the input data
parameters = {"output_dir": "./outputs"}

response = client.request(inputs, data_type, parameters)  # Send a request to the server
print(response)  # Print the response

# Excepcted response
# [{'result': 'words_100.aiff', 'file_path': '../TTS-Flask-ML/words_100.aiff'},
# {'result': 'words_9999.aiff', 'file_path': '../TTS-Flask-ML/words_9999.aiff'}]
