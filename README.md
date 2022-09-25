# NFT-ForeignAgents

Welcome to the main page of the project NFT-foreign agents of the team "Свой вариант скину в беседу". 

The project is dedicated to solving the problem of partially automating the creation and placement of NFT tokens for foreign agents.

### How to parse data?

0. Install the following requirements:
```
pandas==1.4.3
Wikipedia-API==0.5.4
webdriver-manager==3.8.3
beautifulsoup4==4.11.1
selenium==4.4.3
numpy==1.23.1
translators==5.4.2
```
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
python3 inst-parser/inst.py [profile_link] [path_to_output_csv_file]
```
4. To parse all information about Russian foreign agents from Wikipedia, use the script:
```
python3 wiki-parser/wiki_parser.py
```
### How to write a prompt for a neural network?
0. Install the following requirements:
```
torch==1.8.2+cu111
torchvision==0.9.2+cu111 
torchaudio===0.8.2
transformers==4.22.1
sentencepiece==0.1.97
```
1. Use jupiter notebook summarization.ipynb. Then finalize and specify your request and go generate nft! Good luck!
### How to generate pictures?
0. Install Wombo Dream API (it's NodeJS):
```
npm install dream-api
const WomboDream = require('dream-api');
```
1. To generate an image from text prompt customize the dream-ai.js file.
### How to delete background?
0. Install removebg distro:
```
pip install removebg
```
1. Edit the remove-bg.ipynb to fit your needs.
