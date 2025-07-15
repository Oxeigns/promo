from pyrogram import Client , filters 
from pyrogram message.type import message

app=Client(''mybot'' ,
           api_id= '125628' ,
           api_hash= ' 125272' ,
           bot_token= 'wywywu' ,
          )
app. on_message (filter.command(''start''))
async def start_handler(Client , message : message)
await message.reply(''hlo bot start ho hya) 
app.run()
                 
        
