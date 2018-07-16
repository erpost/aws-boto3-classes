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
        self.client = boto3.client(self.service_type, self.region)
        response = self.client.describe_vpcs()
        for vpc in response['Vpcs']:
            vpcs.append(vpc['VpcId'])

        return vpcs

    def get_all_vpcs(self):
        """Returns a dictionary of VPCs in all Regions"""
        vpc_by_region = {}
        for region in self.get_regions():
            for vpc in self.get_vpcs(region):
                vpc_by_region[vpc] = region

        return vpc_by_region


if __name__ == "__main__":
    aws = AWS()
    pprint(aws.get_regions())
    pprint(aws.get_vpcs('us-west-1'))
    pprint(aws.get_all_vpcs())
