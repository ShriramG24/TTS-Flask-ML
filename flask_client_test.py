from flask_ml.flask_ml_client import MLClient
from flask_ml.flask_ml_server.constants import DataTypes

url = "http://127.0.0.1:5000/tts_converter"  # The URL of the server
client = MLClient(url)  # Create an instance of the MLClient object

inputs = [
    {"input": "/Users/sahithisingireddy/Downloads/test_dir/text.txt"},
    {"input": "/Users/sahithisingireddy/Downloads/test_dir/text2.txt"}
]  # The inputs to be sent to the server
data_type = DataTypes.CUSTOM  # The type of the input data
parameters = {
    "output_dir": "/Users/sahithisingireddy/Downloads/test_dir/outputs"
}

response = client.request(inputs, data_type, parameters)  # Send a request to the server
print(response)  # Print the response

#Excepcted response
# [{'result': 'words_100.aiff', 'file_path': '/Users/sahithisingireddy/coding/596E/Mini_Project/TTS-Flask-ML/words_100.aiff'}, 
# {'result': 'words_9999.aiff', 'file_path': '/Users/sahithisingireddy/coding/596E/Mini_Project/TTS-Flask-ML/words_9999.aiff'}]