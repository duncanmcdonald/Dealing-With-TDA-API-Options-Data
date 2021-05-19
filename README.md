# Dealing-With-TDA-API-Options-Data

TD Ameritrade's API is very popular for those of us that are interested in trying to build their own trading tools. The TDA API is also nice in that it supports option trading and is a good source of data for current option chains. However, the method used, get_options_chain, returns a JSON object that has a pretty complicated structure. It's a nested dictionary that mixes dicts and lists, where (at least) one of the lists has a single member that is a dict. The only way I found to completely decompose it to (key, value) pairs is to use recursion. 
I've created a couple of Python examples that will:

* Print out on your console every key/value pair in the JSON object

* Write the retrieved JSON object to a JSON file on your local machine

If you are looking for other working code examples, I have found that these GitHub projects are a good source of working code modules for the TDA API:

[td-ameritrade-python-api](https://github.com/areed1192/td-ameritrade-python-api). Usefule code for common operations.

[Options_Data_Science](https://github.com/yugedata/Options_Data_Science). Scrapes TDA option data and puts it in an SQLite database so you can build your own historical data.

There are other projects out there, but I have only tested/used the above.

Another thing to mention. TD Ameritrade limits API requests to 120/minute. If you exceed that rate their servers will start refusing the connection and return an error message about how you have exceeded the transaction limit. These examples are only one-shot so you won't run into that problem here.

Last, it seems that dealing with authorization (OAuth) is a common stumbling block when getting started with the TDA API. Try the example at [td-ameritrade-python-api](https://github.com/areed1192/td-ameritrade-python-api) to get started.

Feedback or advice? dmcdonald999@gmail.com Reddit: u/Duncan999
