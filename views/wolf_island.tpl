<title>Волчий остров</title>
<link rel="stylesheet" href="/static/css/main.css"/>
<head>
    <style>
        #island {
            width: 400px;
            height: 400px;
            background-color: lightgreen;
            display: flex;
            flex-wrap: wrap;
            border-radius: 20px;
            margin-top: 20px;
            margin-bottom: 20px;
        }

        .rabbit {
            background-color: white;
        }

        .wolf {
            background-color: #ADFF00;
        }

        .female-wolf {
            background-color: #FF8743;
        }

        #start-btn {
            margin-top: 20px;
        }
    </style>
</head>
<body>
<div class="container back-container">
    <nav class="navbar">
            <a class="container gradient-bg title" href="/">Biomodel</a>
            <div class="container navbar navbar-right radius-md">
                <a href="/wolf_island">Популяция волков</a>
                <a href="/life">Игра в жизнь</a>
                <a href="/the_spread_of_lichen">Распространение лишая</a>
            </div>
    </nav>

    <div class="container-main">
        <div class="container" style="margin: 20px;">
            <h1 style="color: var(--palette-accent)">Симуляция волчьего острова</h1>
            <p class="label">
    Волчий остров размером 20x20 заселен дикими кроликами, волками и волчицами.
    Имеется по нескольку представителей каждого вида. Кролики довольно
    глупы: в каждый момент времени они с одинаковой вероятностью 1/9
    передвигаются в один из восьми соседних квадратов
    (за исключением участков, ограниченных береговой линией) или просто
    сидят неподвижно. Каждый кролик с вероятностью 0,2 превращается в
    двух кроликов. Каждая волчица передвигается случайным образом,
    пока в одном из соседних восьми квадратов не окажется кролик,
    за которым она охотится. Если волчица и кролик оказываются в
    одном квадрате, волчица съедает кролика и получает одно очко.
            </p>
            <div id="island"></div>

            <p>Кролики: <input id="rabbit-input" type="number" min="0" value="5"></p>
            <p>Волки: <input id="wolf-input" type="number" min="0" value="10"></p>
            <p>Волчицы: <input id="female-wolf-input" type="number" min="0" value="7"></p>
            <button id="start-btn">Начать</button>
        </div>
    </div>
</div>
</body>