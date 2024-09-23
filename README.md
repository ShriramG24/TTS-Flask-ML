# TTS-Flask-ML
Converts text files to audio speech files. Uses pyttsx3 and wrapped by flask-ml.

## Setup
**1. Install pipenv and start virtual env**
```
pip install pipenv
```
```
pipenv shell
```
**2. Install dependencies**

via pipenv
```
pipenv install
```
or

via requirements.txt

*for windows*
``` 
pip install -r requirements-win.txt
``` 
*for mac*
``` 
pip install -r requirements-mac.txt
``` 

## Flask-ML
**Starting server**
```
python -m tts_flask_ml.server.server
```
**Client example**

*update the inputs on the file before running*
```
python -m flask_client_test
```

## Command line Interface

**Convert one or more files**
```
python tts_converter_cli.py --text_files ./text_1.txt ./text_2.txt
```
```
python tts_converter_cli.py -t ./text_1.txt
```

**Convert all text files in a directory**
```
python tts_converter_cli.py --input_dir ./inputs
```
```
python tts_converter_cli.py -i ./inputs
```
> the input file names are continued for outputs and are stored in the same directory unless a output directory is specified like below
</br>

**Optional - Specify output directory/audio format**
```
python tts_converter_cli.py --input_dir ./inputs --output_dir ./out --audio_format wav
```
```
python tts_converter_cli.py -t ./text_1.txt -o ./out -f wav
```
> do not use mp3 format on macOS, default on mac is aiff and default on other systems is mp3




