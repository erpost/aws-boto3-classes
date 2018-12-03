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
        vpc_region = {}
        for region in self.get_regions():
            for vpc in self.get_vpcs(region):
                vpc_region[vpc] = region

        return vpc_region

    def get_default_vpc(self, region):
        """Returns a Default VPC in a Region"""
        default_vpc = ''
        self.region = region
        self.client = boto3.client(self.service_type, self.region)
        response = self.client.describe_vpcs()
        for vpc in response['Vpcs']:
            if vpc['IsDefault']:
                default_vpc = vpc['VpcId']

        return default_vpc

    def get_all_default_vpcs(self):
        """Returns a dictionary of Default VPCs in all Regions"""
        default_vpcs = {}
        for region in self.get_regions():
            default_vpcs[self.get_default_vpc(region)] = region

        return default_vpcs

    def get_subnets(self, vpc_id):
        """Returns all subnets in a VPC"""
        subnets = []
        response = self.client.describe_subnets(
            Filters=[
                {
                    'Name': 'vpc-id',
                    'Values': [vpc_id]
                }
            ]
        )
        for subnet in response['Subnets']:
            subnets.append(subnet['SubnetId'])

        return subnets


if __name__ == "__main__":
    aws = AWS()
    print('#' * 50 + '\nGetting All Regions\n' + '#' * 50)
    pprint(aws.get_regions())
    print('#' * 50 + '\nGetting VPCs in US East 1\n' + '#' * 50)
    pprint(aws.get_vpcs('us-east-1'))
    print('#' * 50 + '\nGetting All VPCs in All Regions\n' + '#' * 50)
    pprint(aws.get_all_vpcs())
    print('#' * 50 + '\nGetting Default VPC in US East 1\n' + '#' * 50)
    pprint(aws.get_default_vpc('us-east-1'))
    print('#' * 50 + '\nGetting All Default VPCs in All Regions\n' + '#' * 50)
    pprint(aws.get_all_default_vpcs())
    print('#' * 50 + '\nGetting All Subnets in a VPC\n' + '#' * 50)
    pprint(aws.get_subnets('vpc-8221c1f8'))
