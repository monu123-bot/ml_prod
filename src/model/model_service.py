from pathlib import Path
import pickle as pk
from model.pipeline.model import build_model
from config.config import session
from loguru import logger


class ModelService:

    def __init__(self):
        self.model = None

    def load_model(self):
        logger.info(
            f"checking the existance of model config file at {session.model_path}/{session.model_name}"
        )

        model_path = Path(f"{session.model_path}/{session.model_name}")

        if not model_path.exists():
            logger.warning(f"model at {session.model_path}/{session.model_name}")
            build_model()
        logger.info(f"model {session.model_name} exists! -> loading model configuration file")
        self.model = pk.load(open(f"{session.model_path}/{session.model_name}", "rb"))

    def predict(self, input_param):
        logger.info(f"making prediction!")
        return self.model.predict([input_param])
