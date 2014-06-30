# finance

## Goals

This project embraces the goals and techniques of the Sunlight Foundation and Follow the Money, and it aims to applly them to DC politics. It will track contributions and expenditures for all candidates running for DC public office.  We plan to start small and grow organically as through projects that interest collaborators.

## Design

Our approach will try to separate apps, so that each part does one specific action and no more. The apps should then chain together to get the results we want. 

## Parts

1. **[scraper](scraper)**: Provide Python and CLI API to raw data from
   from [DC Office of Campaign Finance](http://ocf.dc.gov/index.shtm)
2. **[munger](munger)**: Scripts for munging data into shape.
3. **[data](data)**: Where we put scraped data (like [contributions](/data/input/all_contributions_1999_current.csv) and [expenditures](/data/input/all_expenditures_1999_current.csv) as well as processed data for graphing)
4. **[display](scraper)**: The pieces that generate graphs and content for the front end.

## Branching

Our production branch is gh-pages. For now, our dev branch is master. 
