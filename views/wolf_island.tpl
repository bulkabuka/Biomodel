<title>Волчий остров</title>
<link rel="stylesheet" href="/static/css/main.css"/>
<head>
</head>
<body>
<div class="container back-container">
    <nav class="navbar" style="padding: 32px;">
            <a class="container gradient-bg title" href="/">Biomodel</a>
            <div class="container navbar navbar-right radius-md">
                <a href="/wolf_island">Популяция волков</a>
                <a href="/life">Игра в жизнь</a>
                <a href="/the_spread_of_lichen">Распространение лишая</a>
            </div>
    </nav>

    <div class="container-main" style="padding: 32px;">
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
        </div>
         <div class="container" style="margin: 20px;">
            <h1 style="color: var(--palette-secondary)">Пояснение к задаче</h1>
            <p class="label">В данной задаче моделируется ситуация на волчьем острове размером 20x20, где присутствуют дикие кролики, волки и волчицы. В начале моделирования на острове присутствуют несколько представителей каждого вида. Каждый вид имеет свое поведение и взаимодействие друг с другом.
Кролики - глупые существа, которые в каждый момент времени с одинаковой вероятностью 1/9 передвигаются в один из восьми соседних квадратов, за исключением участков, ограниченных береговой линией. Они также могут просто сидеть неподвижно. Каждый кролик с вероятностью 0,2 превращается в двух кроликов.
Волчицы - передвигаются случайным образом до тех пор, пока в одном из восьми соседних квадратов не окажется кролик, за которым они охотятся. Когда волчица и кролик оказываются в одном квадрате, волчица съедает кролика и получает одно очко.
            </p>
        </div>
    </div>
    <div class="container-main" style="padding: 32px;">
    <div class="container" style="margin: 20px; width: 100%;">
        <div style="display: flex;">
            <div id="island"></div>
            <div style="margin-left: 20px;">
                <button onclick="StartSim()">Начать</button>
                <div id="grid"></div>
            </div>
        </div>
    </div>
</div>
<footer>@ Leftbrained, Inc.</footer>
</div>

</body>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
    function StartSim() {
        $.get('/print_wolf', function(data) {
            console.log(data);
            $('#island').text(data['success'].toString());
        })
    }
</script>