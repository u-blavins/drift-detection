import boto3
import json


def main():
    client = boto3.client('s3')
    response = client.list_buckets()
    print json.dumps(response, indent=4, default=str)
    return 0


if __name__ == '__main__':
    main()
