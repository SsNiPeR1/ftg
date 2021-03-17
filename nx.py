import os

from random import choice

import string

name = "".join(choice(string.ascii_uppercase + string.ascii_letters + string.digits) for _ in range(8))

await reply.download_media(f"{name}.tgs")

os.system(f"lottie_convert.py {name}.tgs {name}.json")

json = open(f"{name}.json","r")

jsn = json.read()

json.close()

jsn = jsn.replace("[0]", "[30]").replace("[1]", "[30]").replace("[2]", "[30]").replace("[3]", "[30]").replace("[4]", "[30]").replace("[5]", "[30]").replace("[6]", "[30]").replace("[7]", "[30]").replace("[8]", "[30]").replace("[9]", "[30]").replace("[10]", "[30]").replace("[11]", "[30]").replace("[12]", "[30]").replace("[13]", "[30]").replace("[14]", "[30]").replace("[15]", "[30]").replace("[16]", "[30]").replace("[17]", "[30]").replace("[18]", "[30]").replace("[19]", "[30]").replace("[20]", "[30]").replace("[21]", "[30]").replace("[22]", "[30]").replace("[23]", "[30]").replace("[24]", "[30]").replace("[25]", "[30]").replace("[26]", "[30]").replace("[27]", "[30]").replace("[28]", "[30]").replace("[29]", "[30]")

open(f"{name}.json","w").write(jsn)

os.system(f"lottie_convert.py {name}.json {name}.tgs")

msg = await reply.reply(file=f"{name}.tgs")

if msg.media.document.mime_type == 'application/x-bad-tgsticker':

 await msg.delete()

os.remove(f"{name}.json")

os.remove(f"{name}.tgs")

await message.delete()

import os

from random import choice

import string

name = "".join(choice(string.ascii_uppercase + string.ascii_letters + string.digits) for _ in range(8))

await reply.download_media(f"{name}.tgs")

os.system(f"lottie_convert.py {name}.tgs {name}.json")

json = open(f"{name}.json","r")

jsn = json.read()

json.close()

jsn = jsn.replace("8","4").replace("7","4")#.replace("3","4")

open(f"{name}.json","w").write(jsn)

os.system(f"lottie_convert.py {name}.json {name}.tgs")

msg = await reply.reply(file=f"{name}.tgs")

if msg.media.document.mime_type == 'application/x-bad-tgsticker':

 await msg.delete()

os.remove(f"{name}.json")

os.remove(f"{name}.tgs")

import os

from random import choice

import string

name = "".join(choice(string.ascii_uppercase + string.ascii_letters + string.digits) for _ in range(8))

await reply.download_media(f"{name}.tgs")

os.system(f"lottie_convert.py {name}.tgs {name}.json")

json = open(f"{name}.json","r")

jsn = json.read()

json.close()

jsn = jsn.replace("8","2").replace("6","7").replace("3","4").replace("[0]","[52]").replace("[5]","[0]")

open(f"{name}.json","w").write(jsn)

os.system(f"lottie_convert.py {name}.json {name}.tgs")

msg = await reply.reply(file=f"{name}.tgs")

if msg.media.document.mime_type == 'application/x-bad-tgsticker':

 await msg.delete()

os.remove(f"{name}.json")

os.remove(f"{name}.tgs")
