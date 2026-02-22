import os
from flask import Flask, redirect, request

app = Flask(__name__)

# This is the part that creates the link
@app.route('/join')
def join_server():
    # 1. Get the server ID from the token in the link
    server_id = request.args.get('token', '')
    
    if not server_id:
        return "❌ Error: No server ID provided.", 400
    
    # 2. Your Roblox Game ID (Steal a Brainrot)
    place_id = "4483381587"
    
    # 3. Create the special link that opens Roblox
    roblox_link = f"roblox://placeId={place_id}&gameInstanceId={server_id}"
    
    # 4. Create a backup web link
    web_link = f"https://www.roblox.com/games/start?placeId={place_id}&jobId={server_id}"
    
    # 5. Show a simple page with the link
    html = f"""
    <html>
    <head><title>Joining Brainrot Server...</title></head>
    <body style="font-family: sans-serif; text-align: center; padding: 50px;">
        <h2>🎯 Brainrot Server Found!</h2>
        <p>Server ID: <code>{server_id}</code></p>
        <p>Click the button to join:</p>
        <a href="{roblox_link}" style="background: #00b894; color: white; padding: 15px 30px; text-decoration: none; border-radius: 5px; display: inline-block; margin: 10px;">🚀 Open Roblox</a>
        <p style="margin-top: 30px; font-size: 12px; color: #666;">
            <a href="{web_link}">Click here if the button doesn't work</a>
        </p>
    </body>
    </html>
    """
    return html

# This keeps the website running
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
