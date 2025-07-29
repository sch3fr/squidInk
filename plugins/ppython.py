import requests
import json
import os

GITHUB_TOKEN = "" # Cant commit this with my token
GITHUB_USESRNAME = ""

GRAPHQL_QUERRY = """
query($userName:String!) {
    user(login: $userName){
        contributionsCollection {
            contributionCalendar {
                totalContributions
                    weeks {
                        contributionDays {
                            contributionCount
                            date
                        }
                    }
                }
            }
        }
    }
"""


def fetch_github_contributions(username, token):
    url = 'https://api.github.com/graphql'
    # resp = HTTParty.post(url, body: body.to_json, headers: headers)
    # data = resp.dig('data', 'user', 'contributionsCollection', 'contributionCalendar')