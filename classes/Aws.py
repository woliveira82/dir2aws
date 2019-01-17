import os, json, boto3


class Aws:


    def __init__(self):
        
        with open('./credentials.json') as jsonFile:
            cred = json.load(jsonFile)
            jsonFile.close()

        self.client = boto3.client(
            's3',
            aws_access_key_id=cred['accessKeyId'],
            aws_secret_access_key=cred['accessKeyId']
        )
        self.bucket = cred['bucket']


    def uploadDir(self, directory):
        directory = os.path.abspath(directory)
        print('Uploading directory "{0}" to "s3://{1}":'.format(directory, self.bucket))
        for root, dirs, files in os.walk(directory):
            for item in files:
                filename = '{0}/{1}'.format(root, item)
                print('    Sending file: {0}'.format(filename))
                #self.client.upload_file(filename, bucket, filename[1:])
        print('End of upload')
        return 0

