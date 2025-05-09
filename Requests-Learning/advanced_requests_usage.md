# Advanced Usage of Python Requests Library

## Proxies

If you need to use a proxy, you can configure individual requests with the `proxies` argument to any request method:

```python
import requests

proxies = {
  'http': 'http://10.10.1.10:3128',
  'https': 'http://10.10.1.10:1080',
}

requests.get('http://example.org', proxies=proxies)
```

Alternatively, you can configure it once for an entire `Session`:

```python
import requests

proxies = {
  'http': 'http://10.10.1.10:3128',
  'https': 'http://10.10.1.10:1080',
}
session = requests.Session()
session.proxies.update(proxies)

session.get('http://example.org')
```

**Warning:** Setting `session.proxies` may behave differently than expected. Values provided will be overwritten by environmental proxies. To ensure correct behavior, explicitly specify the `proxies` argument on each request.

Environment variable configuration example:

```bash
export HTTP_PROXY="http://10.10.1.10:3128"
export HTTPS_PROXY="http://10.10.1.10:1080"
export ALL_PROXY="socks5://10.10.1.10:3434"
```

Using Basic Auth with a proxy:

```bash
export HTTPS_PROXY="http://user:pass@10.10.1.10:1080"
```

Or in Python:

```python
proxies = {'http': 'http://user:pass@10.10.1.10:3128/'}
```

**Warning:** Storing credentials in environment variables or source files is insecure.

To give a proxy for a specific host:

```python
proxies = {'http://10.20.1.128': 'http://10.10.1.10:5323'}
```

Ensure proxy URLs include the scheme.

Trust proxy root certificate for HTTPS connections:

```python
from requests.utils import DEFAULT_CA_BUNDLE_PATH
print(DEFAULT_CA_BUNDLE_PATH)
```

Override with:

```bash
export REQUESTS_CA_BUNDLE="/usr/local/myproxy_info/cacert.pem"
```

### SOCKS Proxies

Install support:

```bash
python -m pip install 'requests[socks]'
```

Usage:

```python
proxies = {
    'http': 'socks5://user:pass@host:port',
    'https': 'socks5://user:pass@host:port'
}
```

Use `socks5h` for DNS resolution on proxy.

## Compliance

Requests follows HTTP specifications where it does not negatively impact usability.

## Encodings

Requests guesses encoding if not provided using `charset_normalizer` or `chardet`. To manually override:

```python
response.encoding = 'utf-8'
```

## HTTP Verbs

Supports: `GET`, `POST`, `PUT`, `DELETE`, `PATCH`, `HEAD`, `OPTIONS`.

Example:

```python
import requests

r = requests.get('https://api.github.com/repos/psf/requests/issues/482')
if r.status_code == 200:
    issue = r.json()
    print(issue['title'])
```

## Custom Verbs

Use `.request()` for non-standard verbs:

```python
r = requests.request('MKCOL', url, data=data)
```

## Link Headers

Requests parses pagination links:

```python
r.links["next"]
r.links["last"]
```

## Transport Adapters

Create custom adapters like this:

```python
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager
import ssl

class Ssl3HttpAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(
            num_pools=connections, maxsize=maxsize,
            block=block, ssl_version=ssl.PROTOCOL_SSLv3)
```

Mount with:

```python
s = requests.Session()
s.mount('https://github.com/', Ssl3HttpAdapter())
```

## Automatic Retries

```python
from urllib3.util import Retry
from requests.adapters import HTTPAdapter
from requests import Session

s = Session()
retries = Retry(
    total=3,
    backoff_factor=0.1,
    status_forcelist=[502, 503, 504],
    allowed_methods={'POST'},
)
s.mount('https://', HTTPAdapter(max_retries=retries))
```

## Blocking vs Non-Blocking

Requests is blocking by default. For async use `httpx`, `requests-threads`, etc.

## Header Ordering

Use `OrderedDict` for custom header ordering:

```python
from collections import OrderedDict

headers = OrderedDict([
    ('User-Agent', 'my-app'),
    ('Accept', 'application/json'),
])
```

## Timeouts

Set timeouts to avoid hangs:

```python
requests.get('https://github.com', timeout=5)
requests.get('https://github.com', timeout=(3.05, 27))
```

Use `None` to wait forever:

```python
requests.get('https://github.com', timeout=None)
```

---

This document includes advanced techniques to help you control proxy behavior, HTTP method usage, retry logic, and much more when using the `requests` library.
