import pytest
from tts_flask_ml.main.tts import TTSConverter
import os

def test_convert_single_valid_input():
    converter = TTSConverter()
    text_file = "test/words_100.txt"
    out_dir = "output"
    result = converter.convert_single(text_file, out_dir)
    assert os.path.exists(result)

def test_convert_single_invalid_input_file_not_found():
    converter = TTSConverter()
    text_file = "nonexistent_file.txt"
    out_dir = "output"
    with pytest.raises(ValueError):
        converter.convert_single(text_file, out_dir)

def test_convert_single_invalid_input_empty_file():
    converter = TTSConverter()
    text_file = "test/empty_file.txt"
    out_dir = "output"
    with pytest.raises(ValueError):
        converter.convert_single(text_file, out_dir)

def test_convert_batch_valid_input():
    converter = TTSConverter()
    text_files = ["test/words_100.txt", "test/words_9999.txt"]
    out_dir = "output"
    results = converter.convert_batch(text_files, out_dir)
    assert len(results) == 2
    for result in results:
        assert os.path.exists(result)

def test_convert_batch_invalid_input_empty_list():
    converter = TTSConverter()
    text_files = []
    out_dir = "output"
    with pytest.raises(ValueError):
        converter.convert_batch(text_files, out_dir)

def test_convert_from_dir_valid_input():
    converter = TTSConverter()
    input_dir = "test"
    out_dir = "output"
    results = converter.convert_from_dir(input_dir, out_dir)
    assert len(results) >= 2  # Ensure at least two files are converted
    for result in results:
        assert os.path.exists(result)

def test_convert_from_dir_invalid_input_directory_not_found():
    converter = TTSConverter()
    input_dir = "nonexistent_dir"
    out_dir = "output"
    with pytest.raises(ValueError):
        converter.convert_from_dir(input_dir, out_dir)
