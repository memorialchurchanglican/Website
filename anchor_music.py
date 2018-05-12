import os

# for file in os.listdir('Pew Slip'):
#     print  ("<li><a href=\"Pew Slip\\" + file + "\" alt=\"" + file + "\" target=\"_blank\">" + file + "</a></li>")


for file in os.listdir('assets/images/Carol-Service-2017/'):
    print('<img src=\"assets/images/Carol-Service-2017/' + file + "\"  " + 'style="width:100%">')
