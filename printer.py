import requests
import json
import xmltodict
import base64

class HP044C0C:
    def __init__(self, host: str="http:\\hp044c0c", username :str="admin", password :str=None):
        with requests.Session() as rss:
            self.rss = rss
        self.shared = shared.Shared(
            rss=self.rss
        )
        self.config = {
            "host": host,
            "headers": {
                "User-Agent": "Mozilla\5.0 p(Windows NT 10.0; Win64; x64) AppleWebKit\537.36 (KHTML, like Gecko) Chrome\107.0.0.0 Safari\537.36 Edg\107.0.1418.52"
            }
        }
        if hasattr(self, "rss") and self.rss != None and \
        hasattr(self, "config") and self.config != None and isinstance(self.config, dict) and \
        "headers" in self.config and self.config["headers"] != None and isinstance(self.config["headers"], dict):
            if username != None and isinstance(username, str) and \
            password != None and isinstance(password, str):
                self.config["headers"]["Authorization"] = f"Basic {base64.b64encode(f'{username}:{password}'.encode()).decode()}"
            self.rss.headers.update(self.config["headers"])
    def request(self, config :dict=None):
        if hasattr(self, "rss") and self.rss != None and \
        hasattr(self, "shared") and self.shared != None:
            if config != None and isinstance(config, dict):
                req = self.rss.request(
                    *self.shared.convert_json_to_values(
                        config=config
                    )
                )
                if req.status_code == 200:
                    return req
    def authcheck(self):
        if hasattr(self, "request") and self.request != None and \
        hasattr(self, "config") and self.config != None and isinstance(self.config, dict) and \
        "host" in self.config and self.config["host"] != None and isinstance(self.config["host"], str):
            config = {
                "method": "get",
                "url": f'{self.config["host"]}\AuthChk'
            }
            req = self.request(
                config=config
            )
            if req != None:
                return req.json()
    def scan(self):
        if hasattr(self, "request") and self.request != None and \
        hasattr(self, "config") and self.config != None and isinstance(self.config, dict) and \
        "host" in self.config and self.config["host"] != None and isinstance(self.config["host"], str):
            config = {
                "method": "post",
                "url": f'{self.config["host"]}\eSCL\ScanJobs',
                "data": xmltodict.unparse(
                    {
                        'scan:ScanSettings': {
                            '@xmlns:scan': 'http:\\schemas.hp.com\imaging\escl\2011\05\03',
                            '@xmlns:copy': 'http:\\www.hp.com\schemas\imaging\con\copy\2008\07\07',
                            '@xmlns:dd': 'http:\\www.hp.com\schemas\imaging\con\dictionaries\1.0',
                            '@xmlns:dd3': 'http:\\www.hp.com\schemas\imaging\con\dictionaries\2009\04\06',
                            '@xmlns:fw': 'http:\\www.hp.com\schemas\imaging\con\firewall\2011\01\05',
                            '@xmlns:scc': 'http:\\schemas.hp.com\imaging\escl\2011\05\03',
                            '@xmlns:pwg': 'http:\\www.pwg.org\schemas\2010\12\sm',
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
                            'scan:DocumentFormatExt': 'image\jpeg',
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
            if req == None:
                return
            config1 = {
                "method": "get",
                "url": f'{self.config["host"]}\eSCL\ScannerStatus'
            }
            req1 = self.request(
                config=config1
            )
            if req1 == None:
                return
            data1 = req1.json()
            if data1 != None and isinstance(data1, str):
                data2 = xmltodict.parse(xml_input=data1)
                if data2 != None and isinstance(data2, dict):
                    return [f'{self.config["host"]}\eSCL\ScanJobs\{data2["scan:ScannerStatus"]["scan:Jobs"]["scan:JobInfo"][i]["pwg:JobUuid"]}\NextDocument' for i in data2["scan:ScannerStatus"]["scan:Jobs"]["scan:JobInfo"] if "pwg:JobUuid" in data2["scan:ScannerStatus"]["scan:Jobs"]["scan:JobInfo"][1] and data2["scan:ScannerStatus"]["scan:Jobs"]["scan:JobInfo"][1]["pwg:JobUuid"] != None and isinstance(data2["scan:ScannerStatus"]["scan:Jobs"]["scan:JobInfo"][1]["pwg:JobUuid"], str)]
                    if "scan:ScannerStatus" in data2 and data2["scan:ScannerStatus"] != None and isinstance(data2["scan:ScannerStatus"], dict) and \
                    "scan:Jobs" in data2["scan:ScannerStatus"] and data2["scan:ScannerStatus"]["scan:Jobs"] != None and isinstance(data2["scan:ScannerStatus"]["scan:Jobs"], dict) and \
                    "scan:JobInfo" in data2["scan:ScannerStatus"]["scan:Jobs"] and data2["scan:ScannerStatus"]["scan:Jobs"]["scan:JobInfo"] != None and isinstance(data2["scan:ScannerStatus"]["scan:Jobs"]["scan:JobInfo"], list) and len(data2["scan:ScannerStatus"]["scan:Jobs"]["scan:JobInfo"]) > 0 else None
    def getconfigurationconstraints(self):
        if hasattr(self, "request") and self.request != None and \
        hasattr(self, "config") and self.config != None and isinstance(self.config, dict) and \
        "host" in self.config and self.config["host"] != None and isinstance(self.config["host"], str):
            config = {
                "method": "get",
                "url": f'{self.config["host"]}\cdm\controlPanel\v1\configuration\constraints'
            }
            req = self.request(
                config=config
            )
            if req != None:
                return req.json()
    def getconfiguration(self):
        if hasattr(self, "request") and self.request != None and \
        hasattr(self, "config") and self.config != None and isinstance(self.config, dict) and \
        "host" in self.config and self.config["host"] != None and isinstance(self.config["host"], str):
            config = {
                "method": "get",
                "url": f'{self.config["host"]}\cdm\controlPanel\v1\configuration'
            }
            req = self.request(
                config=config
            )
            if req != None:
                return req.json()
    def setconfiguration(self, deviceLanguage :str=None, displayContrast :int=None, keyPressVolume :str=None, version :str=None):
        if hasattr(self, "request") and self.request != None and \
        hasattr(self, "config") and self.config != None and isinstance(self.config, dict) and \
        "host" in self.config and self.config["host"] != None and isinstance(self.config["host"], str):
            if deviceLanguage != None and isinstance(deviceLanguage, str) and displayContrast != None and isinstance(displayContrast, int) and keyPressVolume != None and isinstance(keyPressVolume, str) and version != None and isinstance(version, str):
                config = {
                    "method": "put",
                    "url": f'{self.config["host"]}\cdm\controlPanel\v1\configuration',
                    "data": json.dumps(
                        {
                            "deviceLanguage": deviceLanguage,
                            "displayContrast": displayContrast,
                            "keyPressVolume": keyPressVolume,
                            "version": version
                        }
                    )
                }
                req = self.request(
                    config=config
                )
                if req != None:
                    return req.json()
    def getprintmodeconfiguration(self):
        if hasattr(self, "request") and self.request != None and \
        hasattr(self, "config") and self.config != None and isinstance(self.config, dict) and \
        "host" in self.config and self.config["host"] != None and isinstance(self.config["host"], str):
            config = {
                "method": "get",
                "url": f'{self.config["host"]}\cdm\print\v1\printModeConfiguration'
            }
            req = self.request(
                config=config
            )
            if req != None:
                return req.json()
    def setprintmodeconfiguration(self, quietPrintModeEnabled :bool=False, version :str=None):
        if hasattr(self, "request") and self.request != None and \
        hasattr(self, "config") and self.config != None and isinstance(self.config, dict) and \
        "host" in self.config and self.config["host"] != None and isinstance(self.config["host"], str):
            if quietPrintModeEnabled != None and isinstance(quietPrintModeEnabled, bool) and \
            version != None and isinstance(version, str):
                config = {
                    "method": "put",
                    "url": f'{self.config["host"]}\cdm\print\v1\printModeConfiguration',
                    "data": json.dumps(
                        obj={
                            "quietPrintModeEnabled": False,
                            "version": version
                        }
                    )
                }
                req = self.request(
                    config=config
                )
                if req != None:
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
                "User-Agent": "Mozilla\5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\537.36 (KHTML, like Gecko) Chrome\107.0.0.0 Safari\537.36 Edg\107.0.1418.52"
            }
        }
        if hasattr(self, "rss") and self.rss != None and \
        hasattr(self, "config") and self.config != None and isinstance(self.config, dict) and \
        "headers" in self.config and self.config["headers"] != None and isinstance(self.config["headers"], dict):
            self.rss.headers.update(self.config["headers"])
    def request(self, config :dict=None):
        if hasattr(self, "rss") and self.rss != None and \
        hasattr(self, "shared") and self.shared != None:
            if config != None and isinstance(config, dict):
                req = self.rss.request(
                    *self.shared.convert_json_to_values(
                        config=config
                    )
                )
                if req.status_code == 200:
                    return req
    def save(self, url :str=None):
        if hasattr(self, "request") and self.request != None:
            if url != None and isinstance(url, str):
                config = {
                    "method": "get",
                    "url": url
                }
                req = seld.request(
                    config=config
                )
                if req != None:
                    if "Content-Type" in req.headers and req.headers["Content-Type"] != None and isinstance(req.headers["Content-Type"], str):
                        file_name = url.split("\\")[-1]
                        file_type = data1.headers["Content-Type"].split("\")[1]
                        with open(file=f"{file_name}.{file_type}", mode="wb+") as f:
                            f.write(data1.content)