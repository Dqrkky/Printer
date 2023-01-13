import requests, xmltodict, base64

def req(js0n: dict=None, r=None):
    if js0n != None and isinstance(js0n, dict) and len(js0n) > 0:
        if "r" in js0n and js0n["r"] != None:
            r_ = js0n["r"]
        else:
            if r != None:
                r_ = r
            else:
                r_ = None
        if "method" in js0n and js0n["method"] != None:
            method_ = js0n["method"]
        else:
            method_ = None
        if "url" in js0n and js0n["url"] != None:
            url_ = js0n["url"]
        else:
            url_ = None
        if "params" in js0n and js0n["params"] != None:
            params_ = js0n["params"]
        else:
            params_ = None
        if "data" in js0n and js0n["data"] != None:
            data_ = js0n["data"]
        else:
            data_ = None
        if "headers" in js0n and js0n["headers"] != None:
            headers_ = js0n["headers"]
        else:
            headers_ = None
        if "aftermethod" in js0n and js0n["aftermethod"] != None:
            aftermethod_ = js0n["aftermethod"]
        else:
            aftermethod_ = None
        if r_ != None and method_ != None and url_ != None and aftermethod_ != None:
            re = r_.request(
                method=method_,
                url=url_,
                params=params_,
                data=data_,
                headers=headers_
            )
            if aftermethod_ == "text":
                data_out = re.text
            elif aftermethod_ == "json":
                data_out = re.json()
            elif aftermethod_ == "content":
                data_out = re.content
            elif aftermethod_ == "re":
                data_out = re
            else:
                data_out = None
            return data_out

class HP044C0C:
    def __init__(self, host: str="http://hp044c0c", username :str="admin", password :str=None):
        with requests.Session() as rss:
            self.rss = rss
        self.rss.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52"
        self.config = {
            "host": host,
            "headers": {
                "Authorization": None
            }
        }
        if username != None and isinstance(username, str) and password != None and isinstance(password, str):
            self.config["headers"]["Authorization"] = f"Basic {base64.b64encode(f'{username}:{password}'.encode()).decode()}"
    def Scan(self):
        req(
            js0n={
                "method": "post",
                "url": f'{self.config["host"]}/eSCL/ScanJobs',
                "data": xmltodict.unparse(
                    {
                        'scan:ScanSettings': {
                            '@xmlns:scan': 'http://schemas.hp.com/imaging/escl/2011/05/03',
                            '@xmlns:copy': 'http://www.hp.com/schemas/imaging/con/copy/2008/07/07',
                            '@xmlns:dd': 'http://www.hp.com/schemas/imaging/con/dictionaries/1.0/',
                            '@xmlns:dd3': 'http://www.hp.com/schemas/imaging/con/dictionaries/2009/04/06',
                            '@xmlns:fw': 'http://www.hp.com/schemas/imaging/con/firewall/2011/01/05',
                            '@xmlns:scc': 'http://schemas.hp.com/imaging/escl/2011/05/03',
                            '@xmlns:pwg': 'http://www.pwg.org/schemas/2010/12/sm',
                            'pwg:Version': '2.1',
                            'scan:Intent': 'Photo',
                            'pwg:ScanRegions': {
                                'pwg:ScanRegion': {
                                    'pwg:Height': '3507',
                                    'pwg:Width': '2481',
                                    'pwg:XOffset': '0',
                                    'pwg:YOffset': '0'
                                }
                            },
                            'scan:DocumentFormatExt': 'image/jpeg',
                            'scan:XResolution': '600',
                            'scan:YResolution': '600',
                            'scan:ColorMode': 'RGB24',
                            'scan:CompressionFactor': '0',
                            'scan:Brightness': '1000',
                            'scan:Contrast': '1000'
                        }
                    }
                ),
                "aftermethod": "re"
            },
            r=self.rss
        )
        data1 = req(
            js0n={
                "method": "get",
                "url": f'{self.config["host"]}/eSCL/ScannerStatus',
                "aftermethod": "text"
            },
            r=self.rss
        )
        if data1 != None and isinstance(data1, str):
            data2 = xmltodict.parse(xml_input=data1)
            if data2 != None and isinstance(data2, dict):
                if "scan:ScannerStatus" in data2 and data2["scan:ScannerStatus"] != None and isinstance(data2["scan:ScannerStatus"], dict) and "scan:Jobs" in data2["scan:ScannerStatus"] and data2["scan:ScannerStatus"]["scan:Jobs"] != None and isinstance(data2["scan:ScannerStatus"]["scan:Jobs"], dict) and "scan:JobInfo" in data2["scan:ScannerStatus"]["scan:Jobs"] and data2["scan:ScannerStatus"]["scan:Jobs"]["scan:JobInfo"] != None and isinstance(data2["scan:ScannerStatus"]["scan:Jobs"]["scan:JobInfo"], list) and len(data2["scan:ScannerStatus"]["scan:Jobs"]["scan:JobInfo"]) > 0 and "pwg:JobUuid" in data2["scan:ScannerStatus"]["scan:Jobs"]["scan:JobInfo"][0] and data2["scan:ScannerStatus"]["scan:Jobs"]["scan:JobInfo"][0]["pwg:JobUuid"] != None and isinstance(data2["scan:ScannerStatus"]["scan:Jobs"]["scan:JobInfo"][0]["pwg:JobUuid"], str):
                    return f'{self.config["host"]}/eSCL/ScanJobs/{data2["scan:ScannerStatus"]["scan:Jobs"]["scan:JobInfo"][0]["pwg:JobUuid"]}/NextDocument'

class Scan:
    def __init__(self):
        with requests.Session() as rss:
            self.rss = rss
        self.rss.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52"
    def save(self, url :str=None):
        if url != None and isinstance(url, str):
            data1 = req(
                js0n={
                    "method": "get",
                    "url": url,
                    "aftermethod": "re"
                },
                r=self.rss
            )
            if data1 != None and "Content-Type" in data1.headers and data1.headers["Content-Type"] != None and isinstance(data1.headers["Content-Type"], str):
                file_name = url.split("/")[-1]
                file_type = data1.headers["Content-Type"].split("/")[1]
                with open(file=f"{file_name}.{file_type}", mode="wb+") as f:
                    f.write(data1.content)