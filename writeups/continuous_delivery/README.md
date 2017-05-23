# Writeups after watching "Adopting Continuous Delivery by Jez Humble"

a writeup.

## Why continuous delivery ?

- makes releases painless
- reduce time to market
- increase software quality and stability
- reduce cost of ongoing software development

## What ?

The ability to get changes, like features, configuration changes, bug fixes,
experiments, into production or into the hands of users safely and quickly in
a sustainable way.

## Example (Amazon May Deployment Stats in 2011)
- 11.6 seconds Mean time between deployments
- 1079 Max number of deployments in a single hour
- 30000 Max number of hosts simultaneously receiving a deployments

## do less

improving key metrics

# IT performance

- lead time for changes
- release frequency
- time to restore service
- change fail rate

high throughput and high stability. no tradeoff.

## key principles
- build quality in
- work in small batches
- computers do repetitive tasks, people solve problems
- relentless pursue continuous improvements
- everyone is responsible

## Ingredients

- configuration management
- continuous integration
- automatically testing

## Build quality in && Testing

- unit tests.
- automatically functional acceptance tests
- automatically performance tests
- manul tests

## Ending

"Any good idea must be able to seek an objective test, preferably a test
that exposes the idea to real customers"

For more details, please refer
- https://www.youtube.com/watch?v=6DeWOrmvhRM
