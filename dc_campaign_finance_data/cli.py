from __future__ import unicode_literals

import click
import json
import datetime

from . import scraper


@click.group()
def cli(**kwargs):
    pass


@cli.command(short_help='List of records (CSV)')
@click.option('--from-date', default='01/01/' + str(datetime.datetime.now().year),
              help='First date of records.', show_default=True)
@click.option('--to-date', default='01/01/9999',
              help='Last date of records. Future dates are allowed.',
              show_default=True)
@click.option('--report-type',
              default='con',
              help='The type of report. (exp -> expenses, con -> contributions)',
              type=click.Choice(['exp', 'con']),
              show_default=True)
def records(**kwargs):
    '''
    A list all transactions for all campaigns, between FROM-DATE and TO-DATE.
    Either the expenses of the campaign or the contributions of the
    campaign, based on REPORT-TYPE.
    '''
    click.echo(
        scraper.records_csv(**kwargs),
        nl=False
    )


@cli.command(short_help='Possible years (JSON)')
def years():
    '''
    Years in which there are records kept of campaign finances. (JSON)
    '''
    click.echo(
        json.dumps(scraper.available_years()),
        nl=False
    )


@cli.command(short_help='Possible offices (JSON)')
def offices():
    '''
    Offices for DC which are tracked. (JSON)
    '''
    click.echo(
        json.dumps(scraper.offices()),
        nl=False
    )



if __name__ == '__main__':
    cli()
