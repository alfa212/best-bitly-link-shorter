# Bitly url shorterer

Service for working with bitly.com-API

### How to install

An API key is required to work with the service. Obtain your API key from bitly.com and specify it in the BITLY_TOKEN variable in the .env file at the root of the project:

```
BITLY_TOKEN='your-api-key'
```

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Usage

#### Link shortening

```
main.py https://your_link.ru
```
##### Example
```
main.py https://yandex.ru
```

#### Bitly-link statistics

```
main.py https://your_bit_link.ru
```
##### Example
```
main.py https://bit.ly/3FbWwmi
```

### Project Goals

The code is written just for fun.
