
# Data Setup 

Utilities/AnonymisedDatasets already has pre-anonymised data based on originally collected data. If you have the original data file and would like to add your own, you have two options:

- After adding the, run setup.py, no command line arguments, which will reanonymise the data with your additions. After setup.py finishes running, you are ready to go.
- If you wouldn't like to anonymise your data, you'll still need to create the AnonymisedDatasets directory; instead, run setup.py -NO-ANON. All data and network formations will use real names, but you'll still be able to create an anonymous dictionary mapping with the anonymisation tools provided. More on this below.

# Anonymising a single dictionary/ list of names

If you want to anonymise data in a single use case, simple import the "anonymise" function from anonymisationTools.py. Pass in your data to this function, and it will return:

- A replica of your data, with the strings replaced by random name strings
- A dictionary that maps the randomly generated name to the original string in your passed in data 

At the moment, you may pass in either one of: String, Dictionary, or List data types