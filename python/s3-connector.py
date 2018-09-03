import boto3
import botocore
import itertools

def setS3():
    s3 = boto3.resource('s3')
    return s3

def listBuckets():
    s3 = setS3()
    print "connected to s3"
    for bucket in s3.buckets.all():
        print bucket.name

def connectToBucket():
    s3 = setS3()
    bucket_name = 'kawsay-utec'
    bucket = s3.Bucket(bucket_name)
    exists = True
    try:
        s3.meta.client.head_bucket(Bucket=bucket_name)
        print "connected to bucket"
        return bucket
    except botocore.exceptions.ClientError as e:
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            exists = False

# lists all files with a given extension
def listFiles(ext):
    s3 = setS3()
    bucket = connectToBucket()
    filesWithExt = []
    for obj in bucket.objects.filter(Prefix='ls'):
        if str(obj.key).endswith(ext):
            filesWithExt.append(obj.key)
            print obj.key
    return filesWithExt
    print "returned all files with '{0}' extension.".format(ext)
    
def listFilesForYear(year):
    s3 = setS3()
    bucket = connectToBucket()
    year = '_' + str(year)
    filesForYear = []
    for obj in bucket.objects.filter(Prefix='ls'):
        if year not in str(obj.key):
            continue
        else:
            filesForYear.append(obj.key)
    return filesForYear

def getFileDates():
    s3 = setS3()
    bucket = connectToBucket()
    dates = []
    for obj in bucket.objects.filter(Prefix='ls'):
        date = str(obj.key)[22:30]
        dates.append(date)
    dates.sort()
    dates = list(dates for dates,_ in itertools.groupby(dates))
    print dates
    return dates

def downloadFiles():
    # should have options for date range, ls type, band range, output location...
    exit

def downloadForNDVI():
    exit

def downloadForEVI():
    exit

def downloadForSAVI():
    exit

# listBuckets()
connectToBucket()
listFiles('.txt')
# listFilesForYear(2018)
# getFileDates()