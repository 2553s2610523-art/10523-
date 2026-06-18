<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>수행평가 알림이</title>
    <style>
        body {
            font-family: sans-serif;
            background-color: #121212;
            color: #ffffff;
            text-align: center;
            padding: 20px;
        }
        h1 { color: #ffcc00; }
        .container {
            display: flex;
            justify-content: center;
            gap: 20px;
            flex-wrap: wrap;
            margin-top: 30px;
        }
        .card {
            background-color: #1e1e1e;
            border: 1px solid #333;
            border-radius: 12px;
            padding: 20px;
            width: 240px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }
        .subject { font-size: 1.4rem; font-weight: bold; margin-bottom: 15px; }
        
        /* 불꽃 표시 영역 */
        .fire-zone {
            height: 120px;
            display: flex;
            justify-content: center;
            align-items: flex-end;
            margin-bottom: 15px;
        }
        .fire-ball {
            border-radius: 50% 50% 20% 50%;
            transform: rotate(-45deg);
            transition: all 0.3s ease;
        }
        
        /* 상태별 불꽃 (크기, 색상, 그림자) */
        .state-none { width: 30px; height: 30px; background-color: #444; border-radius: 50%; transform: none; }
        .state-safe { width: 40px; height: 40px; background-color: #00ffaa; box-shadow: 0 0 15px #00ffaa; }
        .state-warning { width: 70px; height: 70px; background-color: #ff9900; box-shadow: 0 0 25px #ff9900; }
        .state-danger { width: 100px; height: 100px; background-color: #ff3300; box-shadow: 0 0 40px #ff3300; }
        .state-end { width: 30px; height: 30px; background-color: #555; border-radius: 50%; transform: none; }

        .date-input { margin-top: 15px; }
        input[type="date"] { padding: 6px; font-size: 0.9rem; border-radius: 4px; border: none; }
        .dday-text { font-size: 1.1rem; font-weight: bold; margin-top: 15px; }
    </style>
</head>
<body>

    <h1>🔥 수행평가 알림이</h1>
    <p>날짜를 입력하면 불꽃의 크기와 색상이 변합니다.</p>

    <div class="container">
        <div class="card">
            <div class="subject">📚 국어</div>
            <div class="fire-zone"><div id="ko-fire" class="fire-ball state-none"></div></div>
            <div class="date-input"><input type="date" id="ko-date" onchange="calculate('ko')"></div>
            <div id="ko-text" class="dday-text">날짜를 설정하세요</div>
        </div>

        <div class="card">
            <div class="subject">📐 수학</div>
            <div class="fire-zone"><div id="math-fire" class="fire-ball state-none"></div></div>
            <div class="date-input"><input type="date" id="math-date" onchange="calculate('math')"></div>
            <div id="math-text" class="dday-text">날짜를 설정하세요</div>
        </div>

        <div class="card">
            <div class="subject">🔤 영어</div>
            <div class="fire-zone"><div id="eng-fire" class="fire-ball state-none"></div></div>
            <div class="date-input"><input type="date" id="eng-date" onchange="calculate('eng')"></div>
            <div id="eng-text" class="dday-text">날짜를 설정하세요</div>
        </div>
    </div>

    <script>
        function calculate(sub) {
            var inputVal = document.getElementById(sub + '-date').value;
            var fireEl = document.getElementById(sub + '-fire');
            var textEl = document.getElementById(sub + '-text');

            if (!inputVal) {
                fireEl.className = "fire-ball state-none";
                textEl.innerText = "날짜를 설정하세요";
                textEl.style.color = "#fff";
                return;
            }

            var today = new Date();
            today.setHours(0,0,0,0);
            var target = new Date(inputVal);
            target.setHours(0,0,0,0);

            var diff = target.getTime() - today.getTime();
            var days = Math.ceil(diff / (1000 * 60 * 60 * 24));

            // 모든 상태 클래스 초기화
            fireEl.className = "fire-ball";

            if (days > 7) {
                fireEl.classList.add("state-safe");
                textEl.innerText = "D-" + days + " (여유)";
                textEl.style.color = "#00ffaa";
            } else if (days <= 7 && days > 3) {
                fireEl.classList.add("state-warning");
                textEl.innerText = "D-" + days + " (경고)";
                textEl.style.color = "#ff9900";
            } else if (days <= 3 && days >= 0) {
                fireEl.classList.add("state-danger");
                textEl.innerText = days === 0 ? "D-Day (오늘 마감!)" : "D-" + days + " (위험!)";
                textEl.style.color = "#ff3300";
            } else {
                fireEl.classList.add("state-end");
                textEl.innerText = "마감됨";
                textEl.style.color = "#888";
            }
        }
    </script>
</body>
</html>
