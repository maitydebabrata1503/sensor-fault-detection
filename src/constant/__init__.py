import os


AWS_S3_BUCKET_NAME = "wafer-fault"
MONGO_DATABASE_NAME = "sensor_fault_data"
MONGO_COLLECTION_NAME = "waferfault"


TARGET_COLUMN = "quality"
MONGO_DB_URL = "mongodb+srv://sensor_fault_data:sfd@cluster0.9pqr0ny.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


MODEL_FILE_NAME = "model"
MODEL_FILE_EXTENSION = ".pkl"

artifact_folder = "artifacts"