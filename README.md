# unemployment-inclass-summer-2023


## Setup

Obtain an [Yelp API Key](https://www.yelp.com/developers/v3/manage_app). A normal key is limited to display 50 items. Then create a file called ".env" and place it inside (like the following example):
```sh
# this is the ".env" file (in the root directory of the repo)

API_KEY="____________"
```



Create a virtual environment:
```sh
conda create -n restaurant-env python=3.10
```

```sh
conda activate restaurant-env
```

Install third-party packages:

```sh
pip install -r requirements.txt
```

## Usage

Run the report:

```sh
python app/restaurant.py

python -m app.restaurant
```


Run the web_app:
```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or try a ".env" file approach
export FLASK_APP=web_app
flask run
```


## Testing

Run tests:

```sh
pytest
```


## Deployment

## [Deployment Guide](/DEPLOYING.md)
