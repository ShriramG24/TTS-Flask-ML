from tts_flask_ml.main.tts import TTSConverter
import os

input_dir = os.getcwd() + "\\tts_flask_ml\\test"
print(f"Input Directory: {input_dir}")

tts = TTSConverter()

res = tts.convert_from_dir(input_dir)

print(f"Results: {res}")
