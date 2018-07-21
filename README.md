# Explore-US-Bikeshare-Data
Use of Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington.
# Python Script to Explore US Bikeshare Data
This Python script is written for Project 1 of Udacity's Python Foundation Nanodegree program, and is used to explore data related to bike share systems for Chicago, New York, and Washington. It imports data from csv files and compute descriptive statistics from the data. It also takes in users' raw input to create an interactive experience in the terminal to present these statistics.

## How to run the script
You can run the script using a Python integrated development environment (IDE).

## Datasets
The datasets used for this script contain bike share data for the first six months of 2017. Some data wrangling has been performed by Udacity's staff before being provided to the students. Under the permission of Udacity,The file sizes are too big to be uploaded on GitHub, so they were uploaded on Google Drive instead. After downloading the datasets, place them in the same folder with this Python script.

The data is provided by [Motivate](https://www.motivateco.com/), which is a bike share system provider for many cities in the United States. The data files for all three cities contain the same six columns:
* Start Time
* End Time
* Trip Duration (in seconds)
* Start Station
* End Station
* User Type (Subscriber or Customer)

The Chicago and New York City files also contain the following two columns:
* Gender
* Birth Year

##Statistics Computed:--->


#1 Popular times of travel (i.e., occurs most often in the start time)

most common month
most common day of week
most common hour of day
#2 Popular stations and trip

most common start station
most common end station
most common trip from start to end (i.e., most frequent combination of start station and end station)
#3 Trip duration

total travel time
average travel time
#4 User info

counts of each user type
counts of each gender (only available for NYC and Chicago)
earliest, most recent, most common year of birth (only available for NYC and Chicago)


## Resources referred to complete this project:
I was getting this error!
https://stackoverflow.com/questions/10851906/python-3-unboundlocalerror-local-variable-referenced-before-assignment
Combine mutiple Columns of pandas Dataframe
https://stackoverflow.com/questions/39291499/how-to-concatenate-multiple-column-values-into-a-single-column-in-panda-datafram
To acces specific rows of DF
https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
