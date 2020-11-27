import discord
from discord.ext import commands
import asyncio

client = discord.Client()
client = commands.Bot(command_prefix='!')
maximum=5
mem=1
token = "Nzc2NjQ0MDY2MDI4MDI3OTE0.X634Jg.z0jR8SbclQLyE9r7xI9_h72zxeI"

mem=1
@client.event
async def on_ready():
   print("준비완료됨!")
   print("다음으로 로그인 됩니다")
   print(client.user.name)
   print(client.user.id)



@client.event
async def on_message(message):
  if message.content.startswith("!help"):
    embed = discord.Embed(title= "도움말", description="명령어와 사용법을 확인할 수 있습니다", color = 0x00ff56)
    embed.add_field(name = "!준비", value="계획표를 작성할수 있습니다. !준비/주제/시간/장소/최대인원 순으로 입력해주세요(/는 띄어쓰기입니다.)",inline = False)
    embed.add_field(name = "!참가,!취소", value= "등록된 계획에 참가, 혹은 참가취소를 할 수 있습니다", inline = False)  
    embed.add_field(name = "!help", value="당신이 보고 있는 그래도입니다",inline = False)
    embed.set_footer(text="처음 만든 작으로 실수가 많고 부족한 부분이 많습니다.이해해주시고 이용해주세요.")
    await message.channel.send(embed=embed)
  

  if message.content.startswith("!준비"):
    if message.author.bot:
      return None
    else:
     msg = message.content
     what = msg.split()[1] 
     when = msg.split()[2] 
     where = msg.split()[3] 
     maxi = msg.split()[4]
     embed = discord.Embed(title= "새로운 계획", description="새로 제안된 계획입니다", color = 0x2efec8)
     embed.add_field(name = "무엇을 하나요?", value= what,inline = True)
     embed.add_field(name="시간", value=when, inline= True)
     embed.add_field(name="장소", value= where, inline= True)
     embed.add_field(name="최대인원", value= maxi, inline= True)
     await message.channel.send("새로운계획", embed=embed)
  global mem
  if message.content.startswith("!참가"):
    mem+=1
    await message.channel.send('''=========
    확인되었습니다
    현재인원: '''+str(mem)+'''
    ==========''')

  if message.content.startswith("!취소"):
   mem-=1
   await message.channel.send('''=========
    확인되었습니다
    현재인원: '''+str(mem)+'''
    ==========''')
   



client.run(token)