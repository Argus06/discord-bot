import discord
from discord.ext import commands
from datetime import datetime
from pytz import timezone
import os
from dotenv import load_dotenv

load_dotenv() # .envファイルを読み込む

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = 1336776924323774565 # 送信先チャンネルID

# Intents設定
intents = discord.Intents.default()
intents.message_content = True  # 🔥 メッセージ内容を取得する権限を有効化

# Botインスタンスを作成
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ ログインしました: {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send(f"こんにちは、{ctx.author.mention}！")

# !now コマンドの実装
@bot.command()
async def now(ctx):
    # 日本時間で現在時刻を取得
    now = datetime.now(timezone("Asia/Tokyo"))
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")  # フォーマット: YYYY-MM-DD HH:MM:SS
    await ctx.send(f"現在の時間は {current_time} （日本時間）です！")

bot.run(TOKEN)