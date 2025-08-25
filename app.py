from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>₹300 Reward</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { background: #f3f3f3; font-family: 'Inter', Arial, sans-serif; color: #222; margin: 0; }
        .container {
            max-width: 420px;
            margin: 40px auto 0 auto;
            background: #fff;
            border-radius: 24px;
            box-shadow: 0 4px 24px #0001;
            padding-bottom: 80px; /* make page scrollable */
            min-height: 110vh;   /* for scroll event to work */
        }
        .card-top {
            background: #fe73a3;
            padding: 32px 0 32px 0;
            border-radius: 24px 24px 12px 12px;
            display:flex; flex-direction:column; align-items:center; justify-content:center;
        }
        .reward-label { font-weight: 700; font-size: 40px; margin: 0 0 5px 0; letter-spacing: -1px; text-align:center; }
        .steps-box { width: 90%; margin: 22px auto 0 auto; text-align: center;}
        .steps-box h2 { font-size: 21px; margin: 8px 0 3px 0; }
        .steps-box p { font-size: 15px; margin: 6px; color: #555; }
        .btn-list { margin: 15px 0; }
        .join-btn {
            display: flex;
            align-items: center;
            background: #18b47e;
            color: #fff;
            border-radius: 10px;
            width: 95%;
            max-width: 340px;
            font-size: 17px;
            font-weight: 500;
            border: none;
            outline: none;
            margin: 8px auto;
            padding: 13px 0;
            justify-content: center;
            cursor: pointer;
            transition: background 0.2s, opacity 0.6s;
        }
        .hidden-btn {
            opacity: 0;
            pointer-events: none;
            height: 0;
            overflow: hidden;
            margin-top: 0;
            margin-bottom: 0;
            padding-top: 0;
            padding-bottom: 0;
        }
        .join-btn.visible {
            opacity: 1;
            pointer-events: auto;
            height: auto;
            margin: 8px auto;
            padding: 13px 0;
        }
        .join-btn:disabled { background: #a2d1bc; color: #fff; cursor: not-allowed;}
        .lock-btn, .claim-btn {
            display: block;
            width: 95%;
            max-width: 340px;
            margin: 14px auto 0 auto;
            padding: 12px 0;
            border-radius: 10px;
            color: #556;
            background: #e4ecf4;
            border: none;
            font-size: 16px;
            font-weight: 500;
        }
        .claim-btn {
            background: #8594af;
            color: #fff;
            margin-top: 9px;
        }
        .claim-btn:disabled {
            background: #e4ecf4;
            color: #bbb;
            cursor: not-allowed;
        }
        #withdraw-section { display: none; width: 95%; margin: 18px auto 0 auto;}
        input[type=text] {
            width: 70%;
            padding: 11px 3px;
            margin: 10px 0 8px 0;
            border: 1px solid #d9e6f5;
            border-radius: 6px;
            font-size: 16px;
            outline: none;
        }
        .success-msg {
            color: #18b47e;
            background: #e3f8ee;
            font-weight: bold;
            border-radius: 6px;
            padding: 10px 0;
            margin: 14px 0 2px 0;
            font-size: 15px;
        }
        .disc-box {
            margin: 12px 0 0 0;
            text-align: center;
            width: 98%;
        }
        .step-desc { color: #444; font-size: 15px; margin-top:14px; }
        .disclaimer {
            color: #ffae00;
            font-size: 14px;
            margin-top: 9px;
            background: #fff9e5;
            padding: 8px;
            border-radius: 8px;
        }
    </style>
</head>
<body>
<div class="container">
    <div class="card-top">
        <div class="reward-label">₹300<br>INSTANT</div>
    </div>
    <div class="steps-box">
        <h2>Join All Channels to Unlock Reward</h2>
        <p>Complete all steps to unlock your ₹300 UPI reward!</p>
    </div>
    <div class="btn-list">
        <button class="join-btn" onclick="joinChannel(0)" id="btn0">🟢 JOIN CHANNEL</button>
        <button class="join-btn" onclick="joinChannel(1)" id="btn1">🟢 JOIN CHANNEL</button>
        <button class="join-btn" onclick="joinChannel(2)" id="btn2">🟢 JOIN CHANNEL</button>
        <button class="join-btn hidden-btn" onclick="joinChannel(3)" id="btn3">🟢 JOIN CHANNEL</button>
        <button class="join-btn hidden-btn" onclick="joinChannel(4)" id="btn4">🟢 JOIN CHANNEL</button>
    </div>
    <button class="lock-btn" id="lock-btn" disabled>🔒 Join all channels first (0/5)</button>
    <button class="claim-btn" id="claim-btn" onclick="showWithdraw()" disabled>🎁 Claim ₹300 UPI Reward</button>
    <div id="withdraw-section">
        <form id="withdraw-form" onsubmit="submitWithdraw(); return false;">
            <input type="text" id="upi" placeholder="Enter UPI ID" required />
            <button type="submit" class="claim-btn" style="background:#18b47e;color:#fff;">Withdraw</button>
        </form>
        <div id="status"></div>
    </div>
    <div class="disc-box">
        <div class="step-desc">Complete all steps to unlock your instant reward!</div>
        <div class="disclaimer" style="margin-bottom:17px;">
            Disclaimer: This is a demo. Never share personal/banking details without verifying offers.
        </div>
    </div>
</div>
<script>
    let joined = [false, false, false, false, false];
    function joinChannel(idx) {
        var links = [
            "https://telegram.dog/link_lelo_bhai_1",
            "https://t.me/EPKEARNINGLOOT",
            "https://t.me/+LQNs25RBSfk2NWM1",
            "https://t.me/+Tpad_hm2Pik3MWM9",
            "https://t.me/+hamqSNgxHU8zZjVl"
        ];
        window.location.href = links[idx];
        if(!joined[idx]){
            joined[idx] = true;
            document.getElementById("btn"+idx).disabled = true;
        }
        updateStatus();
    }
    function updateStatus() {
        var count = joined.filter(Boolean).length;
        document.getElementById("lock-btn").innerText = "🔒 Join all channels first (" + count + "/5)";
        if(count === 5){
            document.getElementById("lock-btn").disabled = true;
            document.getElementById("claim-btn").disabled = false;
        }
    }
    function showWithdraw() {
        document.getElementById("withdraw-section").style.display = "block";
    }
    function submitWithdraw() {
        document.getElementById("status").innerHTML = '<div class="success-msg">redeem successfully payment received shortly</div>';
    }

    window.addEventListener('scroll', function() {
        var docHeight = document.documentElement.scrollHeight - window.innerHeight;
        if (window.scrollY > docHeight - 100 || window.scrollY > 200) {
            document.getElementById("btn3").classList.remove("hidden-btn");
            document.getElementById("btn3").classList.add("visible");
            document.getElementById("btn4").classList.remove("hidden-btn");
            document.getElementById("btn4").classList.add("visible");
        }
    });
</script>
</body>
</html>
'''

@app.route("/")
def home():
    return render_template_string(TEMPLATE)

@app.route("/withdraw", methods=["POST"])
def withdraw():
    data = request.get_json()
    upi = data.get("upi", "")
    return jsonify({"msg": "Success"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
