import uuid

print(str(uuid.uuid3(uuid.NAMESPACE_DNS,"bakricoder71@gmail.com")).split("-")[4])
