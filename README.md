# finance

## Goals

We want to apply the techniques and goals of the Sunlight Foundation and Follow the Money to DC politics. We will track contributions and expenditures for all candidates running for DC public office.  We plan to start small and grow organically as through projects that interest collaborators.

## Design

We will try to separate apps, so  that each part does one specific action and no more. The apps should then chain together to get the results we want. 

## Parts

1. **[scraper](scraper)**: Provide Python and CLI API to raw data from
   from [DC Office of Campaign Finance](http://ocf.dc.gov/index.shtm)
2. **[munger](munger)**: Scripts for munging data into shape.
3. **[data](data)**: Where we put scraped data (like [contributions](/data/input/all_contributions_1999_current.csv) and [expenditures](/data/input/all_expenditures_1999_current.csv) as well as processed data for graphing)
4. **[display](scraper)**: The pieces that generate graphs and content for the front end.

## Branching

Our production branch is gh-pages. 
