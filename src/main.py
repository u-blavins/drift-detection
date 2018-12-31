import json
from utils.credentials import AWS_Client


def get_details():
    """ Go into

    :return:
    """


def get_stacks(client):
    """ Make a call to AWS to retrieve CloudFormation
    stacks

    Args:
        (obj)client: boto3 client
    Returns:
        (list)stacks: a list of CF stacks
    """
    stacks = []
    paginator = client.get_paginator('describe_stacks')
    response = paginator.paginate()
    for page in response:
        for stack in page['Stacks']:
            stacks.append(stack)
    return stacks


# def detect_drift(stacks):
#     return 0


def main(aws_client):
    """ Main function

    Args:
        (obj)aws_client: boto3 client
    """
    # stacks = get_stacks(aws_client)
    # print json.dumps(stacks, indent=4, default=str)
    return 0


if __name__ == '__main__':
    client = AWS_Client('account_number').client
    main(client)
