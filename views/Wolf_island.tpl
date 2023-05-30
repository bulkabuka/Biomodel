<title>Волчий остров</title>
<link rel="stylesheet" href="/static/css/main.css"/>
<div class="container back-container">
    <nav class="navbar">
            <a class="container gradient-bg title" href="/">Biomodel</a>
            <div class="container navbar navbar-right radius-md">
                <a>Популяция волков</a>
                <a>Игра в жизнь</a>
                <a href="/the_spread_of_lichen">Распространение лишая</a>
            </div>
    </nav>
<head>
    <title>Wolf Island Simulation</title>
    <style>
        #island {
            width: 400px;
            height: 400px;
            background-color: lightgreen;
            display: flex;
            flex-wrap: wrap;
        }
        .rabbit {
            background-color: white;
        }

        .wolf {
            background-color: darkgray;
        }

        .female-wolf {
            background-color: lightgray;
        }

        #start-btn {
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h1>Wolf Island Simulation</h1>
    <div id="island"></div>

    <div id="input-container">
        <div class="label">Rabbits:</div>
        <input id="rabbit-input" type="number" min="0" value="0">
        <div class="label">Wolves:</div>
        <input id="wolf-input" type="number" min="0" value="0">
        <div class="label">Female Wolves:</div>
        <input id="female-wolf-input" type="number" min="0" value="0">
        <button id="start-btn">Start</button>
    </div>
</body>
</div>