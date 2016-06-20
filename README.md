# opensecrets Scraper 

## Installation

```shell
virtualenv venv
. venv/bin/activate
pip install -U -r requirements.txt

```

## How to use

### File
```shell
scrapy crawl opensecrets -s OUTPUT_URI="output/"
```

### AWS S3
```shell
scrapy crawl opensecrets -s OUTPUT_URI="s3://bucket/output/" -s AWS_ACCESS_KEY_ID="YOURACCESSKEY" -s AWS_SECRET_ACCESS_KEY="YOURSECRETKEY"
```

### Controlling the number of processes

You can use the command-line argument `-s CONCURRENT_REQUESTS=x` to set the number of processes to use:

```shell
scrapy crawl opensecrets -s OUTPUT_URI="output/" -s CONCURRENT_REQUESTS=8
```

or with AWS S3 as a storage:

```shell
scrapy crawl opensecrets -s OUTPUT_URI="s3://bucket/output/" -s AWS_ACCESS_KEY_ID="YOURACCESSKEY" -s AWS_SECRET_ACCESS_KEY="YOURSECRETKEY" -s CONCURRENT_REQUESTS=8
```

### Throttling the crawling speed

You can use the command-line argument `-s DOWNLOAD_DELAY=x` to set the amount of time (in secs) that the downloader
should wait before downloading consecutive pages.

```shell
scrapy crawl opensecrets -s OUTPUT_URI="output/" -s DOWNLOAD_DELAY=1
```

or with AWS S3 as a storage:

```shell
scrapy crawl opensecrets -s OUTPUT_URI="s3://bucket/output/" -s AWS_ACCESS_KEY_ID="YOURACCESSKEY" -s AWS_SECRET_ACCESS_KEY="YOURSECRETKEY" -s DOWNLOAD_DELAY=1
```


## Alternatives ways to configure AWS credentials

You have a few options for providing the AWS credentials:

### Using a Boto configuration file

Create a ~/.boto file with these contents:

```
[Credentials]
aws_access_key_id = YOURACCESSKEY
aws_secret_access_key = YOURSECRETKEY
```


### Using a shared AWS configuration file

Create a ~/.aws/credentials file with these contents:

```
[default]
aws_access_key_id = <your access key>
aws_secret_access_key = <your secret key>
```

More info here http://boto.cloudhackers.com/en/latest/boto_config_tut.html
