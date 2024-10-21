from embodiedcity import DroneClient, ImageType, CameraID

base_url = "https://embodied-ai.city"
drone_id = "0"
token = "22f48a0a-8984-4472-ae2e-b5bf4f00744d"
client = DroneClient(base_url, drone_id, token)

client.move_back_forth(10)
image = client.get_image(ImageType.Scene, CameraID.FrontCenter)
print(image.shape)