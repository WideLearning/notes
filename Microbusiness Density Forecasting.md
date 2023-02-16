# Microbusiness Density Forecasting
From [[Kaggle competitions]], [link](https://www.kaggle.com/competitions/godaddy-microbusiness-density-forecasting/)
$\physics$
## Available data
### Overview
We are given many timeseries of length 39 given in the train dataset and need to predict the next 8 values for each. 

### Given files
`train.csv`
- `row_id`
- `cfips`
- `county`
- `state`
- `first_day_of_month`
- `microbusiness_density`
- `active`
Here `row_id` has format `{cfips}_{first_day_of_month}`, `cfips` is an integer in $[1, 56045]$ corresponding to `county` and `state` in a strange way (see below), `first_day_of_month` has format `YYYY-MM-01`, `microbusiness_density` is a target real variable, and `active` is another integer feature. The time interval covered is from August’19 to October’22.

`test.csv`
- `row_id`
- `cfips`
- `first_day_of_month`
Columns mean the same as in `train.csv`, time interval here is from November’22 to June’23.

`sample_submission.csv`
- `row_id`
- `microbusiness_density`

`census_starter.csv`
Some annual statistics for each county.

### How `cfips` works
![[counties.png]]
The first two numbers represent state and the last three represent county. But as can be seen here, the same county can have different three-digit representations when in different states, it corresponds to its place among other counties of that state in lexicographical order.

### Online sources
Listed in competition description:
- https://www.godaddy.com/ventureforward/explore-the-data/?section=survey&cfips=6073
- https://data.census.gov/