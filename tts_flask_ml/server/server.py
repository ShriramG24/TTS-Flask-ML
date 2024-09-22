import os

from flask_ml.flask_ml_server import MLServer
from flask_ml.flask_ml_server.constants import DataTypes
from flask_ml.flask_ml_server.models import (AudioResult, Response,
                                             ResponseModel)
from tts_flask_ml.main.tts_converter import TTSConverter

tts = TTSConverter()
server = MLServer(__name__)


@server.route("/tts_converter", input_type=DataTypes.CUSTOM)
def tts_converter(inputs: list[dict], parameters: dict) -> Response:
    print("Inputs:", inputs)
    print("Parameters:", parameters)

    files = [e.input for e in inputs]
    out_dir = None

    if "output_dir" in parameters:
        out_dir = parameters["output_dir"]

    if "audio_format" in parameters:
        tts.set_audio_format(parameters["audio_format"])

    res = [
        AudioResult(file_path=r, result=os.path.basename(r))
        for r in tts.convert_batch(files, out_dir)
    ]
    return ResponseModel(results=res).get_response()


server.run()
