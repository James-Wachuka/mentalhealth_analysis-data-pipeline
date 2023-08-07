from prefect_gcp import GcpCredentials
from prefect_gcp.cloud_storage import GcsBucket

# alternative to creating GCP blocks in the UI
# copy your own service_account_info dictionary from the json file you downloaded from google
# IMPORTANT - do not store credentials in a publicly available repository!

# enter your credentials from the json file
credentials_block = GcpCredentials(
    service_account_info={
  "type": "service_account",
  "project_id": "mental-health-analysis-395019",
  "private_key_id": "dc302d910c18d5459aa48d9e0eb26a562648112f",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDcQ1yDmd0V1H9w\n4i0+3b92306GzrSj3IscQKXwftM4B35kDXcibsj43VvTs4E2H2sCeKI8uOgnIdwD\nDx4EH52b355XCGjeTI2t+iL/nj4aXIRzKhKhCKRifbggzmSKkq2BXAM3l27YtXWC\nuYv5Dt+jbZYAcO9ajGFj4q0vY/9ZdFwjRK+O01+qbVG9+srbnLa4n6sGgHr6rQOd\nEldAa3xd52HADec+OhbANsahSEOZyT35JhhI27YYmPOHLo8xWhe1n+JCc/u+OB7I\nhSHMFVYqJIFBbtU2t5FZNdmyHC368VzZNgKd51uM1t9AlzmTKDaLKQq0ET0/shN3\nu9Yrct/FAgMBAAECggEAEuj7l9bNWtLwEAZzAPsztWZtjPhRHOJR1R6dwHx68Mv/\n52IakMu3GFqUyCOYm8dtvfwSXak4USfAhki1eIAoXVoA85LmwfMLlNytRYnV5hh8\nTJDXoZim2EfX14Uwr47xM3JtWkf3fcZybMM2R68ltxew8Z/AhOMZd2ReHvv0T78b\nZBeYMoAr9C6IFVohS/M7Lyjj+PHo2Mjpzw4W2LqkGDisg/2bbB2LmptASm1Hn6Y4\nbw8potIAW3Vl/EwA3GZLnh1bgLEkGPWBshoetPOJwEnNFLUfbQ/yWqmG9EkAD76O\nNZXZiSfm2RcD2SOvh2VwH61UoymT8apBhAIucmSv0QKBgQDx6wN8NWkEzt3T53JT\nwhXDWzuuLNX24XUYc2SHPEuLYP3uT5oV9EP4NYxf0KE0hVd2/ywPT9xEsOwfBVTl\npWomAMLVNdR+NWaACoij8I0ceBJOXDWmGbGL28jTockNXOQBJDR/K8V7iBsYF/dN\nyP3gXlBGOzgNDNDkrfad1NtgGQKBgQDpFadDrdhCf+dK4mvcw3bty9AtofU8HDt2\nmIq27oNo/2zF4DzhqI4k55TFg1i66PRbBHW3E0RpTtgC3J8HmPFgaNvLXomRxuW/\nEHBXOcWpm7S6JAaDzSITSz7zX0pOvgKIFbvq0bqAT9AkPhlCWQie9+NU6KzSag+P\njW4F96zCjQKBgQCu8GP0zirDb1S6iAQEzbUvMCpYKdQQU7l5lPh9UvzOLbVzP90N\nQzZjp1V7dEMe184IHz6dVALVKZuWUySxbIz2Lla2F9cx7SvSK8vjwXBJxgp23/dr\nxei+WpE/eR8KqsG2kZfk3qJQUnxFUA9mEJKGTa1/HBPMXBgzRhmwyNxbAQKBgQC8\nhITqWlsFPgnGKWdwAK/aGPRhVBLS8Uqu2yWmWzbx31UMnhbftMJy2tMbBObpFa09\nSFglIHI+ckSH3ATL0km33leXHvlJbIM5i4QxKErUqVj9DFIwm+Mpk7xwfuvM0CWg\nB2QbwlGDogoIpikr3nL4kCnP7PiKnrnDM3J/ZRjXqQKBgBjQlZCetHyyUxmTciE7\n0BhrDELIPOeV6xvEkQVrrcE/d4Gx4fqWcEhXM9MgYMubtTLKlY+xCw2sF5RoNYKv\nEw3FWhdCx20z6dQu4WUUow4T7+1wn2o6DfQX1PWR3oNaQR2mNrajf/AVE0+X9j/q\nrmmCPncsA8CcDNtX7pCwC8pK\n-----END PRIVATE KEY-----\n",
  "client_email": "mental-health-analysis-23@mental-health-analysis-395019.iam.gserviceaccount.com",
  "client_id": "117017854749886043193",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/mental-health-analysis-23%40mental-health-analysis-395019.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

)
credentials_block.save("gcp-creds", overwrite=True)


bucket_block = GcsBucket(
    gcp_credentials=GcpCredentials.load("gcp-creds"),
    bucket="mentalhealth_data_mental-health-analysis-395019",  # insert your  GCS bucket name
)

bucket_block.save("mental-health-gcs", overwrite=True)

