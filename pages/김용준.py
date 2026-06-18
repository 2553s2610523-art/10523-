<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>수행평가 알림이</title>
    <style>
        body {
            font-family: 'Malgun Gothic', sans-serif;
            background-color: #1a1a1a;
            color: #fff;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 20px;
            margin: 0;
        }
        h1 {
            color: #ffcc00;
            margin-top: 40px;
        }
        .subject-container {
            display: flex;
            gap: 20px;
            flex-wrap: wrap;
            justify-content: center;
            margin-top: 30px;
        }
        .card {
            background-color: #2a2a2a;
            border-radius: 15px;
            padding: 20px;
            width: 250px;
            text-align: center;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5);
        }
        .subject-name {
            font-size: 1.5rem;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .fire-container {
            height: 150px;
            display: flex;
            justify-content: center;
            align-items: flex-end;
            margin-bottom: 15px;
        }
        /* 기본 불꽃 스타일 기본값 정의 */
        .fire {
            width: 40px;
            height: 40px;
            border-radius: 50% 50% 20% 50%;
            transform: rotate(-45deg);
            transition: all 0.5s ease;
        }
        /* 상태별 스타일 */
        .none {
            background-color: #444;
            box-shadow: none;
            border-radius: 50%;
        }
        .safe {
            width: 40px; height: 40px;
            background-color: #00ffaa;
            box-shadow: 0 0 15px #00ffaa;
        }
        .warning {
            width: 70px; height: 70px;
            background-color: #ff9900;
            box-shadow: 0 0 30px #ff9900;
            animation: flicker 0.1s infinite alternate;
        }
        .danger {
            width: 100px; height: 100px;
            background-color: #ff3300;
            box-shadow: 0 0 50px #ff3300;
            animation: flicker 0.05s infinite alternate;
        }
        .expired {
            background-color: #555;
            box-shadow: none;
            border-radius: 50%;
        }
        @keyframes flicker {
            0% { transform: rotate(-45deg) scale(0.95); }
            100% { transform: rotate(-45deg) scale(1.05); }
        }
        .d-day {
            font-size: 1.2rem;
            font-weight: bold;
            margin-top: 15px;
        }
        .input-group {
            margin-top: 15px;
        }
        input[type="date"] {
            padding: 8px;
            border-radius: 5px;
            border: none;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>

    <h1>🔥 수행평가 마감 시기 알림이 🔥</h1>
    <p>우리 모둠을 위한 수행평가 타임라인</p>

    <div class="subject-container">
        <div class="card">
            <div class="subject-name">📚 국어</div>
            <div class="fire-container">
                <div id="ko-fire" class="fire none"></div>
            </div>
            <div class="input-group">
                <input type="date" id="ko-date" onchange="updateDday('ko')">
            </div>
            <div class="d-day" id="ko-text">날짜를 선택하세요</div>
        </div>

        <div class="card">
            <div class="subject-name">📐 수학</div>
            <div class="fire-container">
                <div id="math-fire" class="fire none"></div>
            </div>
            <div class="input-group">
                <input type="date" id="math-date" onchange="updateDday('math')">
            </div>
            <div class="d-day" id="math-text">날짜를 선택하세요</div>
        </div>

        <div class="card">
            <div class="subject-name">🔤 영어</div>
            <div class="fire-container">
                <div id="eng-fire" class="fire none"></div>
            </div>
            <div class="input-group">
                <input type="date" id="eng-date" onchange="updateDday('eng')">
            </div>
            <div class="d-day" id="eng-text">날짜를 선택하세요</div>
        </div>
    </div>

    <script>
        function updateDday(subject) {
            const dateInput = document.getElementById(`${subject}-date`).value;
            const fireDiv = document.getElementById(`${subject}-fire`);
            const textDiv = document.getElementById(`${subject}-text`);

            if (!dateInput) {
                fireDiv.className = "fire none";
                textDiv.innerText = "날짜를 선택하세요";
                textDiv.style.color = "#fff";
                return;
            }

            const today = new Date();
            today.setHours(0, 0, 0, 0); 
            const targetDate = new Date(dateInput);
            targetDate.setHours(0, 0, 0, 0);

            const diffTime = targetDate - today;
            const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));

            // 클래스 초기화 후 새로 지정
            fireDiv.className = "fire";

            if (diffDays > 7) {
                fireDiv.classList.add("safe");
                textDiv.innerText = `D-${diffDays} (여유)`;
                textDiv.style.color = "#00ffaa";
            } else if (diffDays <= 7 && diffDays > 3) {
                fireDiv.classList.add("warning");
                textDiv.innerText = `D-${diffDays} (준비 필요!)`;
                textDiv.style.color = "#ff9900";
            } else if (diffDays <= 3 && diffDays >= 0) {
                fireDiv.classList.add("danger");
                textDiv.innerText = diffDays === 0 ? "D-Day 🔥 오늘 마감!" : `D-${diffDays} (코앞임!)`;
                textDiv.style.color = "#ff3300";
            } else {
                fireDiv.classList.add("expired");
                textDiv.innerText = "마감됨";
                textDiv.style.color = "#888";
            }
        }
    </script>
</body>
</html>
