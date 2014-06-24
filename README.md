# finance

## Goals

We want to apply the techniques and goals of the Sunlight Foundation and Follow the Money to DC politics. We will track contributions and expenditures for all candidates running for DC public office.  We plan to start small and grow organically as through projects that interest collaborators. 

## Design

We will try to seperate apps as much as possible, designing small tools that do one thing very well. This means that each part should should articulate what specific action it does and no more. Then we can chain these tools together to get the results we want. As much as possible, tools should be created as stand alone repos. 

## Parts

1. **[finance-scraper](https://github.com/techforelissa/finance-scraper)**: Provide Python and CLI API to raw data from
   from [DC Office of Campaign finance](http://ocf.dc.gov/index.shtm)
2. **[finance-munger](https://github.com/techforelissa/finance-munger)**: scripts for munging data into shape.
3. **[finance-data](https://github.com/techforelissa/finance-data)**: where we put the data for graphing.
4. **[finance-display](https://github.com/techforelissa/finance-scraper)**: Front end one page site that visualizes
   the data.
