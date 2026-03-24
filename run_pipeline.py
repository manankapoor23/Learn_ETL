from networksecurity.pipeline.training_pipeline import TrainingPipeline

if __name__ == "__main__":
    pipeline = TrainingPipeline()
    artifact = pipeline.start_data_ingestion()
    print(f"Data Ingestion Complete!")
    print(f"Training file: {artifact.trained_file_path}")
    print(f"Testing file: {artifact.test_file_path}")
