<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>수행평가 알림이</title>
    <style>
        body { background-color: #121212; color: white; font-family: sans-serif; text-align: center; padding: 20px; }
        .container { display: flex; justify-content: center; gap: 20px; margin-top: 20px; }
        .card { background-color: #222; border: 2px solid #444; border-radius: 10px; padding: 20px; width: 220px; }
        .subject { font-size: 24px; font-weight: bold; }
        
        /* 불빛이 들어올 상자 */
        .light-box { 
            width: 100px; height: 100px; 
            margin: 20px auto; 
            border-radius: 10px; 
            background-color: #444; /* 기본은 회색 */
            font-size: 40px;
            line-height: 100px;
            transition: 0.3s;
        }
        
        input[type="date"] { padding: 5px; font-size: 16px; width: 80%; }
        .dday-text { font-size: 18px; font-weight: bold; margin-top: 15px; }
    </style>
</head>
<body>

    <h1>🔥 수행평가 마감 알림이 🔥</h1>
    <p>과목별 마감일을 선택하면 불의 크기와 색이 바뀝니다.</p>

    <div class="container">
        <div class="card">
            <div class="subject">📚 국어</div>
            <div id="ko-light" class="light-box">💤</div>
            <input type="date" id="ko-date" onchange="checkDday('ko')">
            <div id="ko-text" class="dday-text">날짜를 선택하세요</div>
        </div>

        <div class="card">
            <div class="subject">📐 수학</div>
            <div id="math-light" class="light-box">💤</div>
            <input type="date" id="math-date" onchange="checkDday('math')">
            <div id="math-text" class="dday-text">날짜를 선택하세요</div>
        </div>

        <div class="card">
            <div class="subject">🔤 영어</div>
            <div id="eng-light" class="light-box">💤</div>
            <input type="date" id="eng-date" onchange="checkDday('eng')">
            <div id="eng-text" class="dday-text">날짜를 선택하세요</div>
        </div>
    </div>

    <script>
        function checkDday(subject) {
            var dateVal = document.getElementById(subject + '-date').value;
            var lightEl = document.getElementById(subject + '-light');
            var textEl = document.getElementById(subject + '-text');

            if (!dateVal) return;

            // 날짜 계산
            var today = new Date();
            today.setHours(0,0,0,0);
            var target = new Date(dateVal);
            target.setHours(0,0,0,0);

            var diff = target.getTime() - today.getTime();
            var days = Math.ceil(diff / (1000 * 60 * 60 * 24));

            // 조건에 따라 불 크기(폰트 크기)와 색상 변경
            if (days > 7) {
                // 7일 초과 : 안전 (작은 초록 불)
                lightEl.style.backgroundColor = "#00ffaa";
                lightEl.style.fontSize = "25px"; 
                lightEl.innerText = "🌱";
                textEl.innerText = "D-" + days + " (안전)";
                textEl.style.color = "#00ffaa";
            } 
            else if (days <= 7 && days > 3) {
                // 4일~7일 : 경고 (중간 주황 불)
                lightEl.style.backgroundColor = "#ff9900";
                lightEl.style.fontSize = "50px"; 
                lightEl.innerText = "🔥";
                textEl.innerText = "D-" + days + " (주의!)";
                textEl.style.color = "#ff9900";
            } 
            else if (days <= 3 && days >= 0) {
                // 0일~3일 : 위험 (거대한 빨간 불)
                lightEl.style.backgroundColor = "#ff3300";
                lightEl.style.fontSize = "80px"; 
                lightEl.innerText = "💥";
                textEl.innerText = days === 0 ? "D-Day (오늘 마감!)" : "D-" + days + " (위험!!!)";
                textEl.style.color = "#ff3300";
            } 
            else {
                // 마감 지난 경우
                lightEl.style.backgroundColor = "#555";
                lightEl.style.fontSize = "30px";
                lightEl.innerText = "❌";
                textEl.innerText = "마감됨";
                textEl.style.color = "#888";
            }
        }
    </script>
</body>
</html>
