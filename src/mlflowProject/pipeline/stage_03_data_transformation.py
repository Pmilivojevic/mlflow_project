from mlflowProject.config.configuration import ConfigurationManager
from mlflowProject.components.data_transformation import DataTransformation

from pathlib import Path
# from mlflowProject import logger


# STAGE_NAME = "Data Transformation"

class DataTransformationTrainingPipeline:
    def __init__(self):
        self.config = ConfigurationManager()
        self.data_validation_config = self.config.get_data_validation_config()
    
    def main(self):
        try:
            with open(Path(self.data_validation_config.STATUS_FILE), 'r') as f:
                status = f.read().split(" ")[-1]
                
            if status:
                data_transformation_config = self.config.get_data_tranformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()
            else:
                raise Exception("Your data schema is not valid")
        
        except Exception as e:
            print(e)


# if __name__ == "__main__":
#     try:
#         logger.info(f">>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<<")
#         obj = DataTransformationTrainingPipeline()
#         obj.main()
#         logger.info(f">>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<")
    
#     except Exception as e:
#         logger.exception(e)
#         raise e
    