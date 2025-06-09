#!/usr/bin/python3
"""Module to make a GET request to a URL and print the response."""
import requests
import csv


def fetch_and_print_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: {}".format(r.status_code))
    my_post = r.json()
    for post in my_post:
        print(post["title"])


def fetch_and_save_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    posts = r.json()
    fieldnames = ["userId", "id", "title", "body"]
    if r.status_code == 200:
        with open("posts.csv", mode="w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for post in posts:
                writer.writerow(post)
