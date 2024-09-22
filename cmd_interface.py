import argparse
from tts_flask_ml.main.tts_converter import TTSConverter

def main():
    parser = argparse.ArgumentParser(description="Text-to-Speech Converter")
    parser.add_argument("text_files", nargs="+", help="Input text files")
    parser.add_argument("-o", "--output_dir", default="output", help="Output directory")
    parser.add_argument("-f", "--audio_format", default=".mp3", help="Audio format (e.g., .mp3, .wav)")

    args = parser.parse_args()

    converter = TTSConverter()
    converter.set_audio_format(args.audio_format)

    for text_file in args.text_files:
        converter.convert_single(text_file, args.output_dir)

if __name__ == "__main__":
    main()