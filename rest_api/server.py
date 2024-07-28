from dotenv import load_dotenv
from flask import Flask, request, jsonify
from content.creator import get_fun_things_to_do
from flask_cors import CORS

load_dotenv()

mockData = {
    "activities": [
        {
            "date": "27th Jul",
            "description": "Experience all things sake at Sake Meguri, featuring over 200 brands and breweries from Japan. Enjoy up to 60% off on products.",
            "location": "1 Expo Drive, Singapore EXPO, Foyer 1, Singapore 486150",
            "ticket": "$58",
            "title": "Sake Meguri"
        },
        {
            "date": "27th-28th Jul",
            "description": "Anime fanatics can meet popular guest cosplayers and shop exclusive merchandise at AFA Creators Super Fest Singapore 2024.",
            "location": "1 Expo Drive, Singapore EXPO, Hall 3, Singapore 486150",
            "ticket": "From $19",
            "title": "AFA Creators Super Fest Singapore 2024"
        },
        {
            "date": "27th-28th Jul & 3rd-4th Aug",
            "description": "Enjoy a Fast and Furious weekend at Sprint Fest 2024 with car races, magic performances, and racing simulators for all ages.",
            "location": "54 Palawan Beach Walk, Palawan Green, Singapore 098233",
            "ticket": "Free",
            "title": "Sprint Fest 2024"
        },
        {
            "date": "27th Jul",
            "description": "Watch 'Big Hero 6' under the stars at Movies Under The Stars event. Kids under 12 watch for free.",
            "location": "20 Lengkok Bahru, Enabling Village Amphitheater, #02-06, Singapore 159053",
            "ticket": "$6",
            "title": "Movies Under The Stars"
        },
        {
            "date": "26th-28th Jul",
            "description": "Stock up on makeup and skincare essentials at Beauty Fiesta with products up to 90% off from top brands.",
            "location": "1 Expo Drive, Singapore EXPO, Hall 6B, Singapore 486150",
            "ticket": "From $19",
            "title": "Beauty Fiesta"
        },
        {
            "date": "27th-28th Jul",
            "description": "Indulge in different prata gravies and enjoy free-flow prata at The Prata Festival.",
            "location": "60 Springside Walk, Semma Bistro, #01-19, Singapore 786020",
            "ticket": "From $15",
            "title": "The Prata Festival"
        },
        {
            "date": "26th-28th Jul",
            "description": "Attend workshops, watch live performances, and get inked by guest artists at The Lion’s Gate Singapore Tattoo Convention.",
            "location": "1 Expo Drive, Singapore EXPO, Hall 4B, Singapore 486150",
            "ticket": "From $30",
            "title": "The Lion’s Gate Singapore Tattoo Convention"
        },
        {
            "date": "Now till 31st Aug",
            "description": "Try local-flavored treats at Tim Hortons Everyday Heroes and participate in a giveaway for yummy treats.",
            "location": "Check Tim Hortons outlets",
            "ticket": "",
            "title": "Tim Hortons Everyday Heroes"
        },
        {
            "date": "Now till 28th Jul",
            "description": "Enjoy deals and discounts on activities and F&B at The Palawan @ Sentosa First Birthday Celebration.",
            "location": "54 Palawan Beach Walk, Singapore 098233",
            "ticket": "",
            "title": "The Palawan @ Sentosa First Birthday Celebration"
        },
        {
            "date": "10th-28th Jul",
            "description": "Laugh out loud at Kumar Uncut comedy show featuring drag queens and lip-syncing performances.",
            "location": "10 Bayfront Avenue, Marina Bay Sands Theatre, Singapore 018956",
            "ticket": "From $58",
            "title": "Kumar Uncut"
        },
        {
            "date": "From 12th Jul",
            "description": "Experience the gorgeous Impressions of Monet exhibition at Gardens by the Bay, bringing Claude Monet's garden to life.",
            "location": "18 Marina Gardens Dr, Singapore 018953",
            "ticket": "",
            "title": "Impressions of Monet"
        }
    ],
    "source": "https://thesmartlocal.com/",
    "summary": "Exciting events and activities happening in Singapore this weekend, from sake festivals to tattoo conventions!"
}

app = Flask(__name__)

CORS(app)

@app.route("/fun_things", methods=["GET"])
def get_fun_activities():
    activities = get_fun_things_to_do()
    return jsonify(activities.to_dict())

@app.route("/mock", methods=["GET"])
def get_mock_data():
    return jsonify(mockData)

def run_rest_server():
    app.run(host="0.0.0.0", port= 9000, debug=True)
