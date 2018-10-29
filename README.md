# monastery
Intelligent Knowledge Base

I really want to make this in common lisp however, for the sake of shipping something in the duration of the hackathon, I will deploy this as a Python-Flask application on Heroku

# To Run

```bash
gunicorn app:app
```

# Description

This app is a Python Flask application that serves data to the frontend (can be upgraded to a React.js application)

The database is a NoSQL database for flexibility and easy introduction of new fields

We're using mLab MongoDB Heroku plugin and the ideal structure of an object in the collection is

```json
{
	"author": "Yev Barkalov",
	// A quote
	"statement": "Water is wet",
	"implications": [
		"water can be dry",
		"water of any mass is wet"
	],
	"concepts": [
		"water",
		"wetness"
	]
}
```

[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fyevbar%2Fmonastery.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fyevbar%2Fmonastery?ref=badge_shield)
