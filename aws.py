import boto3
from pprint import pprint


class AWS:

    def __init__(self):
        self.service_type = 'ec2'
        self.region = 'us-east-1'
        self.client = boto3.client(self.service_type, self.region)

    def get_regions(self):
        """Returns a list of Regions"""
        regions = []
        response = self.client.describe_regions()
        for region in response['Regions']:
            regions.append(region['RegionName'])

        return regions

    def get_vpcs(self, region):
        """Returns a list of VPCs in a Region"""
        vpcs = []
        self.region = region
        response = self.client.describe_vpcs()
        for vpc in response['Vpcs']:
            vpcs.append(vpc['VpcId'])

        return vpcs


if __name__ == "__main__":
    aws = AWS()
    pprint(aws.get_regions())
    pprint(aws.get_vpcs('us-east-1'))
