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
