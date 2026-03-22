<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>JABBAR TV</title>
    <style>
        body { background: #000; color: white; text-align: center; font-family: sans-serif; }
        .logo { background: #E50914; width: 70px; height: 70px; line-height: 70px; margin: 20px auto; border-radius: 15px; font-size: 40px; font-weight: bold; box-shadow: 0 0 20px #ff0000; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; padding: 20px; }
        .card { background: #1a1a1a; padding: 15px; border-radius: 15px; border: 1px solid #333; }
        video { width: 100%; border-radius: 10px; }
    </style>
</head>
<body>
    <div class="logo">J</div>
    <h1>سينما جبار الخاصة</h1>
    <div class="grid">
        <div class="card">
            <h3>فيلم أكشن 1</h3>
            <video controls src="https://www.w3schools.com/html/mov_bbb.mp4"></video>
        </div>
        <div class="card">
            <h3>فيلم أكشن 2</h3>
            <video controls src="https://media.w3.org/2010/05/sintel/trailer.mp4"></video>
        </div>
    </div>
</body>
</html>
