from mlflowProject.config.configuration import ConfigurationManager
from mlflowProject.components.model_evaluation import ModelEvaluation
# from mlflowProject import logger


# STAGE_NAME = "Model Evaluation"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()


# if __name__ == "__main__":
#     try:
#         logger.info(f">>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<")
#         obj = ModelEvaluationTrainingPipeline()
#         obj.main()
#         logger.info(f">>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<")
    
#     except Exception as e:
#         logger.exception(e)
#         raise e
    