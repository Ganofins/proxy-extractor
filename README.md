# Proxy Extractor

<a href="https://github.com/Ganofins/proxy-extractor/releases">
    <img src="https://img.shields.io/pypi/v/proxy-extractor?color=3498db&label=version">
</a>

**Proxy Extractor** is a utility for extracting free proxies from various free proxy listings.

Currectly, it extracts proxy from the following listings:

[free-proxy-list](https://free-proxy-list.net/)

#### Installation
##### with pip
```
pip3 install proxy-extractor
```
##### or build from source
```
git clone https://github.com/Ganofins/proxy-extractor.git && cd proxy-extractor && python3 setup.py install
```

<hr>

### Documentation
proxy-extractor is available as both a package as well as a command line program. The relevant documentation can be found below:

- [For package usage](https://github.com/Ganofins/proxy-extractor#for-package-usage)
- [For cmd usage](https://github.com/Ganofins/proxy-extractor#for-cmd-usage)

### For package usage
The sample program below demonstrates usage of `proxy-extractor` library

```python
from proxy_extractor.extractor import extract_proxy

proxy_list = extract_proxy(https=True, proxy_count=10)
print(proxy_list)
```

it returns output as a list

The arguments `https` and `proxy_count` are optional.

- `https` to display only https supportable proxies
- `proxy_count` define number of proxies you want to extract (max. 300)

<hr>

### For cmd usage
`cli.py` provides a grep-like command line interface to `proxy-extractor` library. You will need to install the library first to use it.


```bash
python cli.py --https --count 10
```

- `--https` to display only https supportable proxies
- `--count` define number of proxies you want to extract (max. 300)
- `--json` to display proxies in json format

# Contribute
Feel free to contribute to this repository.