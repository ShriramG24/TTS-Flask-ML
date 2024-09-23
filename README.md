# TTS-Flask-ML
Converts text files to mp3 audio speech files. Uses pyttsx3 and wrapped by flask-ml.

#### To install pipenv
```pip install pipenv```
#### To create virtual environment
```pipenv shell```

### Installing requirements

#### To install using pipenv 
```pipenv install```

#### To install from .txt
##### For windows 

``` pip install -r requirements-win.txt``` 
##### For Mac

``` pip install -r requirements-mac.txt``` 

### Starting the server
```python -m tts_flask_ml.server.server```

### Client example
##### update the inputs on the file before running
```python -m flask_client_test```

### Command line Interface

#### For input directory path
```python ./tts_converter_cli.py -i directorypath```
##### Or
```python ./tts_converter_cli.py --input_dir directorypath```

#### For input files path
```python ./tts_converter_cli.py -t filepath_1 filepath_2```
##### Or
```python ./tts_converter_cli.py --text_files filepath_1 filepath_2```

#### For output directory path (not mandatory)
```python ./tts_converter_cli.py -o output_directorypath``` 
##### or 
```python ./tts_converter_cli.py --output_dir output_directorypath``` 




