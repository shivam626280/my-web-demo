from flask import Flask, render_template_string, session, jsonify
import random

app = Flask(__name__)
app.secret_key = 'somesecret'

HTML = '''
<!DOCTYPE html>
<html>
<head>
  <title>Spin Wheel Game</title>
  <link rel="stylesheet" href="/static/style.css">
</head>
<body>
<header>
  <div>
    <span class="avatar"></span>
    <b id="username">Shivam</b> | <span id="userid">ID: 6383718204</span>
  </div>
  <div class="coins">💰 <span id="coin">{{coins}}</span></div>
</header>
<main>
  <div class="reward"><span id="rewardAmt">{{coins}}</span></div>
  <div>
    <img src="/static/wheel.png" id="spinWheel" onclick="spinWheel()" style="width:260px;display:block;margin:20px auto;" />
    <button onclick="spinWheel()" class="spin-btn">SPIN</button>
  </div>
  <div style="display:flex;justify-content:space-around;padding:16px 0;">
    <button onclick="alert('Wallet coming soon!')">Wallet</button>
    <button onclick="alert('Daily Sign-In')">Daily Sign-In</button>
    <button onclick="alert('Invite Friends')">Invite Friends</button>
    <button onclick="alert('Invite History')">Invite History</button>
  </div>
  <div id="result"></div>
</main>
<script src="/static/spinner.js"></script>
</body>
</html>
'''

@app.route('/')
def home():
    session.setdefault('coins', 86.89)
    return render_template_string(HTML, coins=session['coins'])

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
    message = f"{outcome}! You won {reward:.2f} coins." if outcome != "Double" else f"Double! You won double your last reward: {reward:.2f} coins."
    return jsonify({'reward': reward, 'coins': session['coins'], 'message': message})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
