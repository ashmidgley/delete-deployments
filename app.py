#!/usr/bin/env python3

__author__ = "Ash Midgley"
__version__ = "0.1.0"
__license__ = "MIT"

import requests
import json

def get_deployments(user, repo):
    response = requests.get(f"https://api.github.com/repos/{user}/{repo}/deployments")
    data = json.loads(response.text) 
    results = []
    for i in range(0, len(data)):
        item = data[i]["id"]
        results.append(item)
    return results

def delete_deployments(user, repo, token):
    print("Deleting deployments")
    for id in ids:
        print(id)
        set_inactive(id, user, repo, token)
        delete_deployment(id, user, repo, token)

def set_inactive(id, user, repo, token):
    url = f"https://api.github.com/repos/{user}/{repo}/deployments/{id}/statuses"
    data = { "state": "inactive" }
    headers = { "Accept": "application/vnd.github.ant-man-preview+json" }
    requests.post(url, data=json.dumps(data), headers=headers, auth=(user, token))

def delete_deployment(id, user, repo, token):
    url = f"https://api.github.com/repos/{user}/{repo}/deployments/{id}"
    requests.delete(url, auth=(user, token))

if __name__ == "__main__":
    user = input("User name: ")
    repo = input("Repo name: ")
    token = input("Token: ")
    ids = get_deployments(user, repo)
    if(len(ids) > 0):
        print(f"{len(ids)} deployments found")
        delete_deployments(user, repo, token)
        print("All done!")
    else:
        print("No deployments to delete!")
 
