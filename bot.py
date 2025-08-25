from flask import Flask, render_template_string, session, jsonify, request
from telegram import Bot
import random

app = Flask(name)
app.secret_key = 'change_this'

TG_BOT_TOKEN = "8235156992:AAF7LFWNbMpI2CzDFD4KRbbNqlQ_JF87Mjk"
bot = Bot(token=TG_BOT_TOKEN)

HTML = '''
<!DOCTYPE html>
<html>
<head>
  <title>Spin Wheel TG Bot</title>
  <link rel="stylesheet" href="/static/style.css">
</head>
<body>
  <header>
    <div><b>{{username}}</b> | ID: {{userid}}</div>
    <div class="coins">💰 <span id="coin">{{coins}}</span></div>
  </header>
  <main>
    <div class="reward"><span id="rewardAmt">{{coins}}</span></div>
    <div>
      <img src="/static/wheel.png" style="width:260px;display:block;margin:16px auto;" id="spinWheel" onclick="spinWheel()" />
      <button onclick="spinWheel()" class="spin-btn">SPIN</button>
    </div>
    <div style="display:flex;justify-content:space-around;">
      <button onclick="alert('Wallet!')">Wallet</button>
      <button onclick="alert('Daily Sign-In!')">Daily Sign-In</button>
      <button onclick="alert('Invite Friends!')">Invite Friends</button>
      <button onclick="alert('Invite History!')">Invite History</button>
    </div>
    <div id="result"></div>
  </main>
  <script src="/static/spinner.js"></script>
</body>
</html>
'''

@app.route('/')
def home():
    # here you can use Telegram authentication or static placeholder
    session.setdefault('username', 'Shivam')
    session.setdefault('userid', '6383718204')
    session.setdefault('coins', 86.89)
    return render_template_string(
        HTML,
        username=session['username'],
        userid=session['userid'],
        coins=session['coins']
    )

@app.route('/spin', methods=['POST'])
def spin():
    last_reward = session.get('last_reward', 0.0)
    outcomes = [
        ("Mini", round(random.uniform(0.01, 0.084), 3)),
        ("Mega", round(random.uniform(0.1, 0.9), 2)),
        ("Coin", round(random.uniform(0.01, 0.85), 2)),
        ("₹100", float(random.randint(1, 9))),
        ("Double", last_reward * 2 if last_reward else round(random.uniform(0.02, 0.15), 2))
    ]
    outcome, reward = random.choice(outcomes)
    session['coins'] = round(session.get('coins', 86.89) + reward, 3)
    session['last_reward'] = reward
    # Optional: send Telegram message
    # bot.send_message(chat_id="YOUR_CHAT_ID", text=f"{outcome}! Won {reward}")
    return jsonify({'reward': reward, 'coins': session['coins'], 'message': f'{outcome}! You won {reward:.2f} coins.'})

if name == 'main':
    app.run(host="0.0.0.0", port=5000, debug=True)
