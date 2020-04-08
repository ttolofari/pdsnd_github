{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 2016 US Bike Share Activity Snapshot\n",
    "\n",
    "## Table of Contents\n",
    "- [Introduction](#intro)\n",
    "- [Posing Questions](#pose_questions)\n",
    "- [Data Collection and Wrangling](#wrangling)\n",
    "  - [Condensing the Trip Data](#condensing)\n",
    "- [Exploratory Data Analysis](#eda)\n",
    "  - [Statistics](#statistics)\n",
    "  - [Visualizations](#visualizations)\n",
    "- [Performing Your Own Analysis](#eda_continued)\n",
    "- [Conclusions](#conclusions)\n",
    "\n",
    "<a id='intro'></a>\n",
    "## Introduction\n",
    "\n",
    "> **Tip**: Quoted sections like this will provide helpful instructions on how to navigate and use a Jupyter notebook.\n",
    "\n",
    "Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles for short trips, typically 30 minutes or less. Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.\n",
    "\n",
    "In this project, you will perform an exploratory analysis on data provided by [Motivate](https://www.motivateco.com/), a bike-share system provider for many major cities in the United States. You will compare the system usage between three large cities: New York City, Chicago, and Washington, DC. You will also see if there are any differences within each system for those users that are registered, regular users and those users that are short-term, casual users."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='pose_questions'></a>\n",
    "## Posing Questions\n",
    "\n",
    "Before looking at the bike sharing data, you should start by asking questions you might want to understand about the bike share data. Consider, for example, if you were working for Motivate. What kinds of information would you want to know about in order to make smarter business decisions? If you were a user of the bike-share service, what factors might influence how you would want to use the service?\n",
    "\n",
    "**Question 1**: Write at least two questions related to bike sharing that you think could be answered by data.\n",
    "\n",
    "**Answer - Q1**: What is the trend of rides by month?\n",
    "\n",
    "**Answer - Q2**: What is the number of rides by user type by day of week?\n",
    "\n",
    "> **Tip**: If you double click on this cell, you will see the text change so that all of the formatting is removed. This allows you to edit this block of text. This block of text is written using [Markdown](http://daringfireball.net/projects/markdown/syntax), which is a way to format text using headers, links, italics, and many other options using a plain-text syntax. You will also use Markdown later in the Nanodegree program. Use **Shift** + **Enter** or **Shift** + **Return** to run the cell and show its rendered form."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='wrangling'></a>\n",
    "## Data Collection and Wrangling\n",
    "\n",
    "Now it's time to collect and explore our data. In this project, we will focus on the record of individual trips taken in 2016 from our selected cities: New York City, Chicago, and Washington, DC. Each of these cities has a page where we can freely download the trip data.:\n",
    "\n",
    "- New York City (Citi Bike): [Link](https://www.citibikenyc.com/system-data)\n",
    "- Chicago (Divvy): [Link](https://www.divvybikes.com/system-data)\n",
    "- Washington, DC (Capital Bikeshare): [Link](https://www.capitalbikeshare.com/system-data)\n",
    "\n",
    "If you visit these pages, you will notice that each city has a different way of delivering its data. Chicago updates with new data twice a year, Washington DC is quarterly, and New York City is monthly. **However, you do not need to download the data yourself.** The data has already been collected for you in the `/data/` folder of the project files. While the original data for 2016 is spread among multiple files for each city, the files in the `/data/` folder collect all of the trip data for the year into one file per city. Some data wrangling of inconsistencies in timestamp format within each city has already been performed for you. In addition, a random 2% sample of the original data is taken to make the exploration more manageable. \n",
    "\n",
    "**Question 2**: However, there is still a lot of data for us to investigate, so it's a good idea to start off by looking at one entry from each of the cities we're going to analyze. Run the first code cell below to load some packages and functions that you'll be using in your analysis. Then, complete the second code cell to print out the first trip recorded from each of the cities (the second line of each data file).\n",
    "\n",
    "> **Tip**: You can run a code cell like you formatted Markdown cells above by clicking on the cell and using the keyboard shortcut **Shift** + **Enter** or **Shift** + **Return**. Alternatively, a code cell can be executed using the **Play** button in the toolbar after selecting it. While the cell is running, you will see an asterisk in the message to the left of the cell, i.e. `In [*]:`. The asterisk will change into a number to show that execution has completed, e.g. `In [1]`. If there is output, it will show up as `Out [1]:`, with an appropriate number to match the \"In\" number."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "## import all necessary packages and functions.\n",
    "import csv # read and write csv files\n",
    "from datetime import datetime # operations to parse dates\n",
    "from pprint import pprint # use to print data structures like dictionaries in\n",
    "                          # a nicer way than the base print function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "City: NYC\n",
      "OrderedDict([('tripduration', '839'),\n",
      "             ('starttime', '1/1/2016 00:09:55'),\n",
      "             ('stoptime', '1/1/2016 00:23:54'),\n",
      "             ('start station id', '532'),\n",
      "             ('start station name', 'S 5 Pl & S 4 St'),\n",
      "             ('start station latitude', '40.710451'),\n",
      "             ('start station longitude', '-73.960876'),\n",
      "             ('end station id', '401'),\n",
      "             ('end station name', 'Allen St & Rivington St'),\n",
      "             ('end station latitude', '40.72019576'),\n",
      "             ('end station longitude', '-73.98997825'),\n",
      "             ('bikeid', '17109'),\n",
      "             ('usertype', 'Customer'),\n",
      "             ('birth year', ''),\n",
      "             ('gender', '0')])\n",
      "\n",
      "City: Chicago\n",
      "OrderedDict([('trip_id', '9080545'),\n",
      "             ('starttime', '3/31/2016 23:30'),\n",
      "             ('stoptime', '3/31/2016 23:46'),\n",
      "             ('bikeid', '2295'),\n",
      "             ('tripduration', '926'),\n",
      "             ('from_station_id', '156'),\n",
      "             ('from_station_name', 'Clark St & Wellington Ave'),\n",
      "             ('to_station_id', '166'),\n",
      "             ('to_station_name', 'Ashland Ave & Wrightwood Ave'),\n",
      "             ('usertype', 'Subscriber'),\n",
      "             ('gender', 'Male'),\n",
      "             ('birthyear', '1990')])\n",
      "\n",
      "City: Washington\n",
      "OrderedDict([('Duration (ms)', '427387'),\n",
      "             ('Start date', '3/31/2016 22:57'),\n",
      "             ('End date', '3/31/2016 23:04'),\n",
      "             ('Start station number', '31602'),\n",
      "             ('Start station', 'Park Rd & Holmead Pl NW'),\n",
      "             ('End station number', '31207'),\n",
      "             ('End station', 'Georgia Ave and Fairmont St NW'),\n",
      "             ('Bike number', 'W20842'),\n",
      "             ('Member Type', 'Registered')])\n"
     ]
    }
   ],
   "source": [
    "def print_first_point(filename):\n",
    "    \"\"\"\n",
    "    This function prints and returns the first data point (second row) from\n",
    "    a csv file that includes a header row.\n",
    "    \"\"\"\n",
    "    # print city name for reference\n",
    "    city = filename.split('-')[0].split('/')[-1]\n",
    "    print('\\nCity: {}'.format(city))\n",
    "    \n",
    "    with open(filename, 'r') as f_in:\n",
    "        ## TODO: Use the csv library to set up a DictReader object. ##\n",
    "        ## see https://docs.python.org/3/library/csv.html           ##\n",
    "        trip_reader = csv.DictReader(f_in)\n",
    "        \n",
    "        ## TODO: Use a function on the DictReader object to read the     ##\n",
    "        ## first trip from the data file and store it in a variable.     ##\n",
    "        ## see https://docs.python.org/3/library/csv.html#reader-objects ##\n",
    "        \n",
    "        first_trip = next(trip_reader)\n",
    "        \n",
    "        ## TODO: Use the pprint library to print the first trip. ##\n",
    "        ## see https://docs.python.org/3/library/pprint.html     ##\n",
    "        \n",
    "        pprint(first_trip)\n",
    "        \n",
    "    # output city name and first trip for later testing\n",
    "    return (city, first_trip)\n",
    "\n",
    "# list of files for each city\n",
    "data_files = ['./data/NYC-CitiBike-2016.csv',\n",
    "              './data/Chicago-Divvy-2016.csv',\n",
    "              './data/Washington-CapitalBikeshare-2016.csv',]\n",
    "\n",
    "# print the first trip from each file, store in dictionary\n",
    "example_trips = {}\n",
    "for data_file in data_files:\n",
    "    city, first_trip = print_first_point(data_file)\n",
    "    example_trips[city] = first_trip"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If everything has been filled out correctly, you should see below the printout of each city name (which has been parsed from the data file name) that the first trip has been parsed in the form of a dictionary. When you set up a `DictReader` object, the first row of the data file is normally interpreted as column names. Every other row in the data file will use those column names as keys, as a dictionary is generated for each row.\n",
    "\n",
    "This will be useful since we can refer to quantities by an easily-understandable label instead of just a numeric index. For example, if we have a trip stored in the variable `row`, then we would rather get the trip duration from `row['duration']` instead of `row[0]`.\n",
    "\n",
    "<a id='condensing'></a>\n",
    "### Condensing the Trip Data\n",
    "\n",
    "It should also be observable from the above printout that each city provides different information. Even where the information is the same, the column names and formats are sometimes different. To make things as simple as possible when we get to the actual exploration, we should trim and clean the data. Cleaning the data makes sure that the data formats across the cities are consistent, while trimming focuses only on the parts of the data we are most interested in to make the exploration easier to work with.\n",
    "\n",
    "You will generate new data files with five values of interest for each trip: trip duration, starting month, starting hour, day of the week, and user type. Each of these may require additional wrangling depending on the city:\n",
    "\n",
    "- **Duration**: This has been given to us in seconds (New York, Chicago) or milliseconds (Washington). A more natural unit of analysis will be if all the trip durations are given in terms of minutes.\n",
    "- **Month**, **Hour**, **Day of Week**: Ridership volume is likely to change based on the season, time of day, and whether it is a weekday or weekend. Use the start time of the trip to obtain these values. The New York City data includes the seconds in their timestamps, while Washington and Chicago do not. The [`datetime`](https://docs.python.org/3/library/datetime.html) package will be very useful here to make the needed conversions.\n",
    "- **User Type**: It is possible that users who are subscribed to a bike-share system will have different patterns of use compared to users who only have temporary passes. Washington divides its users into two types: 'Registered' for users with annual, monthly, and other longer-term subscriptions, and 'Casual', for users with 24-hour, 3-day, and other short-term passes. The New York and Chicago data uses 'Subscriber' and 'Customer' for these groups, respectively. For consistency, you will convert the Washington labels to match the other two.\n",
    "\n",
    "\n",
    "**Question 3a**: Complete the helper functions in the code cells below to address each of the cleaning tasks described above."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "def duration_in_mins(datum, city):\n",
    "    \"\"\"\n",
    "    Takes as input a dictionary containing info about a single trip (datum) and\n",
    "    its origin city (city) and returns the trip duration in units of minutes.\n",
    "    \n",
    "    Remember that Washington is in terms of milliseconds while Chicago and NYC\n",
    "    are in terms of seconds. \n",
    "    \n",
    "    HINT: The csv module reads in all of the data as strings, including numeric\n",
    "    values. You will need a function to convert the strings into an appropriate\n",
    "    numeric type when making your transformations.\n",
    "    see https://docs.python.org/3/library/functions.html\n",
    "    \"\"\"\n",
    "\n",
    "    # YOUR CODE HERE\n",
    "    if city == 'NYC' or city == 'Chicago':\n",
    "        duration = int(datum['tripduration'])/60\n",
    "    else:\n",
    "        duration = int(datum['Duration (ms)'])/(1000*60)\n",
    "    \n",
    "    return duration\n",
    "    \"\"\"\"\n",
    "    Converting milliseconds and seconds to minutes.\n",
    "    \"\"\"\n",
    "\n",
    "# Some tests to check that your code works. There should be no output if all of\n",
    "# the assertions pass. The `example_trips` dictionary was obtained from when\n",
    "# you printed the first trip from each of the original data files.\n",
    "tests = {'NYC': 13.9833,\n",
    "         'Chicago': 15.4333,\n",
    "         'Washington': 7.1231}\n",
    "\n",
    "for city in tests:\n",
    "    assert abs(duration_in_mins(example_trips[city], city) - tests[city]) < .001"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def time_of_trip(datum, city):\n",
    "    \"\"\"\n",
    "    Takes as input a dictionary containing info about a single trip (datum) and\n",
    "    its origin city (city) and returns the month, hour, and day of the week in\n",
    "    which the trip was made.\n",
    "    \n",
    "    Remember that NYC includes seconds, while Washington and Chicago do not.\n",
    "    \n",
    "    HINT: You should use the datetime module to parse the original date\n",
    "    strings into a format that is useful for extracting the desired information.\n",
    "    see https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior\n",
    "    \"\"\"\n",
    "    \n",
    "    # YOUR CODE HERE\n",
    "    \n",
    "    \n",
    "    \"\"\"\n",
    "    Converting the starttime to return the month, hour and day of the week.\n",
    "    \"\"\"\n",
    "        \n",
    "    if city =='NYC':\n",
    "        startdate = datetime.strptime((datum['starttime']), '%m/%d/%Y %H:%M:%S') \n",
    "        month = int(startdate.strftime(\"%m\"))\n",
    "        hour = int(startdate.strftime(\"%H\"))\n",
    "        day_of_week = startdate.strftime(\"%A\")\n",
    "        \n",
    "    elif city =='Chicago':\n",
    "        startdate = datetime.strptime((datum['starttime']), '%m/%d/%Y %H:%M') \n",
    "        month = int(startdate.strftime(\"%m\"))\n",
    "        hour = int(startdate.strftime(\"%H\"))\n",
    "        day_of_week = startdate.strftime(\"%A\")\n",
    "        \n",
    "    else:\n",
    "        startdate = datetime.strptime((datum['Start date']), '%m/%d/%Y %H:%M') \n",
    "        month = int(startdate.strftime(\"%m\"))\n",
    "        hour = int(startdate.strftime(\"%H\"))\n",
    "        day_of_week = startdate.strftime(\"%A\")\n",
    "    \n",
    "    \n",
    "    return (month, hour, day_of_week)\n",
    "\n",
    "\n",
    "# Some tests to check that your code works. There should be no output if all of\n",
    "# the assertions pass. The `example_trips` dictionary was obtained from when\n",
    "# you printed the first trip from each of the original data files.\n",
    "tests = {'NYC': (1, 0, 'Friday'),\n",
    "         'Chicago': (3, 23, 'Thursday'),\n",
    "         'Washington': (3, 22, 'Thursday')}\n",
    "\n",
    "for city in tests:\n",
    "    assert time_of_trip(example_trips[city], city) == tests[city]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "def type_of_user(datum, city):\n",
    "    \"\"\"\n",
    "    Takes as input a dictionary containing info about a single trip (datum) and\n",
    "    its origin city (city) and returns the type of system user that made the\n",
    "    trip.\n",
    "    \n",
    "    Remember that Washington has different category names compared to Chicago\n",
    "    and NYC. \n",
    "    \"\"\"\n",
    "    \n",
    "    # YOUR CODE HERE\n",
    "    \"\"\"\n",
    "    Converting the type of the system user to match with the data in all the cities.\n",
    "    \"\"\"\n",
    "    if city == 'NYC' or city == 'Chicago':\n",
    "        user_type = datum['usertype']\n",
    "    else:\n",
    "        if datum['Member Type'] == 'Registered':\n",
    "            user_type = 'Subscriber'\n",
    "        elif datum['Member Type'] == 'Casual':\n",
    "            user_type = 'Customer'\n",
    "    \n",
    "    return user_type\n",
    "    \n",
    "\n",
    "# Some tests to check that your code works. There should be no output if all of\n",
    "# the assertions pass. The `example_trips` dictionary was obtained from when\n",
    "# you printed the first trip from each of the original data files.\n",
    "tests = {'NYC': 'Customer',\n",
    "         'Chicago': 'Subscriber',\n",
    "         'Washington': 'Subscriber'}\n",
    "\n",
    "for city in tests:\n",
    "    assert type_of_user(example_trips[city], city) == tests[city]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Question 3b**: Now, use the helper functions you wrote above to create a condensed data file for each city consisting only of the data fields indicated above. In the `/examples/` folder, you will see an example datafile from the [Bay Area Bike Share](http://www.bayareabikeshare.com/open-data) before and after conversion. Make sure that your output is formatted to be consistent with the example file."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "def condense_data(in_file, out_file, city):\n",
    "    \"\"\"\n",
    "    This function takes full data from the specified input file\n",
    "    and writes the condensed data to a specified output file. The city\n",
    "    argument determines how the input file will be parsed.\n",
    "    \n",
    "    HINT: See the cell below to see how the arguments are structured!\n",
    "    \"\"\"\n",
    "    \n",
    "    with open(out_file, 'w') as f_out, open(in_file, 'r') as f_in:\n",
    "        # set up csv DictWriter object - writer requires column names for the\n",
    "        # first row as the \"fieldnames\" argument\n",
    "        out_colnames = ['duration', 'month', 'hour', 'day_of_week', 'user_type']        \n",
    "        trip_writer = csv.DictWriter(f_out, fieldnames = out_colnames)\n",
    "        trip_writer.writeheader()\n",
    "        \n",
    "        ## TODO: set up csv DictReader object ##\n",
    "        trip_reader = csv.DictReader(f_in)\n",
    "\n",
    "        # collect data from and process each row\n",
    "        for row in trip_reader:\n",
    "            # set up a dictionary to hold the values for the cleaned and trimmed\n",
    "            # data point\n",
    "            new_point = {}\n",
    "\n",
    "            ## TODO: use the helper functions to get the cleaned data from  ##\n",
    "            ## the original data dictionaries.                              ##\n",
    "            ## Note that the keys for the new_point dictionary should match ##\n",
    "            ## the column names set in the DictWriter object above.         ##\n",
    "            new_point['duration'] = duration_in_mins(row,city)\n",
    "            new_point['month']=  time_of_trip(row,city)[0]\n",
    "            new_point['hour'] = time_of_trip(row,city)[1]\n",
    "            new_point['day_of_week'] = time_of_trip(row,city)[2]\n",
    "            new_point['user_type'] = type_of_user(row,city)\n",
    "\n",
    "            ## TODO: write the processed information to the output file.     ##\n",
    "            ## see https://docs.python.org/3/library/csv.html#writer-objects ##\n",
    "            trip_writer.writerow(new_point)           "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "City: Washington\n",
      "OrderedDict([('duration', '7.123116666666666'),\n",
      "             ('month', '3'),\n",
      "             ('hour', '22'),\n",
      "             ('day_of_week', 'Thursday'),\n",
      "             ('user_type', 'Subscriber')])\n",
      "\n",
      "City: Chicago\n",
      "OrderedDict([('duration', '15.433333333333334'),\n",
      "             ('month', '3'),\n",
      "             ('hour', '23'),\n",
      "             ('day_of_week', 'Thursday'),\n",
      "             ('user_type', 'Subscriber')])\n",
      "\n",
      "City: NYC\n",
      "OrderedDict([('duration', '13.983333333333333'),\n",
      "             ('month', '1'),\n",
      "             ('hour', '0'),\n",
      "             ('day_of_week', 'Friday'),\n",
      "             ('user_type', 'Customer')])\n"
     ]
    }
   ],
   "source": [
    "# Run this cell to check your work\n",
    "city_info = {'Washington': {'in_file': './data/Washington-CapitalBikeshare-2016.csv',\n",
    "                            'out_file': './data/Washington-2016-Summary.csv'},\n",
    "             'Chicago': {'in_file': './data/Chicago-Divvy-2016.csv',\n",
    "                         'out_file': './data/Chicago-2016-Summary.csv'},\n",
    "             'NYC': {'in_file': './data/NYC-CitiBike-2016.csv',\n",
    "                     'out_file': './data/NYC-2016-Summary.csv'}}\n",
    "\n",
    "\"\"\" \n",
    "Creating an output file from data in the input file.\n",
    "\"\"\"\n",
    "\n",
    "for city, filenames in city_info.items():\n",
    "    condense_data(filenames['in_file'], filenames['out_file'], city)\n",
    "    print_first_point(filenames['out_file'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Tip**: If you save a jupyter Notebook, the output from running code blocks will also be saved. However, the state of your workspace will be reset once a new session is started. Make sure that you run all of the necessary code blocks from your previous session to reestablish variables and functions before picking up where you last left off.\n",
    "\n",
    "<a id='eda'></a>\n",
    "## Exploratory Data Analysis\n",
    "\n",
    "Now that you have the data collected and wrangled, you're ready to start exploring the data. In this section you will write some code to compute descriptive statistics from the data. You will also be introduced to the `matplotlib` library to create some basic histograms of the data.\n",
    "\n",
    "<a id='statistics'></a>\n",
    "### Statistics\n",
    "\n",
    "First, let's compute some basic counts. The first cell below contains a function that uses the csv module to iterate through a provided data file, returning the number of trips made by subscribers and customers. The second cell runs this function on the example Bay Area data in the `/examples/` folder. Modify the cells to answer the question below.\n",
    "\n",
    "**Question 4a**: Which city has the highest number of trips? Which city has the highest proportion of trips made by subscribers? Which city has the highest proportion of trips made by short-term customers?\n",
    "\n",
    "**Answer**: Based on the data from the exploratory analysis, NYC has the highest trip with 276,798 trips.\n",
    "            NYC has the highest proportion of trips made by subscribers with 88.84% while Chicago has the highest proportion of trips made by short-term customers with 23.77%."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "def number_of_trips(filename):\n",
    "    \"\"\"\n",
    "    This function reads in a file with trip data and reports the number of\n",
    "    trips made by subscribers, customers, and total overall.\n",
    "    \"\"\"\n",
    "    with open(filename, 'r') as f_in:\n",
    "        # set up csv reader object\n",
    "        reader = csv.DictReader(f_in)\n",
    "        \n",
    "        # initialize count variables\n",
    "        n_subscribers = 0\n",
    "        n_customers = 0\n",
    "        \n",
    "        # tally up ride types\n",
    "        for row in reader:\n",
    "            if row['user_type'] == 'Subscriber':\n",
    "                n_subscribers += 1\n",
    "            else:\n",
    "                n_customers += 1\n",
    "        \n",
    "        # compute total number of rides\n",
    "        n_total = n_subscribers + n_customers\n",
    "        \n",
    "        #compute the ratios for the different user types\n",
    "        n_subs_ratio = '{0:.2%}'.format(n_subscribers/n_total)\n",
    "        n_cust_ratio = '{0:.2%}'.format(n_customers/n_total)\n",
    "        \n",
    "        # return tallies as a tuple\n",
    "        return(n_subscribers, n_customers, n_total, n_subs_ratio, n_cust_ratio)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total Number of Trips by City: {'Chicago': 72131, 'NYC': 276798, 'Washington': 66326}\n",
      "City with the highest trip is NYC with 276798 Trips\n",
      "Subscriber ratio by City: {'Chicago': '76.23%', 'NYC': '88.84%', 'Washington': '78.03%'}\n",
      "City with the subscriber ratio is NYC with 88.84%\n",
      "Customer ratio by City: {'Chicago': '23.77%', 'NYC': '11.16%', 'Washington': '21.97%'}\n",
      "City with the customer ratio is Chicago with 23.77%\n"
     ]
    }
   ],
   "source": [
    "## Modify this and the previous cell to answer Question 4a. Remember to run ##\n",
    "## the function on the cleaned data files you created from Question 3.      ##\n",
    "\n",
    "##data_file = './examples/BayArea-Y3-Summary.csv'\n",
    "\n",
    "data_file1 = './data/Chicago-2016-Summary.csv'\n",
    "data_file2 = './data/NYC-2016-Summary.csv'\n",
    "data_file3 = './data/Washington-2016-Summary.csv'\n",
    "\n",
    "\n",
    "# Calculating the number of trips in the different cities.\n",
    "num_trips = {'Chicago': number_of_trips(data_file1)[2],\n",
    "           'NYC': number_of_trips(data_file2)[2], \n",
    "           'Washington': number_of_trips(data_file3)[2]}\n",
    "\n",
    "# Calculating the city with the maximum number of trips.\n",
    "max_num_trips = max(num_trips.keys(), key=(lambda x:num_trips[x]))\n",
    "\n",
    "\n",
    "# Calculating the subscriber ratio by city.\n",
    "subs_ratio = {'Chicago': number_of_trips(data_file1)[3],\n",
    "           'NYC': number_of_trips(data_file2)[3], \n",
    "           'Washington': number_of_trips(data_file3)[3]}\n",
    "\n",
    "# Calculating the city with the maximum subscriber ratio.\n",
    "max_subs_ratio = max(subs_ratio.keys(), key=(lambda x:subs_ratio[x]))\n",
    "\n",
    "\n",
    "# Calculating the customer ratio by city.\n",
    "cust_ratio = {'Chicago': number_of_trips(data_file1)[4],\n",
    "           'NYC': number_of_trips(data_file2)[4], \n",
    "           'Washington': number_of_trips(data_file3)[4]}\n",
    "\n",
    "\n",
    "# Calculating the city with the maximum customer ratio\n",
    "max_cust_ratio = max(cust_ratio.keys(), key=(lambda x:cust_ratio[x]))\n",
    "\n",
    "\n",
    "\n",
    "# Printing all values to the screen\n",
    "print('Total Number of Trips by City:', num_trips)\n",
    "print('City with the highest trip is {} with {} Trips'.format(max_num_trips, num_trips[max_num_trips]))\n",
    "\n",
    "\n",
    "print('Subscriber ratio by City:', subs_ratio)\n",
    "print('City with the subscriber ratio is {} with {}'.format(max_subs_ratio, subs_ratio[max_subs_ratio]))\n",
    "\n",
    "\n",
    "print('Customer ratio by City:', cust_ratio)\n",
    "print('City with the customer ratio is {} with {}'.format(max_cust_ratio, cust_ratio[max_cust_ratio]))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Tip**: In order to add additional cells to a notebook, you can use the \"Insert Cell Above\" and \"Insert Cell Below\" options from the menu bar above. There is also an icon in the toolbar for adding new cells, with additional icons for moving the cells up and down the document. By default, new cells are of the code type; you can also specify the cell type (e.g. Code or Markdown) of selected cells from the Cell menu or the dropdown in the toolbar.\n",
    "\n",
    "Now, you will write your own code to continue investigating properties of the data.\n",
    "\n",
    "**Question 4b**: Bike-share systems are designed for riders to take short trips. Most of the time, users are allowed to take trips of 30 minutes or less with no additional charges, with overage charges made for trips of longer than that duration. What is the average trip length for each city? What proportion of rides made in each city are longer than 30 minutes?\n",
    "\n",
    "**Answer**: Based on the exploratory analysis, the average trip length for Chicago is 17.0 minutes with 8.33% of the trips longer than 30 minutes. For NYC, the average trip length is 16.0 minutes and 7.30% of trips are longer than 30 minutes. \n",
    "\n",
    "Finally, for Washington, the average trip length is 19.0 minutes and 10.84% of trips are longer than 30 minutes."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "## Use this and additional cells to answer Question 4b.                 ##\n",
    "##                                                                      ##\n",
    "## HINT: The csv module reads in all of the data as strings, including  ##\n",
    "## numeric values. You will need a function to convert the strings      ##\n",
    "## into an appropriate numeric type before you aggregate data.          ##\n",
    "## TIP: For the Bay Area example, the average trip length is 14 minutes ##\n",
    "## and 3.5% of trips are longer than 30 minutes.                        ##\n",
    "\n",
    "def travel_length(filename):\n",
    "    \n",
    "    \n",
    "    with open(filename, 'r') as f_in:\n",
    "        # set up csv reader object\n",
    "        reader = csv.DictReader(f_in)\n",
    "        \n",
    "        short_trip = 0\n",
    "        \n",
    "        long_trip = 0  \n",
    "        \n",
    "        trip_length = 0\n",
    "   \n",
    "        for row in reader:\n",
    "            \n",
    "            # Calculating the total trip length\n",
    "            trip_length += float(row['duration'])\n",
    "            \n",
    "            \"\"\" \n",
    "            Based on duration criteria, long trip are greater than 30 minutes.\n",
    "            \"\"\"\n",
    "            if float(row['duration']) > 30:\n",
    "                \n",
    "                long_trip +=1\n",
    "\n",
    "            else:\n",
    "                short_trip +=1\n",
    "            \n",
    "            # Calculating the total number of trip\n",
    "            \n",
    "            total_trip = short_trip + long_trip\n",
    "            \n",
    "            # Calculating the average number of trip\n",
    "            \n",
    "            average_trip = round((trip_length)/(total_trip),0)\n",
    "            \n",
    "            # Ratio of Short trips to the total number of trips\n",
    "            short_trip_pct = '{0:.2%}'.format((short_trip)/(total_trip))\n",
    "            \n",
    "            # Ratio of Long trips to the total number of trips\n",
    "            long_trip_pct =  '{0:.2%}'.format((long_trip)/(total_trip))\n",
    "            \n",
    "            \n",
    "            # Return all the calculated values\n",
    "        return (average_trip, short_trip_pct, long_trip_pct)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "For Chicago, the average trip length is 17.0 minutes and 8.33% of trips are longer than 30 minutes\n",
      "For NYC, the average trip length is 16.0 minutes and 7.30% of trips are longer than 30 minutes\n",
      "For Washington, the average trip length is 19.0 minutes and 10.84% of trips are longer than 30 minutes\n"
     ]
    }
   ],
   "source": [
    "data_file = {'Chicago': './data/Chicago-2016-Summary.csv',\n",
    "             'NYC': './data/NYC-2016-Summary.csv',\n",
    "             'Washington': './data/Washington-2016-Summary.csv'}\n",
    "\n",
    "for city, file in data_file.items():\n",
    "    average_trip, short_trip_pct, long_trip_pct = travel_length(file)\n",
    "    print('For {}, the average trip length is {} minutes and {} of trips are longer than 30 minutes'\n",
    "          .format(city,average_trip,long_trip_pct))\n",
    "    \n",
    "    # Displaying all the values to the screen.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Question 4c**: Dig deeper into the question of trip duration based on ridership. Choose one city. Within that city, which type of user takes longer rides on average: Subscribers or Customers?\n",
    "\n",
    "**Answer**: For this portion of the exploratory analysis, the city of Washington is selected, the average Subscriber trip duration is 12.5 minutes and 41.7 minutes the average Customer trip duration.\n",
    "For Chicago, the average Subscriber trip duration is 12.1 minutes and 31.0 minutes the average Customer trip duration\n",
    "For NYC, the average Subscriber trip duration is 13.7 minutes and 32.8 minutes the average Customer trip duration"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "## Use this and additional cells to answer Question 4c. If you have    ##\n",
    "## not done so yet, consider revising some of your previous code to    ##\n",
    "## make use of functions for reusability.                              ##\n",
    "##                                                                     ##\n",
    "## TIP: For the Bay Area example data, you should find the average     ##\n",
    "## Subscriber trip duration to be 9.5 minutes and the average Customer ##\n",
    "## trip duration to be 54.6 minutes. Do the other cities have this     ##\n",
    "## level of difference?                                                ##\n",
    "\n",
    "def rides_by_usertype(filename):\n",
    "    with open(filename, 'r') as f_in:\n",
    "        # set up csv reader object\n",
    "        reader = csv.DictReader(f_in)\n",
    "        \n",
    "        n_subscribers = 0\n",
    "        subs_trip_length = 0\n",
    "        \n",
    "        n_customers = 0\n",
    "        cust_trip_length = 0\n",
    "   \n",
    "        for row in reader:\n",
    "              \n",
    "            # Calculating the trip length for the different user types.\n",
    "            if row['user_type'] == 'Subscriber':\n",
    "                n_subscribers += 1\n",
    "                subs_trip_length += float(row['duration'])\n",
    "            else:\n",
    "                n_customers += 1\n",
    "                cust_trip_length += float(row['duration'])\n",
    "                \n",
    "            # Calculating the average trip length for the different user types.    \n",
    "        avg_sub_trip = round((subs_trip_length)/(n_subscribers),1)\n",
    "        avg_cust_trip = round((cust_trip_length)/(n_customers),1)\n",
    "                      \n",
    "        return (avg_sub_trip, avg_cust_trip, n_subscribers, subs_trip_length, n_customers, cust_trip_length)\n",
    "            # Returning all calculated values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "For Washington, the average Subscriber trip duration is 12.5 minutes and 41.7 minutes the average Customer trip duration\n"
     ]
    }
   ],
   "source": [
    "# Selected City: Washington\n",
    "\n",
    "data_file = {'Washington': './data/Washington-2016-Summary.csv'}\n",
    "\n",
    "for city, file in data_file.items():\n",
    "    avg_sub_trip, avg_cust_trip, n_subscribers, subs_trip_length, n_customers, cust_trip_length = rides_by_usertype(file)\n",
    "    \n",
    "    print('For {}, the average Subscriber trip duration is {} minutes and {} minutes the average Customer trip duration'\n",
    "          .format(city, avg_sub_trip, avg_cust_trip))\n",
    "\n",
    "# Printing the average trip length for the different user types for Washington."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "For Chicago, the average Subscriber trip duration is 12.1 minutes and 31.0 minutes the average Customer trip duration\n",
      "For NYC, the average Subscriber trip duration is 13.7 minutes and 32.8 minutes the average Customer trip duration\n"
     ]
    }
   ],
   "source": [
    "# For other cities\n",
    "\n",
    "data_file = {'Chicago': './data/Chicago-2016-Summary.csv',\n",
    "             'NYC': './data/NYC-2016-Summary.csv'}\n",
    "\n",
    "for city, file in data_file.items():\n",
    "    avg_sub_trip, avg_cust_trip, n_subscribers, subs_trip_length, n_customers, cust_trip_length = rides_by_usertype(file)\n",
    "    \n",
    "    print('For {}, the average Subscriber trip duration is {} minutes and {} minutes the average Customer trip duration'\n",
    "          .format(city, avg_sub_trip, avg_cust_trip))\n",
    "    \n",
    "# Printing the average trip length for the different user types for the other cities."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='visualizations'></a>\n",
    "### Visualizations\n",
    "\n",
    "The last set of values that you computed should have pulled up an interesting result. While the mean trip time for Subscribers is well under 30 minutes, the mean trip time for Customers is actually _above_ 30 minutes! It will be interesting for us to look at how the trip times are distributed. In order to do this, a new library will be introduced here, `matplotlib`. Run the cell below to load the library and to generate an example plot."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x7faf88116710>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# load library\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# this is a 'magic word' that allows for plots to be displayed\n",
    "# inline with the notebook. If you want to know more, see:\n",
    "# http://ipython.readthedocs.io/en/stable/interactive/magics.html\n",
    "%matplotlib inline \n",
    "\n",
    "# example histogram, data taken from bay area sample\n",
    "data = [ 7.65,  8.92,  7.42,  5.50, 16.17,  4.20,  8.98,  9.62, 11.48, 14.33,\n",
    "        19.02, 21.53,  3.90,  7.97,  2.62,  2.67,  3.08, 14.40, 12.90,  7.83,\n",
    "        25.12,  8.30,  4.93, 12.43, 10.60,  6.17, 10.88,  4.78, 15.15,  3.53,\n",
    "         9.43, 13.32, 11.72,  9.85,  5.22, 15.10,  3.95,  3.17,  8.78,  1.88,\n",
    "         4.55, 12.68, 12.38,  9.78,  7.63,  6.45, 17.38, 11.90, 11.52,  8.63,]\n",
    "plt.hist(data)\n",
    "plt.title('Distribution of Trip Durations')\n",
    "plt.xlabel('Duration (m)')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In the above cell, we collected fifty trip times in a list, and passed this list as the first argument to the `.hist()` function. This function performs the computations and creates plotting objects for generating a histogram, but the plot is actually not rendered until the `.show()` function is executed. The `.title()` and `.xlabel()` functions provide some labeling for plot context.\n",
    "\n",
    "You will now use these functions to create a histogram of the trip times for the city you selected in question 4c. Don't separate the Subscribers and Customers for now: just collect all of the trip times and plot them."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x7faf88116588>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "## Use this and additional cells to collect all of the trip times as a list ##\n",
    "## and then use pyplot functions to generate a histogram of trip times.     ##\n",
    "\n",
    "# Using matplotlib and other library to plot a histogram of the duration in the selected city.\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "%matplotlib inline \n",
    "\n",
    "dataframe = pd.read_csv('./data/Washington-2016-Summary.csv')\n",
    "duration = dataframe['duration']\n",
    "num_bins = np.arange(0,200,5)\n",
    "plt.hist(duration, num_bins, facecolor='#607c8e')\n",
    "plt.ylabel('Frequency')\n",
    "plt.xlabel('Duration (minutes)')\n",
    "plt.title('Frequency Distribution of Duration for Washington')\n",
    "plt.axis([0, None, 0, None])\n",
    "plt.grid(False)\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If you followed the use of the `.hist()` and `.show()` functions exactly like in the example, you're probably looking at a plot that's completely unexpected. The plot consists of one extremely tall bar on the left, maybe a very short second bar, and a whole lot of empty space in the center and right. Take a look at the duration values on the x-axis. This suggests that there are some highly infrequent outliers in the data. Instead of reprocessing the data, you will use additional parameters with the `.hist()` function to limit the range of data that is plotted. Documentation for the function can be found [[here]](https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist).\n",
    "\n",
    "**Question 5**: Use the parameters of the `.hist()` function to plot the distribution of trip times for the Subscribers in your selected city. Do the same thing for only the Customers. Add limits to the plots so that only trips of duration less than 75 minutes are plotted. As a bonus, set the plots up so that bars are in five-minute wide intervals. For each group, where is the peak of each distribution? How would you describe the shape of each distribution?\n",
    "\n",
    "**Answer**: Based on the generated histogram, the peak duration for Subscribers in Washington is between 5 and 10 minutes.\n",
    "\n",
    "On the other hand, the peak duration for Customers in Washington is between 15 and 20 minutes.\n",
    "The duration for both Customers and Subscribers in Washington appears to be positively skewed."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x7faf78ce7940>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x7faf616bd358>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "## Use this and additional cells to answer Question 5. ##\n",
    "\n",
    "# Using matplotlib to plot a histogram of the duration in the selected city.\n",
    "\n",
    "%matplotlib inline \n",
    "\n",
    "# Selecting the duration for the Subscriber user type\n",
    "subs_duration = dataframe.query(\"user_type == 'Subscriber'\")\n",
    "duration = subs_duration['duration']\n",
    "\n",
    "\n",
    "#print(duration)\n",
    "num_bins = np.arange(0, 75, 5)\n",
    "plt.hist(duration, num_bins, facecolor='#56B4E9')\n",
    "plt.ylabel('Frequency')\n",
    "plt.xlabel('Duration (minutes)')\n",
    "plt.title('Distribution of Duration for Subscribers in Washington')\n",
    "\n",
    "# Limiting the x-axis to duration less than 75 minutes.\n",
    "plt.axis([0, 75, 0, None])\n",
    "plt.xticks(num_bins)\n",
    "plt.grid(False)\n",
    "\n",
    "# Showing the plot\n",
    "plt.show()\n",
    "\n",
    "\n",
    "# Selecting the duration for the Customer user type\n",
    "cust_duration = dataframe.query(\"user_type == 'Customer'\")\n",
    "duration = cust_duration['duration']\n",
    "\n",
    "#print(duration)\n",
    "num_bins = np.arange(0, 75, 5)\n",
    "plt.hist(duration, num_bins, facecolor='#607C8E')\n",
    "plt.ylabel('Frequency')\n",
    "plt.xlabel('Duration (minutes)')\n",
    "plt.title('Distribution of Duration for Customers in Washington')\n",
    "\n",
    "# Limiting the x-axis to duration less than 75 minutes.\n",
    "plt.axis([0, 75, 0, None])\n",
    "plt.xticks(num_bins)\n",
    "plt.grid(False)\n",
    "\n",
    "# Showing the plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "<a id='eda_continued'></a>\n",
    "## Performing Your Own Analysis\n",
    "\n",
    "So far, you've performed an initial exploration into the data available. You have compared the relative volume of trips made between three U.S. cities and the ratio of trips made by Subscribers and Customers. For one of these cities, you have investigated differences between Subscribers and Customers in terms of how long a typical trip lasts. Now it is your turn to continue the exploration in a direction that you choose. Here are a few suggestions for questions to explore:\n",
    "\n",
    "- How does ridership differ by month or season? Which month / season has the highest ridership? Does the ratio of Subscriber trips to Customer trips change depending on the month or season?\n",
    "- Is the pattern of ridership different on the weekends versus weekdays? On what days are Subscribers most likely to use the system? What about Customers? Does the average duration of rides change depending on the day of the week?\n",
    "- During what time of day is the system used the most? Is there a difference in usage patterns for Subscribers and Customers?\n",
    "\n",
    "If any of the questions you posed in your answer to question 1 align with the bullet points above, this is a good opportunity to investigate one of them. As part of your investigation, you will need to create a visualization. If you want to create something other than a histogram, then you might want to consult the [Pyplot documentation](https://matplotlib.org/devdocs/api/pyplot_summary.html). In particular, if you are plotting values across a categorical variable (e.g. city, user type), a bar chart will be useful. The [documentation page for `.bar()`](https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar) includes links at the bottom of the page with examples for you to build off of for your own use.\n",
    "\n",
    "**Question 6**: Continue the investigation by exploring another question that could be answered by the data available. Document the question you want to explore below. Your investigation should involve at least two variables and should compare at least two groups. You should also use at least one visualization as part of your explorations.\n",
    "\n",
    "**Question**: How does ridership differ by month? Which month has the highest ridership? Does the ratio of Subscriber trips to Customer trips change depending on the month?\n",
    "\n",
    "**Answer**: There is an increase in the ridership from January to July, and a decrease in the ridership from July to December. This trend follows for both user types. The month with the highest ridership is July, and this is peak for the number of rides for Customers. \n",
    "The ratio of Subscriber trips to Customer trips changed over time with the lowest value of 2.358 occuring in July."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "user_type  Customer  Subscriber  Total  Subs_Percent  Cust_Percent  \\\n",
      "month                                                                \n",
      "1               222        2212   2434     90.879211      9.120789   \n",
      "2               283        2571   2854     90.084093      9.915907   \n",
      "3              1188        4383   5571     78.675283     21.324717   \n",
      "4              1192        4410   5602     78.721885     21.278115   \n",
      "5              1248        4520   5768     78.363384     21.636616   \n",
      "6              1707        5613   7320     76.680328     23.319672   \n",
      "7              2186        5155   7341     70.222041     29.777959   \n",
      "8              1806        5392   7198     74.909697     25.090303   \n",
      "9              1674        5204   6878     75.661530     24.338470   \n",
      "10             1560        5232   6792     77.031802     22.968198   \n",
      "11             1075        4139   5214     79.382432     20.617568   \n",
      "12              432        2922   3354     87.119857     12.880143   \n",
      "\n",
      "user_type  Sub_Cust_Ratio  \n",
      "month                      \n",
      "1                9.963964  \n",
      "2                9.084806  \n",
      "3                3.689394  \n",
      "4                3.699664  \n",
      "5                3.621795  \n",
      "6                3.288225  \n",
      "7                2.358188  \n",
      "8                2.985604  \n",
      "9                3.108722  \n",
      "10               3.353846  \n",
      "11               3.850233  \n",
      "12               6.763889  \n"
     ]
    },
    {
     "data": {
      "image/png": "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uHAhN910E4sXL+b5559nt91247vf/S5z585l/vz57L333nz/+98nMwH44x//WPfnrLvuusybN2+ptmOOOYYTTzyRESNGLNVbN2HCBBYsWMDs2bOZOHEiI0aMYO+992b8+PHMnz8fgL/85S/MnDlzFZyBVcseN0mS1DA9e/bktNNOY6eddmLw4MG8973vZdGiRXz605/m1VdfJTM56aST6Nu3L6eeeipf/OIXGTp0KJnJoEGDllyz1pmhQ4fSo0cP3v/+93PkkUdy0kkn8YEPfIB3v/vdHHXUUUutO3LkSPbff3+ee+45Tj31VAYMGMCAAQOYNm0au+yyCwB9+vThyiuvZKONNlrl52RlREuqfScZPnx41naJSlp9LG8vWtI97xyTmmHatGlss802zS5jlXnhhRcYNWoUjz32GGusUQwynnHGGfTp04cvf/nLTamprXMcEVMzc3g92ztUKkmS3nEuv/xydtppJ84+++wloe2dwKFSSZJUGX/60584/PDDl2pbe+21uffee5dqO+KIIzjiiCOW2f6MM85oZHkNZ3CTJEmV8b73vW+pB+uubt45fYeSJEnvcAY3SZKkijC4SZIkVYTBTZIkqSIMbpIkqVv561//yqGHHspWW23Ftttuy3777cef//zn5drHDTfcwKOPPtqgCpvH4CZJktoUsWq/6pGZfPSjH2XUqFE8+eSTPProo3zrW9/ipZdeWq7amxHcFi1a1PDPMLhJkqRu43e/+x09e/bks5/97JK2YcOGsWjRIg444IAlbf/yL//CpZdeCsDJJ5/Mtttuy9ChQ/nyl7/MH/7wB2688Ua+8pWvMGzYMJ588kkeeOABdt55Z4YOHcpHP/pRXnnlFQBGjRrFSSedxK677so222zDfffdx0EHHcSQIUP4+te/vuTzrrzySkaOHMmwYcM4/vjjl4S0Pn36LHml1913393w8+Nz3CRJK8XXjGlVevjhh/nABz5Q9/pz5szhF7/4BY899hgRwdy5c+nbty9jxozhgAMO4OMf/zhQvMv0+9//Ph/+8Ic57bTTOPPMM7ngggsAWGuttZg0aRLf+973GDt2LFOnTqVfv35stdVWnHTSScycOZOf/OQn/P73v6dnz56ccMIJXHXVVRxxxBG89tprbL/99px11lkNOR+tGdwkSVJlvfvd76ZXr14cc8wx7L///kv1yrV49dVXmTt3Lh/+8IcBGDduHAcffPCS5WPGjAGKh/tut912bLLJJgBsueWWPP/889x1111MnTqVESNGAPD3v/99ycvn11xzTT72sY819BhrGdwkSVK3sd1223Hdddct096jRw8WL168ZH7BggVL2idPnsztt9/Otddeyw9+8AN++9vfLtdnrr322gCsscYaS6Zb5t966y0yk3HjxvHtb397mW179erFmmuuuVyftzK8xk2SJHUbu+++OwsXLuTHP/7xkrb77ruPRYsW8eijj7Jw4UJeffVVbr/9dgDmz5/Pq6++yn777ccFF1yw5HVY6667LvPmzQNgvfXWY/311+fOO+8E4IorrljS+1aPPfbYg+uuu46ZM2cCxfDss88+u0qOd3nZ4yZJkrqNiOAXv/gFX/ziFznnnHPo1asXgwYN4oILLuATn/gEQ4cOZciQIeywww4AzJs3j7Fjx7JgwQIyk/PPPx+AQw89lGOPPZYLL7yQ6667jssuu4zPfvazvP7662y55ZZccskldde07bbb8s1vfpPRo0ezePFievbsyQ9/+EO22GKLhpyDjkRmdvmHNtrw4cNzypQpzS5DUhN4oXzX85y/c0ybNo1tttmm2WW8o7V1jiNiamYOr2d7h0olSZIqwuAmSZJUEQY3SZKkivDmBEmSKsbrCldfBjdJ0mpreQKQ4UfdgUOlkiRJFWFwkyRJ3crZZ5/Ndtttx9ChQxk2bBj33ntvu+ueccYZnHfeeav086dMmcKJJ57YsP2vDIdKJambcNhO3c3yXkvXmXp+bu+++25uuukm7r//ftZee21efvll3njjjVVaR0feeusthg8fzvDhdT1WrUOZSWayxhqrrp/MHjdJktRtvPjii2y44YZL3hm64YYbMmDAAAYNGsTLL78MFD1io0aNWrLNgw8+yO67786QIUOWvCrrxRdfZNddd2XYsGFsv/32S1539etf/5odd9yR97///eyxxx5A0at23HHHMXr0aI444ggmTpy41Mvq29o/wLnnnsuIESMYOnQop59ehNJnnnmGbbbZhhNOOIEdd9yR559/fpWeH3vcJElStzF69GjOOuss3vOe97DnnntyyCGHdPpe0Yceeoh77rmH1157jR122IH999+fa665hr333puvfe1rLFq0iNdff51Zs2Zx7LHHMmnSJAYPHsycOXOW7GPq1Knc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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x7faf61722be0>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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IiJSkZYtW0bbtm0Llh955BHuueceHn/8cY488kjS09MZMGAAAJs3b+bSSy+lS5cudOzYkXHjxgEwYsQIzj33XE477TR69+5d5Hluu+02pk2bRocOHXjyySc5/vjjmT9/fsHn3bp1Y8GCBdxzzz1cdNFF9OzZk8MPP5znnnuuYJthw4bRpUsX0tPTufvuu8PxdVSI0gzq34WZtQT+7O5/DEM9IiIiEqUefPBBfvjhB2rUqMGGDaEH99x///307NmT4cOHs2HDBrp27cpJJ50EwMyZM1mwYAEHHHBAscd75JFHmDBhAllZWTRu3JgRI0bw2GOP8c0335CTk0N6ejpvvfUWCxYs4NNPP2Xz5s107NiRvn378tVXX7F06VJmz56Nu3P66aczdepUunfvXuT5ollJY8jamtl/zGy+md1jZqlm9iYwFfi+4koUERGRaJCens7AgQN55ZVXiI8P9elMmjSJBx98kA4dOpCRkcG2bdv46aefAOjVq1exYawo5557LhMmTGDHjh0MHz6cwYMHF3zWv39/kpKSaNCgAT169GD27NlMmjSJSZMm0bFjR4466ii+/vprli5dWq5trigl9ZA9H/zMBE4G5gGjgRbuvrUCahMREZEIiI+PJy8vr2A5/15bEydOZOrUqYwfP5777ruPhQsX4u6MHTuWtLS0XY4xa9YsatWqVabz1qxZk169ejFu3DhGjRrFnDlzCj7b/RYTZoa7c/vtt3PllVeWtYlRp6RB/Ynu/ry7L3T3fwTrblEYExERiW0HHnggq1evZt26deTk5DBhwgTy8vJYvnw5PXr04OGHH2bDhg1kZ2fTp08fnnjiCdwdgM8//7zU50lJSSErK2uXdZdffjnXX389Xbp02aV3bdy4cWzbto1169aRmZlJly5d6NOnD8OHDyc7OxuAX375hdWrV5fDN1DxSuohSzSzdkB+JM0GjrAgorr7gnAXJyIiIhUvISGBu+66i6OPPprmzZvTunVrcnNzufDCC9m4cSPuzp/+9Cfq1q3LnXfeyY033kh6ejruTrNmzZgwYUKpzpOenk58fDzt27dnwIAB3H777XTq1InatWtzySWX7LJt165d6du3Lz/99BN33nknjRs3pnHjxixevJhjjz0WgOTkZF555RUaNmxY7t9JuJUUyNYATxdaXlto2fn9RrEiIiISY66//nquv/76vW6XlJTEv//97z3WDx48eJcxYEVJSEhg8uTJAAU9ZStWrCAvL2+PmZmtWrXi2Wef3eMYN9xwAzfccMNe64x2JT1c/PiKLERERESqtpdeeom//vWvPProo1SrVprHbceOMt/2QkRERKQsvvzySy666KJd1tWoUYNZs2btsu7iiy/m4osv3mP/e+65J5zlRQUFMhEREQmrdu3a7XLDV9lT1eoPFBEREYlCxfaQmVl6STtqlqWIiIhI+SjpkuVTJXymWZYiIiIi5USzLEVEREQirFSD+s2sNXAkkJi/zt1fC1dRIiIiIlXJXgf1m9kdwLPAM8ApwGPAOaU5uJktM7MvgweUzwnWHWBmH5jZ0uC13n7ULyIiIhVg1apVDBgwgBYtWnDkkUdy6qmn8s0335TpGO+88w6LFi0qcZvBgwfTvHlzOnTowFFHHcXMmTP3p+x9lpmZyYwZMyrsfKWZZXk+0ANY6e4XAe0p2+0yerh7B3fvHCzfBkx298OBycGyiIiIRCl358wzzyQjI4PvvvuORYsW8cADD/Drr7+W6TilCWQAw4YNY/78+Tz44INlenD4zp07y1RPSSo6kJUmWG1191wz22lmKcAq4LD9OGd/ICN4PxLIBG7dj+OJiIhUGTfeCPm39MrNTSIubv+P2aEDPPZY8Z9PmTKFhIQErrrqqkL7dCAzM5N+/foVPLvy2muvpXPnzgwePJjbbruN8ePHEx8fT+/evTnrrLMYP348H3/8MUOHDmXs2LG0aNGixLq6d+/Ot99+C8B3333HNddcw5o1a6hZsybPPfccrVu3ZvDgwRxwwAF8/vnnHHXUUdx7771cd911zJkzBzPj7rvv5uyzz2bSpEncfffd5OTk0KJFC1588UWSk5Np1qwZgwYN4t1332XHjh2MHj2axMREnnnmGeLi4njllVd44oknOP748A6tL00g+9zM6gLDgTnAJmBeKY/vwCQzc+Df7v4scKC7rwRw95VmVvmeACoiIlKFfPXVV3Tq1KnU2//222+8/fbbfP3115gZGzZsoG7dupx++un069ePc84p1cgn3n33Xdq1awfAkCFDeOaZZzj88MOZNWsWV199NR999BEA33zzDR9++CFxcXHceuut1KlThy+//BKA9evXs3btWoYOHcqHH35IrVq1eOihh3j00Ue56667AGjQoAHz5s3j6aef5pFH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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x7faf615c88d0>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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b9jRREREpJqptgUZgJlxySWX8NZbb5Gbm8s111zDiSeeyKpVq8KOJiIiItVItS7Iihx++OG8/PLLjB07ljfeeIMuXbrw6KOP4u5hRxMREZFqQAVZlJkxbNgwVqxYQa9evRg2bBinnnoqq1evDjuaiIiIpDkVZKUceeSRvPbaa/zlL39hxowZdO7cmSeeeEK9ZSIiIpIwKsj2IyMjg2uuuYZly5bRqVMnLr74Ys466yzWrFkTdjQRERFJQyrIytCuXTtmzJjBPffcwyuvvELnzp156qmnwo4lIiIiaUYFWTlq1KjByJEjWbJkCUcddRTnnXceP/7xj1m3bl3Y0URERCRNqCCL0THHHMPcuXO56667eOGFF+jUqRMvvPBC2LFEREQkDaggOwiZmZnccsstLFy4kFatWnHWWWdx0UUXsXHjxrCjiYiISBWmgqwCunbtyoIFC7jtttuYPHkynTt35uWXXw47loiIiFRRKsgqqGbNmtxxxx0sWLCAJk2acMopp3D55ZezZcuWsKOJiIhIFaOCrJJ69uzJokWLuOmmm5gwYQJdunRh6tSpYccSERGRKkQFWRzUqlWLu+++mzlz5lC7dm1OOOEErr76agoKCsKOJiIiIlWACrI46tu3L0uWLOH666/noYceolu3bsyaNSvsWCIiIpLiVJDFWd26dRk1ahTTp0/H3TnuuOO44YYb2LFjR9jRREREJEWpIEuQIAhYvnw5V1xxBaNGjSInJ4cFCxaEHUtERERSkAqyBKpfvz4PPvggr776Ktu3b6d///689957YccSERGRFBNKQWZmvzCzt8zsbTO7PowMyXTCCSewePFiAObOnRtyGhEREUk1SS/IzKwzMAw4FugGnGZm7ZOdI9maN29OTk4OK1asCDuKiIiIpJgwesiOAea7+3Z33wPMAM4KIUfS5ebm8s4777Bz586wo4iIiEgKMXdP7gnNjgH+AfQDdgBTgYXufm2p7YYDwwGys7N7TpkyJak5E2HWrFncdtttjBkzhi5duoQdp1IKCgqoX79+2DHiQm1JPenSDlBbUlW6tCVd2gHp1Za8vLxF7t7rYPbJTFSYA3H3d83sT8CrQAGwDNizn+3GAmMBOnbs6IMGDUpmzITo1KkTt912G9u2baOqt2f69OlVvg1F1JbUky7tALUlVaVLW9KlHZBebamIUAb1u/s4d+/h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w4Y0atSIxo0b06hRo4N+Xbt27QR+6yIiqaewsJD//Oc/jB8/nhdffJFdu3bRq1cvHnjgAc4//3yaNGkSdsQqQwWZHLRLLrmEuXPn8vHHH5ORkVHukpmZWebnNWrUiOk4iVreeecdmjdvzubNm9m0aRObN29m8+bNfPrpp8WvN2/eXG6BV7NmzQoXc0VLZqb+kxSR1Pfhhx8yYcIEJk6cyOrVq2nevDlXXXUVl156KV27dg07XpWk//vLQTv++ON59NFHGTRoUNhR4mL69OnltmXv3r0UFBTsU7SV9/rLL78sfr1t27Zys9SrV6/CvXSNGzeO0zciIrKvgoICnn76aSZMmMCsWbPIyMjghz/8IWPGjOG0006jZs2aYUes0lSQicQgIyODhg0b0rBhQ1q3bl2hY+zZs+c7PW4lC7gDFXTr16/no48+Kl5X3mOrDj30UE455RQGDx5MXl4ehx56aIWyiohAZCzunDlzmDBhAk899RTbtm2jQ4cO3H333Vx00UW0atUq7IhpQwWZSJJkZmbSrFkzmjVrVuFjfPvttwcs4NavX89LL73Es88+y7hx4wA4+uiji4uzQYMG0bx583g1R0TS2JdffsnEiRMZP348H374IfXr1+e8887jsssuo1+/froJKgFUkIlUIbVr16Z27dq0aNFiv5/36dOH3Nxcli1bxuuvv860adOYOHEiDz74IABdu3Zl8ODBDB48mCAIaNSoUTLji0gK27VrF//85z8ZP348r7zyCnv37iUIAm699VaGDBlC/fr1w46Y1lSQiaSZGjVq0KNHD3r06MGNN97I7t27WbhwIdOmTeP111/nr3/9K/fddx8ZGRn07NmTvLw8Bg8ezMCBA6lXr17Y8UUkyZYtW8aECROYNGkS69ev57DDDuPmm29m6NChtGvXLux41YYKMpE0l5WVRb9+/ejXrx+33HILO3fuZP78+cU9aKNGjeLPf/4zWVlZHHvsscU9aH379tVUHiJpasOGDUyePJnx48ezePFiatasyZlnnsmll17KiSeeqDnDQqCCTKSaqVWrFscddxzHHXccd9xxB9u2bWPOnDnFPWh33XUXv//976lduzb9+/cvHoPWu3dvsrKywo4vIhVUWFjI1KlTGT9+PM8//zy7du0iJyeHMWPGcMEFF1RqfKtUngoykWquXr16nHTSSZx00kkAbN68mVmzZhX3oP3mN78p3i43N7e4B6179+76V7RIFfDRRx/x2GOP8dhjj/HFF1/QtGlTrrjiCi699FK6d+8edjyJUkEmIt/RqFEjTjvtNE477TQA1q1bx4wZM4p70H71q18B0LhxY4477rjiHrROnTqRkZERZnQRidq2bRvPPvss48ePZ8aMGWRkZPCDH/yA/Px8Tj/9dGrVqhV2RClFBZmIlKl58+YMGTKEIUOGAPDVV18xffp0Xn/9dV5//XX+8Y9/AJCdnc2gQYOKe9Dat2+vW+NFksjdmT9/PuPHj+epp55i69attGvXjrvuuouLL76Yww8/POyIUgYVZCJyUA499FDOP/98zj//fABWrVrFtGnTinvQnn76aQBatWpVXJzl5eVx5JFHhphaJH199dVXPPHEE0yYMIH33nuPevXqce6553LZZZcxcOBA/cOoilBBJiKV0qZNG4YOHcrQoUNxd1auXFlcnP373/9m0qRJALRt27Z4io28vDzN8C1SQRs2bGDZsmUsWbKEZ555hjfeeIPCwkIGDBjAuHHjOPfcc2nQoEHYMeUgqSATkbgxM9q3b0/79u0ZPnw47s4777xTfIPA888/z/jx4wHo2LFjcQ+aniIgsi93Z9WqVSxdupQlS5awdOlSli5dymeffVa8TYsWLfjlL3/J0KFD6dixY4hppbJUkIlIwpgZnTp1olOnTlx77bUUFhaybNmy4h60J554goceegiIPEWgqAdNNwdIdbNr1y7efffd4qKrqADbvHkzEHmebseOHRkwYABXX301OTk5dOvWjXfeeYdBgwaFG17iQgWZiCRNyacIjBw5kt27d7No0aLiGwQefvhhRo8eTWZmJr///e/55S9/qak1JO1s3ryZZcuWFRdfS5cu5e2332bXrl0A1K1bl65du3L++efTvXt3unfvTpcuXahbt+4+x3rnnXeSHV8SRAWZiIQmKyuLvn370rdv3+88ReC2227j5ptv5t///jdPPPGE7g6TKsndWb169XcuNy5dupSPP/64eJvs7GxycnIYMWJEcfHVvn17/UOkGlJBJiIpo+gpArfffjuffPIJ1113HV27duWRRx4pnnZDJBXt2bOH999/f5/xXuvXry/epn379vTs2ZPLL7+8uPhq2bKl7oIUQAWZiKQgM+Oyyy4jNzeXCy64gHPOOYfLL7+c++67Tw9A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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x7faf61523828>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "dataframe = pd.read_csv('./data/Washington-2016-Summary.csv')\n",
    "\n",
    "# Calculating the number of rides by user type and month\n",
    "rides_count = dataframe.groupby(['user_type','month'])['duration'].count().reset_index()\n",
    "\n",
    "# Creating a pivot table of the number of rides by user type and month\n",
    "total_rides = rides_count.pivot(index = 'month', columns = 'user_type', values = 'duration')\n",
    "\n",
    "# Plotting the data on a bar chart\n",
    "ax = total_rides.plot(kind = 'bar', title = 'Number of Rides by User Type by Month', figsize=(10,6), colormap='winter')\n",
    "ax.set_xlabel(\"Month\")\n",
    "ax.set_ylabel(\"Number of Rides\")\n",
    "\n",
    "\n",
    "rides_by_month = rides_count.pivot(index = 'month', columns = 'user_type', values = 'duration')\n",
    "\n",
    "# Calculating the total rides \n",
    "rides_by_month['Total'] = rides_by_month['Customer'] + rides_by_month['Subscriber']\n",
    "\n",
    "# Calculating the ratio of user type rides to total rides\n",
    "rides_by_month['Subs_Percent'] = (rides_by_month['Subscriber']*100)/(rides_by_month['Total'])\n",
    "rides_by_month['Cust_Percent'] = 100 - rides_by_month['Subs_Percent']\n",
    "\n",
    "# Calculating the Subscriber to Customer Ratio\n",
    "rides_by_month['Sub_Cust_Ratio'] = (rides_by_month['Subscriber'])/(rides_by_month['Customer'])\n",
    "\n",
    "\n",
    "# Plotting the ratio of user type rides to total rides\n",
    "monthly_ride = rides_by_month.reset_index()\n",
    "monthly_r = monthly_ride[['month','Cust_Percent', 'Subs_Percent', 'Sub_Cust_Ratio']]\n",
    "ax_ = monthly_r.plot(x = 'month', y = ['Cust_Percent','Subs_Percent'], kind = 'line', title = 'Percent of Rides by Customers', \n",
    "          figsize = (10,6), colormap='winter', legend = True, grid = True)\n",
    "\n",
    "plt.axis([1, 12, None, None])\n",
    "plt.xticks(monthly_r['month'])\n",
    "plt.xlabel(\"Month\")\n",
    "plt.ylabel(\"% of Total Rides\")\n",
    "\n",
    "\n",
    "# Plotting the Subscriber to Customer Ratio\n",
    "sub_cust_ratio = monthly_r.plot(x = 'month', y = ['Sub_Cust_Ratio'], \n",
    "                                kind = 'line', title = 'Ratio of Subscribers to Customers', \n",
    "                                figsize = (10,6), colormap='gray', legend = False, grid = True)\n",
    "plt.axis([1, 12, None, None])\n",
    "plt.xticks(monthly_r['month'])\n",
    "plt.xlabel(\"Month\")\n",
    "plt.ylabel(\"Subscriber to Customer Ratio\")\n",
    "\n",
    "#Printing the rides by month by user type\n",
    "print(rides_by_month)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Question**: Is the pattern of ridership different on the weekends versus weekdays? On what days are Subscribers most likely to use the system? What about Customers? Does the average duration of rides change depending on the day of the week?\n",
    "\n",
    "**Answer**: Based on the data, the pattern of ridership is generally differnt on weekends versus weekdays. Saturday and Sunday has the lowest number of rides when compared to the weekdays. Subscribers are most likely to use the system on Wednesday and least likely to use it on Sunday. On the other hand, Customers are most likely to use the system on Saturday and least likely to use it on Tuesday. \n",
    "Average duration of rides is highly dependent on the day of the week. Whereas Saturday has the highest average duration, Wednesday has the lowest."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                 len       mean            sum\n",
      "day_of_week                                   \n",
      "Friday        9970.0  17.931890  178780.947133\n",
      "Monday        9394.0  17.563755  164993.915067\n",
      "Saturday      8900.0  24.811503  220822.374133\n",
      "Sunday        8227.0  23.972443  197221.284800\n",
      "Thursday      9984.0  16.685824  166591.263533\n",
      "Tuesday       9748.0  16.691084  162704.685600\n",
      "Wednesday    10103.0  16.294893  164627.301417\n",
      "                 len                  mean                       sum  \\\n",
      "user_type   Customer Subscriber   Customer Subscriber       Customer   \n",
      "day_of_week                                                            \n",
      "Friday        2012.0     7958.0  40.715875  12.171476   81920.339650   \n",
      "Monday        1736.0     7658.0  40.752832  12.306999   70746.916433   \n",
      "Saturday      3311.0     5589.0  44.589926  13.094494  147637.246283   \n",
      "Sunday        2975.0     5252.0  43.429348  12.951062  129202.308883   \n",
      "Thursday      1530.0     8454.0  39.685053  12.523436   60718.131767   \n",
      "Tuesday       1426.0     8322.0  41.777629  12.392428   59574.898867   \n",
      "Wednesday     1583.0     8520.0  36.370252  12.564929   57574.109600   \n",
      "\n",
      "                            \n",
      "user_type       Subscriber  \n",
      "day_of_week                 \n",
      "Friday        96860.607483  \n",
      "Monday        94246.998633  \n",
      "Saturday      73185.127850  \n",
      "Sunday        68018.975917  \n",
      "Thursday     105873.131767  \n",
      "Tuesday      103129.786733  \n",
      "Wednesday    107053.191817  \n"
     ]
    },
    {
     "data": {
      "image/png": "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VPNvd51Jm7oCEzdJakXZR+4VisEFhzU4nDUWEf+DYuqVn2Xm2jbDr00c91I0F5+YdW7yKSfifQF4Fji09b2larCpVJIkqSIcnCBJklQRXbKpdIsttsgBAwY0OgxJkqRVmjZt2muZ2aY36nTJxG3AgAFMnbrKdxZLkiQ1XES09K7mldhUKkmSVBEmbpIkSRVh4iZJklQRXbKPmyRJWn3vv/8+c+fO5d133210KF1Sr1696N+/Pz179lzjc5i4SZIkAObOncuGG27IgAEDKN5MpvaSmbz++uvMnTuXgQMHrvF5bCqVJEkAvPvuu2y++eYmbXUQEWy++eZrXZtp4iZJkpYxaauf9ni2Jm6SJEkVYeImSZIq79lnn+W6665rdBh1Z+ImSZIqY/Hixc2Wm7hJkiStpWeffZZddtll2fr3vvc9xo0bx+WXX85OO+3E4MGDOeGEEwBYtGgRn//859ljjz0YOnQoEyZMAOCqq67iuOOO4+ijj2bkyJHNXuecc87hnnvuYciQIVx22WV86lOfYvr06cu277PPPsyYMYNx48Zx0kknceCBBzJo0CB+8pOfLNvn0ksvZY899mDw4MGMHTu2Ho9jrTkdiCRJ6nCXXHIJzzzzDOuvvz5vvvkmABdffDEHHnggV155JW+++SbDhw/n4IMPBuC+++5jxowZbLbZZi2e73vf+x633XYbAJttthlXXXUV3//+9/nzn//Me++9x+DBg/nVr37FjBkzuP/++1m0aBFDhw7lyCOP5NFHH2XWrFlMmTKFzGTUqFHcfffd7Lfffh3zQNrIGjdJktThBg8ezIknnsi1115Ljx5FPdIdd9zBJZdcwpAhQxgxYgTvvvsuzz//PACHHHJIi0lbc4477jhuu+023n//fa688kpOOeWUZdtGjx5N79692WKLLTjggAOYMmUKd9xxB3fccQdDhw5lt91244knnmDWrFntes/twRo3SZJUNz169GDp0qXL1pvmMfv1r3/N3XffzcSJE7nooot47LHHyExuvvlm/uZv/ma5czzwwANssMEGq3XdD33oQxxyyCFMmDCBG2+8kalTpy7btuK0HBFBZnLuuefyxS9+cXVvsUOZuEnrmOCb7Xq+pHP2A5HUOWy11Va8+uqrvP766/Tp04fbbruNkSNHMmfOHA444AD23XdfrrvuOt5++20OPfRQfvCDH/CDH/yAiODhhx9m6NChbbrOhhtuyMKFC5cr+8IXvsDRRx/Npz71qeVq6yZMmMC5557LokWLmDx5Mpdccgm9e/fm/PPP58QTT6RPnz688MIL9OzZky233LJdn8faMnGTJEl107NnTy644AL23HNPBg4cyMc//nGWLFnC5z73ORYsWEBmctZZZ7HJJptw/vnn89WvfpXBgweTmQwYMGBZn7VVGTx4MD169OATn/gEp5xyCmeddRa77747G220Eaeeeupy+w4fPpwjjzyS559/nvPPP59+/frRr18/Zs6cyd577w1Anz59uPbaaztd4haZ2egY2t2wYcOytkpU0gescVtzPjt1dTNnzmTHHXdsdBjt5sUXX2TEiBE88cQTdOtWdOsfN24cffr04Wtf+1pDYmruGUfEtMwc1pbjHZwgSZK6nKuvvpo999yTiy++eFnS1hXYVCpJkirjT3/6EyeddNJyZeuvvz4PPPDAcmUnn3wyJ5988krHjxs3rp7h1Z2JmyRJqoxdd911uYl11zVdp+5QkiSpi7PGTZVjB3FJ0rrKGjdJkqSKMHGTJEmqCBM3SZLUrIj2/bTVyy+/zAknnMBHPvIRdtppJ4444gj+/Oc/r1bst956K48//vhq3nHnZ+ImSZI6jczk05/+NCNGjOCpp57i8ccf59vf/javvPLKap2nEYnbkiVL6n4NEzdJktRp3HXXXfTs2ZMvfelLy8qGDBnCkiVLOOqoo5aV/eM//iNXXXUVAOeccw477bQTgwcP5mtf+xp//OMfmThxImeffTZDhgzhqaeeYvr06ey1114MHjyYT3/607zxxhsAjBgxgrPOOov99tuPHXfckQcffJBjjz2WQYMGcd555y273rXXXsvw4cMZMmQIX/ziF5claX369Fn2Sq/77ruv7s/HxE2SJHUajz76KLvvvnub958/fz633HILjz32GDNmzOC8887jk5/8JKNGjeLSSy9l+vTpfOQjH+Hkk0/mu9/9LjNmzGDXXXflm9/8YIaC9dZbj7vvvpsvfelLjB49mv/4j//g0Ucf5aqrruL1119n5syZ3HDDDfzhD39g+vTpdO/enZ///OcALFq0iF122YUHHniAfffdt92fx4qcDkSSJFXWRhttRK9evfjCF77AkUceuVytXJMFCxbw5ptvsv/++wMwZswYjjvuuGXbR40aBRST++68885svfXWAOywww7MmTOHe++9l2nTprHHHnsA8Je//GXZy+e7d+/O3/7t39b1HmuZuEmSpE5j55135qabblqpvEePHixdunTZ+rvvvrusfMqUKdx5551cf/31/PCHP+R3v/vdal1z/fXXB6Bbt27LlpvWFy9eTGYyZswYvvOd76x0bK9evejevftqXW9t1LWpNCLOiojHIuLRiPhFRPSKiIER8UBEzIqIGyJivXLf9cv12eX2ATXnObcsfzIiDq1nzJIkqXEOPPBA3nvvPX7yk58sK3vwwQdZsmQJjz/+OO+99x4LFizgzjvvBODtt99mwYIFHHHEEXz/+99f9jqsDTfckIULFwKw8cYbs+mmm3LPPfcAcM011yyrfWuLgw46iJtuuolXX30VKJpnn3vuuXa539VVt8QtIrYBvgwMy8xdgO7ACcB3gcsycxDwBnBaechpwBuZ+VHgsnI/ImKn8ridgcOAH0VEx6W2kiStozLb99MWEcEtt9zCpEmT+MhHPsLOO+/MuHHj6NevH5/5zGcYPHgwJ554IkOHDgVg4cKFHHXUUQwePJj999+fyy67DIATTjiBSy+9lKFDh/LUU08xfvx4zj77bAYPHsz06dO54IIL2vwcdtppJ771rW8xcuRIBg8ezCGHHMJLL7202s+zPUS29Umu7omLxO1+4BPAW8CtwA+AnwMfzszFEbE3MC4zD42I35bL90VED+BloC9wDkBmfqc877L9Wrr2sGHDcurUqXW5LzWer7xaOz6/NeezU1c3c+ZMdtxxx0aH0aU194wjYlpmDmvL8XWrccvMF4DvAc8DLwELgGnAm5m5uNxtLrBNubwNMKc8dnG5/+a15c0cs0xEnBERUyNi6rx589r/hiRJkhqsboMTImJTYDQwEHgT+CVweDO7NlX5NTencrZSvnxB5hXAFVDUuK1ByJKkOrLGUlp79RyccDDwTGbOy8z3gV8BnwQ2KZtCAfoDL5bLc4FtAcrtGwPza8ubOUaSJGmdUc/E7Xlgr4j4UEQEcBDwOHAX8HflPmOACeXyxHKdcvvvsuiANxE4oRx1OhAYBEypY9ySJEmdUt2aSjPzgYi4CXgIWAw8TNGU+Wvg+oj4Vln20/KQnwLXRMRsipq2E8rzPBYRN1IkfYuBMzOz/i8DkyRJ6mTqOgFvZo6FlTohPA0Mb2bfd4HjViwvt10MXNzuAUqSJFWIb06QJEnNatSAkosvvpjrrruO7t27061bN/7zP/+TPffcs9l9x40bR58+ffja177WbnFOnTqVq6++mssvv7wu518bJm6SJKnTuO+++7jtttt46KGHWH/99Xnttdf461//2mHXX7x4McOGDWPYsDZNq9aqzCQz6dat/YYU1PWVV5IkSavjpZdeYosttlj2ztAtttiCfv36MWDAAF577TWgqBEbMWLEsmMeeeQRDjzwQAYNGrTsVVkvvfQS++23H0OGDGGXXXZZ9rqr3/zmN+y222584hOf4KCDDgKKWrszzjiDkSNHcvLJJzN58uTlXlbf3PkBLr30UvbYYw8GDx7M2LFFbeKzzz7LjjvuyD/8wz+w2267MWdO7VS0a88aN0mS1GmMHDmSCy+8kI997GMcfPDBHH/88at8r+iMGTO4//77WbRoEUOHDuXII4/kF7/4BYceeijf+MY3WLJkCe+88w7z5s3j9NNP5+6772bgwIHMnz9/2TmmTZvGvffeS+/evZk8efIqz//oo48ya9YspkyZQmYyatQo7r77brbbbjuefPJJfvazn/GjH/2o3Z+PiZskSeo0+vTpw7Rp07jnnnu46667OP7447nkkktaPWb06NH07t2b3r17c8ABBzBlyhT22GMPPv/5z/P+++9zzDHHMGTIECZPnsx+++3HwIEDAdhss82WnWPUqFH07t27zee/9957ueOOO5a9M/Xtt99m1qxZbLfddmy//fbstdde7fRElmfiJkmSOpXu3bszYsQIRowYwa677sr48ePp0aMHS5cuBeDdd99dbv9iutjl1/fbbz/uvvtufv3rX3PSSSdx9tlns8kmm6y0b5MNNtigxXiaO39mcu655/LFL35xuW3PPvtsq+daWyZuDeBrXyRJat6TTz5Jt27dGDRoEADTp09n++235y9/+QvTpk3j8MMP5+abb17umAkTJnDuueeyaNEiJk+ezCWXXMJzzz3HNttsw+mnn86iRYt46KGH+MY3vsGZZ57JM888s6yptLbWrSXNnb93796cf/75nHjiifTp04cXXniBnj171uWZ1DJxkyRJzWpExcDbb7/NP/3TP/Hmm2/So0cPPvrRj3LFFVcwc+ZMTjvtNL797W+vNDXI8OHDOfLII3n++ec5//zz6devH+PHj+fSSy+lZ8+e9OnTh6uvvpq+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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x7faf6149d668>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x7faf6140dc18>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "dataframe = pd.read_csv('./data/Washington-2016-Summary.csv')\n",
    "\n",
    "# Calculating the number of rides by user type and day of week\n",
    "rides_count = dataframe.groupby(['user_type','day_of_week'])['duration'].count().reset_index()\n",
    "\n",
    "# Creating a data frame of the day of week\n",
    "day_key = pd.DataFrame(['1 - Mon', '2 - Tues', '3 - Wed', '4 - Thurs', '5 - Fri', '6 - Sat', '7 - Sun'], \n",
    "                       index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], \n",
    "                       columns=['day'])\n",
    "\n",
    "# Joining the day of week data frame and the number of rides by user type and day of week\n",
    "data_merged = rides_count.merge(right=day_key, how='inner',left_on='day_of_week',right_index=True, sort=False)\n",
    "\n",
    "# Creating a pivot table to calculate the number of rides by day\n",
    "rides_by_day = data_merged.pivot(index = 'day', columns = 'user_type', values = 'duration')\n",
    "\n",
    "# Plotting the number of rides by user type by day on a bar chart\n",
    "ax = rides_by_day.plot.bar(figsize=(10,6), title = 'Number of Rides by User Type by Day', colormap='winter')\n",
    "ax.set_xlabel(\"Day\")\n",
    "ax.set_ylabel(\"Number of Rides\")\n",
    "\n",
    "\n",
    "# Creating a pivot of the duration by day of week\n",
    "ride_stat_by_day = dataframe.pivot_table(values = 'duration', index =  ['day_of_week'],aggfunc = {np.sum, np.mean, len})\n",
    "\n",
    "# Creating a pivot of the duration by user type by day\n",
    "ride_stat_by_user = dataframe.pivot_table(values = 'duration', index =  ['day_of_week'], \n",
    "                                         columns = ['user_type'],aggfunc = {np.sum, np.mean, len})\n",
    "\n",
    "\n",
    "# Calculating the average of duration by day of week\n",
    "avg_ride_by_day = dataframe.pivot_table(values = 'duration', index =  ['day_of_week'], aggfunc = {np.mean}).reset_index()\n",
    "avg = avg_ride_by_day.merge(right=day_key, how='inner',left_on='day_of_week',right_index=True, sort=False)\n",
    "rides = avg.set_index('day_of_week')\n",
    "\n",
    "# Plotting the average duration by day\n",
    "ax2 = rides.sort_values('day').plot(figsize=(10,6), title = 'Average Duration by Day', \n",
    "                                    colormap='winter', legend = False, grid = True)\n",
    "ax2.set_xlabel(\"Day\")\n",
    "ax2.set_ylabel(\"Average Duration (Minutes)\")\n",
    "\n",
    "# Printing the duration information by day\n",
    "print(ride_stat_by_day)\n",
    "\n",
    "# Printing the duration information by user type by day\n",
    "print(ride_stat_by_user)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id='conclusions'></a>\n",
    "## Conclusions\n",
    "\n",
    "Congratulations on completing the project! This is only a sampling of the data analysis process: from generating questions, wrangling the data, and to exploring the data. Normally, at this point in the data analysis process, you might want to draw conclusions about the data by performing a statistical test or fitting the data to a model for making predictions. There are also a lot of potential analyses that could be performed on the data which are not possible with only the data provided. For example, detailed location data has not been investigated. Where are the most commonly used docks? What are the most common routes? As another example, weather has potential to have a large impact on daily ridership. How much is ridership impacted when there is rain or snow? Are subscribers or customers affected more by changes in weather?\n",
    "\n",
    "**Question 7**: Putting the bike share data aside, think of a topic or field of interest where you would like to be able to apply the techniques of data science. What would you like to be able to learn from your chosen subject?\n",
    "\n",
    "**Answer**: Industry - Agriculture\n",
    "\n",
    "How to conduct farming sustainably to reduce starvation and wastage.\n",
    "\n",
    "> **Tip**: If we want to share the results of our analysis with others, we aren't limited to giving them a copy of the jupyter Notebook (.ipynb) file. We can also export the Notebook output in a form that can be opened even for those without Python installed. From the **File** menu in the upper left, go to the **Download as** submenu. You can then choose a different format that can be viewed more generally, such as HTML (.html) or\n",
    "PDF (.pdf). You may need additional packages or software to perform these exports.\n",
    "\n",
    "> If you are working on this project via the Project Notebook page in the classroom, you can also submit this project directly from the workspace. **Before you do that**, you should save an HTML copy of the completed project to the workspace by running the code cell below. If it worked correctly, the output code should be a 0, and if you click on the jupyter icon in the upper left, you should see your .html document in the workspace directory. Alternatively, you can download the .html copy of your report following the steps in the previous paragraph, then _upload_ the report to the directory (by clicking the jupyter icon).\n",
    "\n",
    "> Either way, once you've gotten the .html report in your workspace, you can complete your submission by clicking on the \"Submit Project\" button to the lower-right hand side of the workspace."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from subprocess import call\n",
    "call(['python', '-m', 'nbconvert', 'Bike_Share_Analysis.ipynb'])"
   ]
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
