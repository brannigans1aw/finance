# finance

## Goals

We would like to make pretty graphs of contributions and expenditures for all candidates running for at large DC council in
2014. It would be awesome to have nice graphs of each candidate, showing who donated to their campaigns, whether they were corporations or indivuals, and how that has changed over time.

## Design

We seperate apps as much as possible, designing small tools that do one thing very well. This means that each part should
should articulate what specific action it does and no more. Then we can chain these tools together to get the results we
want. As much as possible, tools should be created as stand alone repos.

## Parts

1. **[finance-scraper](https://github.com/techforelissa/finance-scraper)**: Provide Python and CLI API to raw data from
   from [DC Office of Campaign finance](http://ocf.dc.gov/index.shtm)
2. **[finance-munger](https://github.com/techforelissa/finance-munger)**: scripts for munging data into shape.
3. **[finance-data](https://github.com/techforelissa/finance-data)**: where we put the data for graphing.
4. **[finance-display](https://github.com/techforelissa/finance-scraper)**: Front end one page site that visualizes
   the data.
