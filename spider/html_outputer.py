#encoding:utf-8
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w', encoding='utf-8')

        fout.write('<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table border='2'>")

        for data in self.datas:
            print(data['summary'].encode('utf-8'))
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</table>")

        fout.close()
