import boto3
from pprint import pprint


class GetRegions:
    """Returns a list of Regions"""
    def __init__(self):
        self.service_type = 'ec2'
        self.default_region = 'us-east-1'
        self.ec2_region_client = boto3.client(self.service_type, self.default_region)

    def get_regions(self):
        regions = []
        response = self.ec2_region_client.describe_regions()
        for region in response['Regions']:
            regions.append(region['RegionName'])

        return regions


if __name__ == "__main__":
    aws = GetRegions()
    pprint(aws.get_regions())
