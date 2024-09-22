from ..main.tts import TTSConverter
import os

input_dir = os.getcwd()
print("Input Directory: {input_dir}")

tts = TTSConverter()

res = tts.convert_from_dir(input_dir)

print("Results: {res}")