# finance

## Goals

This project aims to apply the goals and techniques of the Sunlight Foundation and Follow the Money to DC politics. It will track contributions and expenditures for all candidates running for DC public office.  We plan to start small and grow organically as through projects that interest collaborators.

## Design

Our approach will try to separate apps, so that each part does one specific action and no more. The apps should then chain together to get the results we want. 

## Parts

1. **[scraper](scraper)**: Provide Python and CLI API to raw data from
   from [DC Office of Campaign Finance](http://ocf.dc.gov/index.shtm)
2. **[munger](munger)**: Scripts for munging data into shape.
3. **[data](data)**: Where we put scraped data (like [contributions](/data/input/all_contributions_1999_current.csv) and [expenditures](/data/input/all_expenditures_1999_current.csv)) and [output data](/data/output) processed for graphing (mostly json files).
4. **[display](scraper)**: The pieces that generate graphs and content for the front end.

## Branching

Our production branch is gh-pages. For now, our dev branch is master. 


## Issues
For current issues we are working on check out the [waffle.io board](https://waffle.io/codefordc/finance), which uses our [Github issues](https://github.com/codefordc/finance/issues) underneath.
