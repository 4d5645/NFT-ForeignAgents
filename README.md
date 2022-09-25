# NFT-ForeignAgents

Welcome to the main page of the project NFT-foreign agents of the team "Свой вариант скину в беседу". 

The project is dedicated to solving the problem of partially automating the creation and placement of NFT tokens for foreign agents.

To use parsers, install the following requirements:

```
pandas==1.4.3
Wikipedia-API==0.5.4
webdriver-manager==3.8.3
beautifulsoup4==4.11.1
selenium==4.4.3
numpy==1.23.1
translators==5.4.2
```
### How to parse data?
1. Choose a foreign agent
2. Find their telegram channel or profile on a banned social network with pictures
3. Download json from the telegram channel according to the [instructions](https://www.mobigyaan.com/telegram-4-9-1-update). 
To get all messages of the author of the channel since February 24, use the script tgchannel_parser.py:
```
python3 tgchannel_parser/tgchannel_parser.py [path_to_json_file] [path_to_output_csv_file]
```
Example with Michael Nucky:
```
python3 tgchannel_parser/tgchannel_parser.py tgchannel_parser/macknack.json tgchannel_parser/macknack.csv 
```
To get descriptions for the latest posts on a banned social network with pictures, use the following script:

```
python3 inst-parser/inst.py [profile nickname] [path_to_output_csv_file]

```


