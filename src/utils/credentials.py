import boto3
import json

class AWS_Client:
    """ Class for retrieving AWS credentials

    To do:
        Implement functionality to assume into roles [X]
        Implement functionality to use users []
    """

    def __init__(self, account, region='eu-west-1'):
        """ Initialise Object """
        self.account = account
        self.region = region
        self.session = boto3.Session()
        self.credentials = self.get_credentials()

    def get_credentials(self):
        """ Get credentials from AWS

        Returns:
            (dict)credentials: AWS Credentials
        """
        credentials = self.session.get_credentials()
        return credentials

    def assume_role(self, service, role):
        """ Assumes into an iam role, and returns credentials back
        which can be used in a boto3 client

        Args:
            (str)service: name of the service
            (str)role: name of the role to assume into
        Returns:
            (obj)token: token needed for boto3 client
        """
        assume_role_arn = 'arn:aws:iam/' + \
                          self.account + '/role/' + \
                          role
        sts_client = self.client('sts')
        assume_role = sts_client.assume_role(
            RoleArn=assume_role_arn,
            RoleSessionName='UsamaTestRole'
        )
        new_creds = assume_role['Credentials']
        return boto3.client(
            service,
            region_name=self.region,
            aws_access_key_id=new_creds.access_key,
            aws_secret_access_key=new_creds.secret_key,
            aws_session_token=new_creds.session_token
        )

    def client(self, service):
        """ Returns a boto client from the session and
        the service requested

        Args:
            (str)service: name of the service
        Returns:
            (obj)client: boto client for api calls
        """
        return boto3.client(
            service,
            region_name=self.region,
            aws_access_key_id=self.credentials.access_key,
            aws_secret_access_key=self.credentials.secret_key
        )
