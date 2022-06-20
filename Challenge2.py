#!/usr/bin/env python3
import boto3
import json, sys

ec2_instance_id= input("Enter the EC2 Instance: ")

session=boto3.Session(profile_name='default',region_name="us-east-1")
ec2_resoruce=session.resource(service_name='ec2')
ec2_client=session.client(service_name='ec2')
data=ec2_client.describe_instances()
for inst in data['Reservations']:
    if inst['Instances'][0]['InstanceId'] == ec2_instance_id:
        data = inst['Instances'][0]
        app_json = json.dumps(data,default=str,indent=4)
        print(app_json)
        sys.exit()
print("Not a valid Instance id")
sys.exit()