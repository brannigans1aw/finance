# finance

## Goals

We would like to make pretty graphs of contributions and expenditures for all candidates running for at large DC council in
2014. It would be awesome to have nice graphs of each candidate, showing who donated to their campaigns, whether they were corporations or indivuals, and how that has changed over time.

## Design

We seperate apps as much as possible, designing small tools that do one thing very well. This means that each part should
should articulate what specific action it does and no more. Then we can chain these tools together to get the results we
want. As much as possible, tools should be created as stand alone repos.

## Parts

### Get Data

First we need to grab all the data and plop it into a `.csv` file. It should be one contribution per row, specifying
everything we need about it, including date, amount, donator, and recipient. 
This is at [techforelissa/finance-scraper](https://github.com/techforelissa/finance-scraper).

### Host Data

Then we need to put that data we have downloaded, somewhere easy to host. One option is a VCS file, but this isn't ideal because it ties our code to our data. It would be better to host it on some external place.

This code is at [techforelissa/finance-scraper-pusher](https://github.com/techforelissa/finance-scraper-pusher)

#### Options

[datahub.io](http://datahub.io/)
[socrata](http://www.socrata.com/)
[OpenData DC](http://www.opendatadc.org/)

We have decided to use OpenData DC.

### Graph Data

Finally we need some JS probably to parse that data and make some pretty interactive graphs out of it. This will be [techforelissa/finance-viewer](https://github.com/techforelissa/finance-viewer).
