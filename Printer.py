import requests
import json
import xmltodict
import base64

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
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52"
            }
        }
        if username != None and isinstance(username, str) and password != None and isinstance(password, str):
            self.config["headers"]["Authorization"] = f"Basic {base64.b64encode(f'{username}:{password}'.encode()).decode()}"
        self.rss.headers.update(self.config["headers"])
    def authcheck(self):
        #https://192.168.1.3/AuthChk
        pass
    def scan(self):
        config = {
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
            )
        }
        config1 = {
            "method": "get",
            "url": f'{self.config["host"]}/eSCL/ScannerStatus'
        }
        if data1 != None and isinstance(data1, str):
            data2 = xmltodict.parse(xml_input=data1)
            if data2 != None and isinstance(data2, dict):
                if "scan:ScannerStatus" in data2 and data2["scan:ScannerStatus"] != None and isinstance(data2["scan:ScannerStatus"], dict) and "scan:Jobs" in data2["scan:ScannerStatus"] and data2["scan:ScannerStatus"]["scan:Jobs"] != None and isinstance(data2["scan:ScannerStatus"]["scan:Jobs"], dict) and "scan:JobInfo" in data2["scan:ScannerStatus"]["scan:Jobs"] and data2["scan:ScannerStatus"]["scan:Jobs"]["scan:JobInfo"] != None and isinstance(data2["scan:ScannerStatus"]["scan:Jobs"]["scan:JobInfo"], list) and len(data2["scan:ScannerStatus"]["scan:Jobs"]["scan:JobInfo"]) > 0 and "pwg:JobUuid" in data2["scan:ScannerStatus"]["scan:Jobs"]["scan:JobInfo"][0] and data2["scan:ScannerStatus"]["scan:Jobs"]["scan:JobInfo"][0]["pwg:JobUuid"] != None and isinstance(data2["scan:ScannerStatus"]["scan:Jobs"]["scan:JobInfo"][0]["pwg:JobUuid"], str):
                    return f'{self.config["host"]}/eSCL/ScanJobs/{data2["scan:ScannerStatus"]["scan:Jobs"]["scan:JobInfo"][0]["pwg:JobUuid"]}/NextDocument'
    def getconfigurationconstraints(self):
        #needs fixing (filter data and put em in order)
        config = {
            "method": "get",
            "url": f'{self.config["host"]}/cdm/controlPanel/v1/configuration/constraints'
        }
        if data != None and isinstance(data, dict):
            return data
    def getconfiguration(self):
        config = {
            "method": "get",
            "url": f'{self.config["host"]}/cdm/controlPanel/v1/configuration'
        }
    def setconfiguration(self, deviceLanguage :str=None, displayContrast :int=None, keyPressVolume :str=None, version :str=None):
        #need fixing (check for valid parameters)
        if deviceLanguage != None and isinstance(deviceLanguage, str) and displayContrast != None and isinstance(displayContrast, int) and keyPressVolume != None and isinstance(keyPressVolume, str) and version != None and isinstance(version, str):
            config = {
                "method": "put",
                "url": f'{self.config["host"]}/cdm/controlPanel/v1/configuration',
                "data": json.dumps(
                    {
                        "deviceLanguage": deviceLanguage,
                        "displayContrast": displayContrast,
                        "keyPressVolume": keyPressVolume,
                        "version": version
                    }
                )
            }
    def getprintmodeconfiguration(self):
        config = {
            "method": "get",
            "url": f'{self.config["host"]}/cdm/print/v1/printModeConfiguration'
        }
    def setprintmodeconfiguration(self, quietPrintModeEnabled :bool=False, version :str=None):
        #need fixing (check for valid parameters)
        if quietPrintModeEnabled != None and isinstance(quietPrintModeEnabled, bool) and version != None and isinstance(version, str):
            config = {
                "method": "put",
                "url": f'{self.config["host"]}/cdm/print/v1/printModeConfiguration',
                "data": json.dumps(
                    obj={
                        "quietPrintModeEnabled": False,
                        "version": version
                    }
                ),
                    "aftermethod": "re"
            }

class Scan:
    def __init__(self):
        with requests.Session() as rss:
            self.rss = rss
        self.shared = shared.Shared(
            rss=self.rss
        )
        self.config = {
            "headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52"
            }
        }
        self.rss.headers.update(self.config.headers)
    def save(self, url :str=None):
        if url != None and isinstance(url, str):
            config = {
                "method": "get",
                "url": url
            }
            if data1 != None and "Content-Type" in data1.headers and data1.headers["Content-Type"] != None and isinstance(data1.headers["Content-Type"], str):
                file_name = url.split("/")[-1]
                file_type = data1.headers["Content-Type"].split("/")[1]
                with open(file=f"{file_name}.{file_type}", mode="wb+") as f:
                    f.write(data1.content)