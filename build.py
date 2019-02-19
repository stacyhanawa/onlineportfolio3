def main():

    top = open("templates/top.html").read()
    content = open("content/about.html").read()
    bottom = open("templates/bottom.html").read()
    full = top + content + bottom 
    open("docs/about.html", "w+").write(full)

    top = open("templates/top.html").read()
    content = open("content/contact.html").read()
    bottom = open("templates/bottom.html").read()
    full = top + content + bottom 
    open("docs/contact.html", "w+").write(full)

    top = open("templates/top.html").read()
    content = open("content/index.html").read()
    bottom = open("templates/bottom.html").read()
    full = top + content + bottom 
    open("docs/index.html", "w+").write(full)

    top = open("templates/top.html").read()
    content = open("content/post.html").read()
    bottom = open("templates/bottom.html").read()
    full = top + content + bottom 
    open("docs/post.html", "w+").write(full)
    
    pages = [
    {
        "filename": "content/about.html",
        "output": "docs/about.html",
        "title": "About Me",
    },
    {
        "filename": "content/index.html",
        "output": "docs/index.html",
        "title": "Homepage",
    },
    {
        "filename": "content/post.html",
        "output": "docs/post.html",
        "title": "Good Food",
    },
    {
        "filename": "content/contact.html",
        "output": "docs/contact.html",
        "title": "Contact",
    },
    ]
    
    for page in pages:
        print(page)
    
    page_title = page['title']
    print(page_title)
    
if __name__ == "__main__":
    main()
