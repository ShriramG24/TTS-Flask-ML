import os

from flask_ml.flask_ml_server import MLServer
from flask_ml.flask_ml_server.constants import DataTypes
from flask_ml.flask_ml_server.models import (AudioResult, Response,
                                             ResponseModel)
from tts_flask_ml.main.tts_converter import TTSConverter

tts = TTSConverter()
server = MLServer(__name__)


@server.route("/tts/convert", input_type=DataTypes.CUSTOM)
def transcribe(inputs: list[dict], parameters: dict) -> Response:
    print("Inputs:", inputs)
    print("Parameters:", parameters)

    files = [e["file_path"] for e in inputs]
    out_dir = parameters["output_directory"]
    require_mp3 = parameters["require_mp3"]

    if require_mp3 is not None and require_mp3 == True:
        tts.set_audio_format(".mp3")

    res = [
        AudioResult(file_path=r, result=os.path.basename(r))
        for r in tts.convert_batch(files, out_dir)
    ]
    return ResponseModel(results=res).get_response()


server.run()
