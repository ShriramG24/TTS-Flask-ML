from tts_flask_ml.main.tts_converter import TTSConverter

test_tts = TTSConverter()

result = test_tts.convert_from_dir("/Users/sahithisingireddy/Downloads/test_dir", "/Users/sahithisingireddy/Downloads/test_dir/outputs")
print(f"resulu = {result}")