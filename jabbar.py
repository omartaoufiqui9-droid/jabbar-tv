

<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JABBAR TV</title>
    <style>
        body { 
            background: radial-gradient(circle at center, #1a0505 0%, #000000 100%); 
            color: white; font-family: sans-serif; margin: 0; min-height: 100vh;
            display: flex; align-items: center; justify-content: center;
        }
        .logo { background: #E50914; width: 80px; height: 80px; line-height: 80px; margin: 0 auto 20px; border-radius: 15px; font-size: 50px; font-weight: bold; box-shadow: 0 0 20px #ff0000; text-align: center; }
        #login-box { text-align: center; background: rgba(0,0,0,0.85); padding: 40px; border-radius: 20px; border: 1px solid #444; width: 90%; max-width: 400px; }
        input { width: 90%; padding: 12px; margin: 20px 0; border-radius: 10px; border: none; text-align: center; font-size: 16px; color: black; }
        button { background: #E50914; color: white; border: none; padding: 12px; border-radius: 10px; font-weight: bold; cursor: pointer; width: 95%; font-size: 18px; }
        #cinema-content { display: none; width: 100%; text-align: center; padding: 20px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; padding: 20px; }
        .card { background: rgba(255,255,255,0.05); padding: 15px; border-radius: 15px; border: 1px solid #333; }
        video { width: 100%; border-radius: 10px; background: #000; }
    </style>
</head>
<body>

    <div id="login-box">
        <div class="logo">J</div>
        <h1>JABBAR TV</h1>
        <p>مرحباً بك.. أدخل اسمك للمشاهدة</p>
        <input type="text" id="userName" placeholder="اكتب اسمك هنا...">
        <button onclick="enterCinema()">دخول للمكتبة</button>
    </div>

    <div id="cinema-content">
        <div class="logo" style="width:50px; height:50px; line-height:50px; font-size:30px;">J</div>
        <h2 id="welcomeText"></h2>
        <div class="grid">
            <div class="card"><h3>فيلم 1</h3><video controls src="https://www.w3schools.com/html/mov_bbb.mp4"></video></div>
            <div class="card"><h3>فيلم 2</h3><video controls src="https://media.w3.org/2010/05/sintel/trailer.mp4"></video></div>
        </div>
    </div>

    <script>
        function enterCinema() {
            var name = document.getElementById("userName").value;
            if (name.trim() !== "") {
                document.getElementById("login-box").style.display = "none";
                document.getElementById("cinema-content").style.display = "block";
                document.getElementById("welcomeText").innerText = "مشاهدة ممتعة يا " + name;
                document.body.style.display = "block"; 
            } else {
                alert("لطفاً، اكتب اسمك أولاً!");
            }
        }
    </script>
</body>
</html>
