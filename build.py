pages = [
    {
        "filename": "content/index.html",
        "output": "docs/index.html",
        "title": "Home",
    },
    {
        "filename": "content/about.html",
        "output": "docs/about.html",
        "title": "About Me",
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


def apply_template(template, page_title, file_name):
    index_content = open(file_name).read()
    finished_index_page = template.replace("{{content}}", index_content)
    finished_index_page = finished_index_page.replace("{{title}}", page_title)
    return finished_index_page
    
def print_page(template, page):
    file_name = page['filename']
    page_output = page['output']
    page_title = page['title']
    
    page_html = apply_template(template, page_title, file_name)
    open(page_output, "w+").write(page_html)
    
def main():
    template = open("templates/base.html").read()
    for page in pages:
        print_page(template, page)
    
if __name__ == "__main__":
    main()
