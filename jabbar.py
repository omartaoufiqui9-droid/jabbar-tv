
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JABBAR TV</title>
    <style>
        body { background: radial-gradient(circle, #1a0505, #000); color: white; font-family: sans-serif; margin: 0; text-align: center; }
        .logo { background: #E50914; width: 60px; height: 60px; line-height: 60px; margin: 20px auto; border-radius: 12px; font-size: 40px; font-weight: bold; box-shadow: 0 0 15px #ff0000; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; padding: 20px; }
        .card { background: rgba(255,255,255,0.05); border: 1px solid #333; padding: 15px; border-radius: 15px; transition: 0.3s; }
        .card:hover { border-color: #E50914; transform: scale(1.02); }
        video { width: 100%; border-radius: 10px; }
        h1 { font-size: 30px; margin-bottom: 5px; }
        .tab-bar { display: flex; justify-content: center; gap: 20px; margin-bottom: 20px; color: #888; }
    </style>
</head>
<body>
    <div class="logo">J</div>
    <h1>JABBAR TV</h1>
    <div class="tab-bar">
        <span>🎬 أفلام</span> | <span>📺 مسلسلات</span> | <span>🐥 كرتون</span>
    </div>

    <div class="grid">
        <div class="card">
            <h3>فيلم تجريبي 1</h3>
            <video controls src="https://www.w3schools.com/html/mov_bbb.mp4"></video>
        </div>
        <div class="card">
            <h3>فيلم تجريبي 2</h3>
            <video controls src="https://media.w3.org/2010/05/sintel/trailer.mp4"></video>
        </div>
        <div class="card">
            <h3>كرتون تجريبي</h3>
            <video controls src="http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"></video>
        </div>
    </div>
</body>
</html>
