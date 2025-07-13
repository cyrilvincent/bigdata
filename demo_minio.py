from minio import Minio
from minio.error import S3Error

# Configuration du client MinIO
client = Minio(
    "localhost:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)

bucket_name = "house"
if client.bucket_exists(bucket_name):
    print(f"Contenu du bucket '{bucket_name}':")
    for obj in client.list_objects(bucket_name, recursive=True):
        print(f"- {obj.object_name} ({obj.size} octets)")
    else:
        print(f"Le bucket '{bucket_name}' n'existe pas.")

with client.get_object(bucket_name, "house.csv") as response:
    content = response.read().decode("utf-8")
    print(content)
