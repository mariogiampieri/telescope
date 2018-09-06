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
    for obj in bucket.objects.filter(Prefix='ls08/LC08'):
        if str(obj.key).endswith(ext):
            filesWithExt.append(obj.key)
            # print obj.key
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

def getLS08(cover_threshold=15):
    meta_ext = "MTL.txt"
    meta_files = listFiles(meta_ext)
    bucket = connectToBucket()
    s3_client = boto3.client('s3')
    x = {}
    for each in meta_files:
        z = s3_client.get_object(Bucket='kawsay-utec', Key=each)
        
    to_download = []
    print "checking files..."
    for every in x:
        cloud_cover = float(x[every].split('=')[1])
        # cloud_cover_land = float(x[every][1].split('=')[1])
        base_name = str(every)[:-7]
        
        if cloud_cover <= cover_threshold:
            to_download.append(base_name)
    
    exts = ['ANG.txt', 'sr_band7.tif', 'sr_band6.tif', 'sr_band5.tif', 'sr_band4.tif', 'sr_band3.tif', 'sr_band2.tif', 'sr_band1.tif', 'sr_aerosol.tif', 'radsat_qa.tif', 'pixel_qa.tif']
    each_band = []
    for ea in to_download:
        for a in exts:
            each_band.append(ea+a)
    print 'Found ' + str(len(to_download)) + ' scene(s) with less than ' + str(cover_threshold) + '% cloud cover.'
    print "downloading files..."
    for all in each_band:
        boto3.resource('s3').Bucket('kawsay-utec').download_file(all, str(all)[5:])
        print "downloading " + str(all) + "..." 
    print "downloaded all files."
    # print meta_files

def downloadFiles():
    # should have options for date range, ls type, band range, output location...
    exit

def downloadForNDVI():
    exit

def downloadForEVI():
    exit

def downloadForSAVI():
    exit

# getLS08()
# listBuckets()
# connectToBucket()
# listFiles('.txt')
# listFilesForYear(2018)
# getFileDates()