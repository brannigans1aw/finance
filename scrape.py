from __future__ import print_function
from __future__ import unicode_literals

import requests
import os
import sys

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

get_some_cookies_from_url = "http://www.ocf.dc.gov/serv/download.asp"
s.post(get_some_cookies_from_url, options)

download_url = 'http://www.ocf.dc.gov/serv/download_conexp.asp'
r = requests.post(download_url, options)

# raise error if not 200
r.raise_for_status()

session_expire_response = ('\r\n\t<script language="javascript">\r\n\t\talert'
                           '("Your Session is expired. Please try again");\r'
                           '\n\t\topener.location.href="/serv/download.asp";'
                           '\r\n\t\twindow.close();\r\n\t</script>\r\n')
if r.text == session_expire_response:
    print('Failed in retrieving ', file=sys.stderr)
else:
    print(r.text, end="")
