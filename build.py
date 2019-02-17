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
