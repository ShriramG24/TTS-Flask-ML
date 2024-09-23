# TTS-Flask-ML
Converts text files to mp3 audio speech files. Uses pyttsx3 and wrapped by flask-ml.

## Installation Requirements
### To install pipenv

```pip install pipenv```
### To create your own virtual environment
```pipenv shell```

### To install the required dependencies, run the following `pip` command:

```pipenv install```
###To install dependencies via text files

#### For windows

``` pip install -r requirements-win.txt```
#### For Mac
``` pip install -r requirements-mac.txt```

## Starting the server
```python -m tts_flask_ml.server.server```

## Client example
```python -m tts_converter_cli```

## Command line tool

### For input directory path
```python ./tts_converter_cli.py "./demo"```
### For input file paths
```python ./tts_converter_cli.py "./demo/words_100.txt"```



