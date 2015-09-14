from web import form, template, internalerror, debugerror, application
import tagger

render = template.render('templates/')

urls = (
    '/', 'index'
)

app = application(urls, globals())

myform = form.Form(
    form.Textarea('paragraph'),
)

class index:
    def GET(self):
        form = myform()
        return render.index(form)

    def POST(self):
        form = myform()
        if not form.validates():
            return render.index(form)
        else:
            para = form["paragraph"].value;
            tags = tagger.tagger(para)

            # Set maximum number of tags
            max_tags = 12
            if len(tags) > max_tags:
                tags = tags[:max_tags]

            # Return tags are unicode. Convert them
            # into web-friendly utf-8
            tags = [x.encode("utf-8") for x in tags]
            op = "<ol>\n"
            for tag in tags:
                op += "\t<li>" + tag + "</li>\n"
            op += "</ol>"
            return op

if __name__ == "__main__":
    internalerror = debugerror
    app.run()
