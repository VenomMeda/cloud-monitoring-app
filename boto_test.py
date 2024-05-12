import boto3
from botocore.config import Config


sts = boto3.client('sts')
print(sts.get_caller_identity())

[profile my-base-profile]
# Set up in whatever your usual fashion is
[profile my-assumed-role-profile]
role_arn = arn:aws:iam::123456789012:role/MyRoleToAssume
source_profile = my-base-profile
# or on EC2 instance/ECS, you might do one of:
# credential_source = Ec2InstanceMetadata
# credential_source = EcsContainer


base_session = boto3.Session(profile_name='my-base-profile')
print(base_session.client('sts').get_caller_identity())
# will show your normal identity
# independent of the above code
assumed_role_session = boto3.Session(profile_name='my-assumed-role-profile')
print(assumed_role_session.client('sts').get_caller_identity())
# will show that you're using MyRoleToAssume