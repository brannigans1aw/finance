from __future__ import print_function
from __future__ import unicode_literals

import requests
import click


def get_csv(from_date, to_date, report_type):
    options = {
        "cboFilerType": "PCC",
        "txtFromDate": from_date,
        "txtToDate": to_date,
        "optReportOption": report_type,
        "cboSort1": "agyname, ",
        "filing_year": "",
        "optFormat": "CSV",
    }

    get_some_cookies_from_url = "http://www.ocf.dc.gov/serv/download.asp"

    s = requests.Session()

    s.post(get_some_cookies_from_url, options).raise_for_status()

    download_url = 'http://www.ocf.dc.gov/serv/download_conexp.asp'
    r = s.post(download_url, options)
    r.raise_for_status()

    return r.text

@click.command()
@click.option('--from-date', default='01/01/2014', help='First date of records.')
@click.option('--to-date', default='01/01/9999',
              help='Last date of records. Future dates are allowed.')
@click.option('--report-type',
              default='con',
              help='The type of report. (exp -> expenses, con -> contributions)',
              type=click.Choice(['exp', 'con']))
def cli(**kwargs):
    click.echo(get_csv(**kwargs), nl=False)

if __name__ == '__main__':
    cli()
