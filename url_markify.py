#!/usr/bin/env python3
"""Generates a nicely formatted website link in Markdown syntax.

Based on:
https://hackersandslackers.com/scraping-urls-with-beautifulsoup/
"""


__author__ = "Phixyn"
__version__ = "1.0.0"


import sys
import urllib.request
import pyperclip
from urllib.error import URLError
from bs4 import BeautifulSoup


USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0"


class Website:
    """Represents a website."""

    def __init__(self, title, description, url, site_name):
        """Constructor for website.
        
        Args:
            title (string): The website's title.
            description (string): Description of the website, usually found
                                  in a meta tag.
            url (string): The URL of the website.
            site_name (string): TODO
        """
        self.title = title
        self.description = description
        self.url = url
        self.site_name = site_name

    def __str__(self):
        """Returns a string representation of a website object.
        
        Returns:
            A formatted string with the title and url of the website, using
            Markdown syntax. For example:
            "[Phixyn - Blog](https://phixyn.com/blog)"
        """
        # With site name
        # return "[{site_name} - {title}]({url})".format(
        #     title=self.title,
        #     url=self.url,
        #     site_name=self.site_name
        # )
        # Without site name
        return "[{title}]({url})".format(title=self.title, url=self.url)


def get_raw_html(url):
    """Makes a simple HTTP GET request to the specified URL and returns the
    raw HTML response, if successful.
    
    Args:
        url (string): The URL of the webpage to get the HTML from.

    Returns:
        The response, in bytes, from the urllib request. This contains the
        raw HTML, which can be passed to a HTML parser. If the request fails,
        an error is printed and None is returned.
    """
    # TODO handle POST too?
    http_request = urllib.request.Request(url)
    http_request.add_header("User-Agent", USER_AGENT)
    raw_html = None

    try:
        with urllib.request.urlopen(http_request) as response:
            raw_html = response.read()
    except URLError as e:
        if hasattr(e, "reason"):
            print("Failed to reach server.")
            print("Reason: ", e.reason)
        # HTTPError
        elif hasattr(e, "code"):
            print("The server couldn't fullfil the request.")
            print("HTTP error code: ", e.code)

    return raw_html


def get_title(html):
    """Attempts to get the webpage's title.

    Tries to get the content of the <title> tag, if one is present. Falls back
    to the webpage's first <h1> tag if no <title> tag or string is found.

    Args:
        html (BeautifulSoup): BeautifulSoup object with a webpage's parsed HTML.

    Returns:
        A string containing the webpage's title, if one is found. If no title
        is found, then a default string is returned.
    """
    if html.title.string:
        return html.title.string
    
    h1_element = html.find("h1")
    if h1_element:
        return h1_element.text.strip()
    else:
        return "No title found."


def get_description(html):
    """Attempts to get the webpage's description.

    Looks for a <meta> tag containing the "og:description" property. Falls
    back to the webpage's first paragraph (<p>) element if the desired meta
    tag is not found.

    Args:
        html (BeautifulSoup): BeautifulSoup object with a webpage's parsed HTML.

    Returns:
        A string containing the webpage's description, if one is found. If no
        description is found, then a default string is returned.
    """
    description_meta_tag = html.find("meta", property="og:description")
    if description_meta_tag:
        return description_meta_tag.get("content")

    paragraph_element = html.find("p")
    if paragraph_element:
        return paragraph_element.text.strip()
    else:
        return "No description found."


def get_site_name(html, url):
    """Attempts to get the website's base name.

    Looks for a <meta> tag containing the "og:site_name" property. If the
    desired meta tag is not found, the website's URL is used to get the
    best possible site name. However, this fallback is not always reliable,
    especially when the URL contains a subdomain.

    Args:
        html (BeautifulSoup): BeautifulSoup object with a webpage's parsed HTML.
        url (string): the webpage's URL, used as a fallback to get the website's
                      name.

    Returns:
        A string containing the website's name, if one is found. If no name
        is found, then a default string is returned.
    """
    site_name_meta_tag = html.find("meta", property="og:site_name")
    if site_name_meta_tag:
        return html.find("meta", property="og:site_name").get("content")

    site_name = url.split("//")[1].rsplit(".")[0]
    if not site_name or site_name == "":
        return "No site name found."
    else:
        return site_name


def scrape(url):
    """Scrapes the webpage at the specified URL to gather data about it. This
    data can be used to generate website previews.

    Args:
        url (string): the URL of the webpage to be scraped.

    Returns:
        TODO
    """
    raw_html = get_raw_html(url)
    if not raw_html:
        print("Error getting raw HTML.")
        # sys.exit(1)
        return

    soup = BeautifulSoup(raw_html, "html.parser")
    webpage_preview_data = {
        "title": get_title(soup),
        "description": get_description(soup),
        "url": url,
        "site_name": get_site_name(soup, url)
    }

    return webpage_preview_data


if __name__ == "__main__":
    print("Welcome to the library.\n")
    print("Enter the links you want to save with us.\n")
    websites = []
    try:
        while True:
            url = input("> URL: ")
            
            # Get website data
            data = scrape(url)

            website = Website(data["title"], data["description"], data["url"], data["site_name"])
            print(website)
            pyperclip.copy(str(website))
    except KeyboardInterrupt:
        print("\n\nExiting the library. Have a nice day!\n")
        sys.exit(0)
