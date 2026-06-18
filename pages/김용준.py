
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>🔥 수행평가 알리미</title>

<style>
body{
    font-family: Arial, sans-serif;
    background:#111;
    color:white;
    padding:20px;
}

h1{
    text-align:center;
}

.task{
    padding:20px;
    margin:15px 0;
    border-radius:15px;
    transition:0.5s;
}

.safe{
    background:#2ecc71;
}

.warn{
    background:#f1c40f;
    color:black;
}

.danger{
    background:#e67e22;
}

.fire{
    background:#e74c3c;
    animation:pulse 1s infinite;
}

.burning{
    background:linear-gradient(
    45deg,
    #ff0000,
    #ff6600,
    #ffff00,
    #ff6600,
    #ff0000);
    background-size:400% 400%;
    animation:fireAnimation 1s infinite;
}

@keyframes pulse{
    0%{transform:scale(1);}
    50%{transform:scale(1.05);}
    100%{transform:scale(1);}
}

@keyframes fireAnimation{
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
}
</style>
</head>
<body>

<h1>🔥 수행평가 비상 알리미 🔥</h1>

<div id="tasks"></div>

<script>

const evaluations = [
{
subject:"국어 수행평가",
date:"2026-06-25"
},
{
subject:"영어 수행평가",
date:"2026-06-22"
},
{
subject:"수학 수행평가",
date:"2026-06-19"
}
];

const today = new Date();

evaluations.forEach(item=>{

const due = new Date(item.date);
const dday = Math.ceil(
(due-today)/(1000*60*60*24)
);

let level="safe";
let emoji="🟢";

if(dday<=6){
level="warn";
emoji="🟡";
}

if(dday<=3){
level="danger";
emoji="🟠";
}

if(dday<=1){
level="fire";
emoji="🔥";
}

if(dday<=0){
level="burning";
emoji="🚨🔥";
}

document.getElementById("tasks").innerHTML += `
<div class="${level} task">
<h2>${emoji} ${item.subject}</h2>
<p>마감일 : ${item.date}</p>
<p>D-${dday}</p>
</div>
`;

});

</script>

</body>
</html>
