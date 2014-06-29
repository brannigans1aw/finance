# finance

## Goals

We want to apply the techniques and goals of the Sunlight Foundation and Follow the Money to DC politics. We will track contributions and expenditures for all candidates running for DC public office.  We plan to start small and grow organically as through projects that interest collaborators.

## Design

We will try to seperate apps as much as possible, designing small tools that do one thing very well. This means that each part should should articulate what specific action it does and no more. Then we can chain these tools together to get the results we want. As much as possible, tools should be created as stand alone repos.

## Parts

1. **[scraper](scraper)**: Provide Python and CLI API to raw data from
   from [DC Office of Campaign Finance](http://ocf.dc.gov/index.shtm)
2. **[munger](munger)**: scripts for munging data into shape.
3. **[data](data)**: where we put the data (like [contributions](https://github.com/codefordc/finance/blob/gh-pages/data/all_contributions_1999_current.csv) and [expenditures](/data/all_expenditures_1999_current.csv) and stuff for graphs)
4. **[display](scraper)**: The pieces that generate graphs and content for the front end.

## Branching

Our production branch is gh-pages. 
