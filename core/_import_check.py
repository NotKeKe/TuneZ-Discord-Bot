try:  
    import nacl.secret  
    import nacl.utils  
except ImportError as e:  
    print(f"Failed to import PyNaCl: {e}")

try:
    import discord
except ImportError as e:
    print(f"Failed to import Discord.py: {e}")

# 檢查 ffempg
try:  
    source = discord.FFmpegPCMAudio("nonexistent.mp3")  
except discord.ClientException as e:  
    if "was not found" in str(e):  
        print("FFmpeg was not found.")  
    else:  
        print(f"Failed to import FFmpeg: {e}")