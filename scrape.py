import requests
import os

s = requests.Session()

options = {
    "cboFilerType": "PCC",
    "txtFromDate": os.environ['FROM_DATE'],
    "optReportOption": os.environ['REPORT_TYPE'],
    "txtToDate": os.environ['TO_DATE'],
    "cboSort1": "agyname, ",
    "filing_year": "",
    "optFormat": "CSV",
}

options = 'cboFilerType=PCC&txtFromDate=01%2F01%2F2014&txtToDate=01%2F01%2F9999&optReportOption=con&cboSort1=agyname&cboSort1=&filing_year=&optFormat=CSV'

get_some_cookies_from_url = "http://www.ocf.dc.gov/serv/download.asp"
s.post(get_some_cookies_from_url, options)

download_url = 'http://www.ocf.dc.gov/serv/download_conexp.asp'
r = requests.post(download_url, options, )#cookies={'ASPSESSIONIDSSSABCTT': 'EFHANGHCEIMEKGNJBEPBAOIP'})

print r.text,
