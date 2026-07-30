

import requests
import pyotp
import hashlib
import base64

email = "raghavharshita999@gmail.com"


secret = email + "HENNGECHALLENGE004"
secret_base32 = base64.b32encode(secret.encode()).decode()

totp = pyotp.TOTP(
  secret_base32,
  digits=10,
  digest=hashlib.sha512,
  interval=30
).now()

# Basic Auth

auth = f"{email}:{totp}"
auth_b64 = base64.b64encode(auth.encode()).decode()

url = "https://api.challenge.hennge.com/challenges/backend-recursion/004"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Basic {auth_b64}",
}
data = {
  "github_url": "https://gist.github.com/Hershe-cpu/10b94f762c1184eeeeebc1e391567811",
  "contact_email": "raghavharshita999@gmail.com",
  "solution_language": "python"
}

response = requests.post(url,headers=headers,json=data)
print(response.status_code)
print(response.text)
