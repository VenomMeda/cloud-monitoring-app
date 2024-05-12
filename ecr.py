import boto3

# mySession = boto3.session.Session()
#set region



# Create an ECR client
#ecr_client = boto3.client('ecr', aws_access_key_id='<your access id>', aws_secret_access_key='<your secret access key id>', region_name='us-east-1')

# Create a new ECR repository
repository_name = 'flask-app-repo'
response = ecr_client.create_repository(repositoryName=repository_name)

# Print the repository URI
repository_uri = response['repository']['repositoryUri']
print(repository_uri)