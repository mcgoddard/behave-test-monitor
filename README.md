# Monitoring behave tests

This is a simple example of monitoring behave tests in aggregate using an AWS Cloudwatch metric to identify broken/flaky tests.

## Purpose

You can just look at your test output from CI/run the tests many times locally right?! Well if your tests are expensive to run (either in time or compute) or the nature of the issues you are having can't be replicated locally you may want to capture statistics about them when they run as part of your pipeline. You could of course collect test files and aggregate somewhere, or do something like this to have the tests report into Cloudwatch automatically.

## Running this example

Run `pipenv install` to spin up a Python virtualenv and install the dependencies for this example.

Run `pipenv run behave` to execute the tests once, you will need AWS credentials for your account available in your environment with the `cloudwatch:PutMetricData`. Each run of the script will write 4 datapoints to a single custom metric.

Running the script multiple times over a few minutes can yield graphs like this:

![Average Test Failures CloudWatch Metrics graph](average_failures.png?raw=true "Average Failures")

## Improvements

This writes a single metric for each `behave` scenario run. Whilst fine for a toy example like this large test sets might benefit from storing up scenario results and writing in batch as CloudWatch charges by the API request (and has a fairly low transaction per second limit).

## Cleaning up

Just run `pipenv --rm` to remove the virtual environment when you are done.
