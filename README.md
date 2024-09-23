# TTS-Flask-ML
Converts text files to mp3 audio speech files. Uses pyttsx3 and wrapped by flask-ml.

**To install pipenv**

```pip install pipenv```

**To create your own virtual environment**

```pipenv shell```

### Installing requirements

**To install using pipenv**

```pipenv install```

**To install from .txt**

*For windows*

``` pip install -r requirements-win.txt``` 

*For Mac*

``` pip install -r requirements-mac.txt``` 

**Starting server**

starting flask server

```python -m tts_flask_ml.server.server```

**Client example**

update the inputs on the file before running

```python -m flask_client_test```

### Command line Interface

**For input directory path**

```python tts_converter_cli.py -i "demo"```

*or*

```python tts_converter_cli.py --input_dir "demo"```

**For input files path**

```python tts_converter_cli.py -t "demo/words_1000.txt demo/text.txt"```

*or*

```python tts_converter_cli.py --text_files "demo/words_1000.txt demo/text.txt"```

**For output directory path (Optional)**

```python tts_converter_cli.py -o "demo/out"``` 

*or*

```python tts_converter_cli.py --output_dir "demo/out"``` 




