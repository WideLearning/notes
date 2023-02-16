# Microbusiness Density Forecasting
From [[Kaggle competitions]]
$\physics$
## Available data
### Given files
`train.csv`
- `row_id`
- `cfips`
- `county`
- `state`
- `first_day_of_month`
- `microbusiness_density`
- `active`
Here `row_id` has form `{cfips}_{first_day_of_month}`, `cfips` is an integer in $[1, 56045]$ corresponding to `county` and `state` in a strange way (see below).

`test.csv`
- `row_id`
- `cfips`
- `first_day_of_month`

`sample_submission.csv`
- `row_id`
- `microbusiness_density`

`census_starter.csv`
Some annual statistics for each county.

### How `cfips` works
![[counties.png]]