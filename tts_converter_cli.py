import argparse

from tts_flask_ml.main.tts_converter import TTSConverter


def main():
    parser = argparse.ArgumentParser(description="Text-to-Speech Converter")
    parser.add_argument(
        "-t", "--text_files", nargs="+", default=None, help="Input text files"
    )
    parser.add_argument("-i", "--input_dir", default=None, help="Input directory")
    parser.add_argument("-o", "--output_dir", default=None, help="Output directory")
    parser.add_argument("-f", "--audio_format", default=None, help="Audio format")

    args = parser.parse_args()

    if args.text_files is None and args.input_dir is None:
        raise ValueError(
            "Input must be either path to text file(s) or directory with text files"
        )

    converter = TTSConverter()
    if args.audio_format is not None:
        converter.set_audio_format(args.audio_format)

    print(args)
    if args.text_files is None:
        print(f"result: {converter.convert_from_dir(args.input_dir, args.output_dir)}")
    else:
        print(f"result: {converter.convert_batch(args.text_files, args.output_dir)}")


if __name__ == "__main__":
    main()
