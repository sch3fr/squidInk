import requests
import json
import os
from datetime import datetime

GITHUB_TOKEN = "censored :)" # Cant commit this with my token
GITHUB_USERNAME = "censored :)"

GRAPHQL_QUERY = """
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
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    body = {
        'query': GRAPHQL_QUERY,
        'variables': {'userName': username}
    }

    try:
        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()
        data = response.json()
        
        contributions_data = data.get('data', {}).get('user', {}).get('contributionsCollection', {}).get('contributionCalendar', {})

        total_contributions = contributions_data.get('totalContributions')
        weeks_data = contributions_data.get('weeks', [])

        return {
            'total': total_contributions,
            'commits': weeks_data
        }

    except requests.exceptions.RequestException as e:
        print(f"Error calling the Github API: {e}")
        return None
    
def calculate_github_stats(all_days_raw):
    sorted_days = sorted(all_days_raw, key=lambda day: datetime.strptime(day['date'], '%Y-%m-%d'))

    max_contributions = 0
    if sorted_days:
        contributions_count = [day['contributionCount'] for day in sorted_days]
        max_contributions = max(contributions_count)

    average_contributions = 0.0
    if sorted_days:
        total_sum = sum(day['contributionCount'] for day in sorted_days)
        average_contributions = round(total_sum / len(sorted_days), 2)

    longest_streak = 0
    current_streak_longest = 0
    if sorted_days:
        longest = 0
        current = 0
        for day in sorted_days:
            if day['contributionCount']>0:
                current += 1
                longest = max(longest, current)
            else:
                current = 0
        longest_streak = longest

    current_streak_actual = 0
    if sorted_days:
        for day in reversed(sorted_days):
            if day['contributionCount'] > 0:
                current_streak_actual += 1
            else:
                current_streak_actual = 0
                break

    return{
        'longest_streak': longest_streak,
        'current_strak': current_streak_actual,
        'current_strek': current_streak_actual,
        'max_contributions': max_contributions,
        'average_contributions': average_contributions
    }



if __name__ == "__main__":
    print("Loading GitHub data...")
    contributions = fetch_github_contributions(GITHUB_USERNAME, GITHUB_TOKEN)

    if contributions:
        print("\nData succesfully loaded:")
        # debug print, ignore
        # print(json.dumps(contributions, indent=2))

        # Access total contributions
        total_contributions = contributions.get('total')
        weeks = contributions.get('commits', [])

        print(f"Total contributions: {total_contributions}")
        print(f"Number of valid weeks: {len(weeks)}")

        if weeks:
            # print this week
            print("\nThis week:")
            for day in weeks[0].get('contributionDays', []):
                print(f"  Date: {day['date']}, Contributions: {day['contributionCount']}")
        
        all_contribution_days = []
        for week in weeks:
            all_contribution_days.extend(week.get('contributionDays', []))

        stats = calculate_github_stats(all_contribution_days)
        print(stats)

    else:
        print("Could not load contribuition data.")

