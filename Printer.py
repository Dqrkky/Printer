import requests
import json
import xmltodict
import base64
import shared

class HP044C0C:
    def __init__(self, host: str="http://hp044c0c", username :str="admin", password :str=None):
        with requests.Session() as rss:
            self.rss = rss
        self.shared = shared.Shared(
            rss=self.rss
        )
        self.config = {
            "host": host,
            "headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240" 
            }
        }
        if hasattr(self, "rss") and self.rss != None and \
        hasattr(self, "config") and self.config != None and isinstance(self.config, dict) and \
        "headers" in self.config and self.config["headers"] != None and isinstance(self.config["headers"], dict):  # noqa: E711
            if username != None and isinstance(username, str) and \
            password != None and isinstance(password, str):  # noqa: E711
                self.config["headers"]["Authorization"] = self.makeAuthorization(
                    username=username,
                    password=password
                )
            self.rss.headers.update(self.config["headers"])
    def __repr__(self):
        # Return a string representation of the HP044C0C
        return 'HP044C0C(host: str="http://hp044c0c", username :str="admin", password :str=None)'
    def makeAuthorization(self, username :str=None, password :str=None):
        if username != None and isinstance(username, str) and \
        password != None and isinstance(password, str):  # noqa: E711
            return f"Basic {base64.b64encode(f'{username}:{password}'.encode()).decode()}"
    def request(self, config :dict=None):
        if hasattr(self, "rss") and self.rss != None and \
        hasattr(self, "shared") and self.shared != None:  # noqa: E711
            if config != None and isinstance(config, dict):  # noqa: E711
                req = self.rss.request(
                    *self.shared.convert_json_to_values(
                        config=config
                    )
                )
                return req
    def authcheck(self):
        if hasattr(self, "request") and self.request != None and \
        hasattr(self, "config") and self.config != None and isinstance(self.config, dict) and \
        "host" in self.config and self.config["host"] != None and isinstance(self.config["host"], str):  # noqa: E711
            config = {
                "method": "get",
                "url": f'{self.config["host"]}/AuthChk'
            }
            req = self.request(
                config=config
            )
            if req != None:  # noqa: E711
                return req.json()
    def scan(self):
        if hasattr(self, "request") and self.request != None and \
        hasattr(self, "config") and self.config != None and isinstance(self.config, dict) and \
        "host" in self.config and self.config["host"] != None and isinstance(self.config["host"], str):  # noqa: E711
            config = {
                "method": "post",
                "url": f'{self.config["host"]}/eSCL/ScanJobs',
                "data": xmltodict.unparse(
                    {
                        'scan:ScanSettings': {
                            '@xmlns:scan': 'http://schemas.hp.com/imaging/escl/2011/05/03',
                            '@xmlns:copy': 'http://www.hp.com/schemas/imaging/con/copy/2008/07/07',
                            '@xmlns:dd': 'http://www.hp.com/schemas/imaging/con/dictionaries/1.0',
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
                )
            }
            req = self.request(
                config=config
            )
            print(req)
            config1 = {
                "method": "get",
                "url": f'{self.config["host"]}/eSCL/ScannerStatus'
            }
            req1 = self.request(
                config=config1
            )
            if req == None:  # noqa: E711
                return
            data1 = req1.text
            if data1 != None and isinstance(data1, str):  # noqa: E711
                data2 = xmltodict.parse(data1)
                if data2 != None and isinstance(data2, dict):  # noqa: E711
                    return data2
    def getconfigurationconstraints(self):
        if hasattr(self, "request") and self.request != None and \
        hasattr(self, "config") and self.config != None and isinstance(self.config, dict) and \
        "host" in self.config and self.config["host"] != None and isinstance(self.config["host"], str):  # noqa: E711
            config = {
                "method": "get",
                "url": f'{self.config["host"]}/cdm/controlPanel/v1/configuration/constraints'
            }
            req = self.request(
                config=config
            )
            if req != None:  # noqa: E711
                return req.json()
    def getconfiguration(self):
        if hasattr(self, "request") and self.request != None and \
        hasattr(self, "config") and self.config != None and isinstance(self.config, dict) and \
        "host" in self.config and self.config["host"] != None and isinstance(self.config["host"], str):  # noqa: E711
            config = {
                "method": "get",
                "url": f'{self.config["host"]}/cdm/controlPanel/v1/configuration'
            }
            req = self.request(
                config=config
            )
            if req != None:  # noqa: E711
                return req.json()
    def setconfiguration(self, deviceLanguage :str=None, displayContrast :int=None, keyPressVolume :str=None, version :str=None):
        if hasattr(self, "request") and self.request != None and \
        hasattr(self, "config") and self.config != None and isinstance(self.config, dict) and \
        "host" in self.config and self.config["host"] != None and isinstance(self.config["host"], str):  # noqa: E711
            config = {
                "method": "put",
                "url": f'{self.config["host"]}/cdm/controlPanel/v1/configuration',
                "data": json.dumps(
                    {
                        **({"deviceLanguage": deviceLanguage} if deviceLanguage != None and isinstance(deviceLanguage, str) else {}),  # noqa: E711
                        **({"displayContrast": displayContrast} if displayContrast != None and isinstance(displayContrast, int) else {}),  # noqa: E711
                        **({"keyPressVolume": keyPressVolume} if keyPressVolume != None and isinstance(keyPressVolume, str) else {}),  # noqa: E711
                        **({"version": version} if version != None and isinstance(version, str) else {}),  # noqa: E711
                    }
                )
            }
            req = self.request(
                config=config
            )
            if req != None:  # noqa: E711
                return req.json()
    def getprintmodeconfiguration(self):
        if hasattr(self, "request") and self.request != None and \
        hasattr(self, "config") and self.config != None and isinstance(self.config, dict) and \
        "host" in self.config and self.config["host"] != None and isinstance(self.config["host"], str):  # noqa: E711
            config = {
                "method": "get",
                "url": f'{self.config["host"]}/cdm/print/v1/printModeConfiguration'
            }
            req = self.request(
                config=config
            )
            if req != None:  # noqa: E711
                return req.json()
    def setprintmodeconfiguration(self, quietPrintModeEnabled :bool=False, version :str=None):
        if hasattr(self, "request") and self.request != None and \
        hasattr(self, "config") and self.config != None and isinstance(self.config, dict) and \
        "host" in self.config and self.config["host"] != None and isinstance(self.config["host"], str):  # noqa: E711
            config = {
                "method": "put",
                "url": f'{self.config["host"]}/cdm/print/v1/printModeConfiguration',
                "data": json.dumps(
                    obj={
                        **({"quietPrintModeEnabled": quietPrintModeEnabled} if quietPrintModeEnabled != None and isinstance(quietPrintModeEnabled, bool) else {}),  # noqa: E711
                        **({"version": version} if version != None and isinstance(version, str) else {})  # noqa: E711
                    }
                )
            }
            req = self.request(
                config=config
            )
            if req != None:  # noqa: E711
                return req.json()

class Scan:
    def __init__(self):
        with requests.Session() as rss:
            self.rss = rss
        self.shared = shared.Shared(
            rss=self.rss
        )
        self.config = {
            "headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240"
            }
        }
        if hasattr(self, "rss") and self.rss != None and \
        hasattr(self, "config") and self.config != None and isinstance(self.config, dict) and \
        "headers" in self.config and self.config["headers"] != None and isinstance(self.config["headers"], dict):  # noqa: E711
            self.rss.headers.update(self.config["headers"])
    def request(self, config :dict=None):
        if hasattr(self, "rss") and self.rss != None and \
        hasattr(self, "shared") and self.shared != None:  # noqa: E711
            if config != None and isinstance(config, dict):  # noqa: E711
                req = self.rss.request(
                    *self.shared.convert_json_to_values(
                        config=config
                    )
                )
                if req.status_code == 200:
                    return req
    def save(self, url :str=None):
        if hasattr(self, "request") and self.request != None:  # noqa: E711
            if url != None and isinstance(url, str):  # noqa: E711
                config = {
                    "method": "get",
                    "url": url
                }
                req = self.request(
                    config=config
                )
                if req != None:  # noqa: E711
                    if "Content-Type" in req.headers and req.headers["Content-Type"] != None and isinstance(req.headers["Content-Type"], str):  # noqa: E711
                        file_name = url.split("/")[-1]
                        file_type = req.headers["Content-Type"].split("/")[1]
                        with open(file=f"{file_name}.{file_type}", mode="wb+") as f:
                            f.write(req.content)