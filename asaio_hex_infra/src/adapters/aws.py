import boto3


class AWSSession:
    def __init__(self, credentials:dict = {}, profile_name: str = "", region_name: str = ""):
        if region_name is None:
            region_name = boto3.Session().region_name
        if not credentials and not profile_name:
            print("No credentials or profile name provided, using default AWS session.")
        self.session = boto3.Session(region_name=region_name)

    def get_client(self, service_name: str):
        return self.session.client(service_name, region_name="sa-east-1")

    def get_resource(self, service_name: str):
        return self.session.resource(service_name)