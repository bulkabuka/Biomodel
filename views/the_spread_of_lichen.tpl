<title>Распространение лишая</title>
<link rel="stylesheet" href="/static/css/main.css"/>
<div class="container back-container">
    <nav class="navbar" style="padding: 32px;">
            <a class="container gradient-bg title" href="/">Biomodel</a>
            <div class="container navbar navbar-right radius-md">
                <a href="/wolf_island">Популяция волков</a>
                <a href="/life">Игра в жизнь</a>
                <a href="/the_spread_of_lichen">Распространение лишая</a>
            </div>
    </nav>
<head>
</head>
    <body>
    <div class="container-main">
        <!-- Информация о модели -->
        <div class="container" style="margin: 20px;">
            <h1 style="color: var(--palette-accent)">Распространение лишая на кожу</h1>
            <p class="label">
                Модель распространения лишая моделирует, как грибковая инфекция, такая как лишай, распространяется по поверхности кожи.
                Это может быть представлено как двумерная сетка, где каждая клетка представляет кусок кожи.
                Клетки могут быть заражены или здоровыми, и инфекция может распространяться с зарегистрированных клеток на их соседей.
                Правила модели могут включать вероятности передачи инфекции, скорость ее распространения и естественный иммунный ответ организма.
            </p>
        </div>
        <div class="container" style="margin: 20px; max-width: 40%;">
            <h1 style="color: var(--palette-secondary)">Пояснение к задаче</h1>
            <p class="label">
                Для решения модели распространения лишая была использованна матрица NxN размера.
                Предполагается, что инфецированной клеткой является центральная.
                 пораженная инфекцией клетка может с вероятностью 0,5 заразить любую из соседних здоровых клеток.
                По прошествии шести единиц времени зараженная клетка становится невосприимчивой к инфекции,
                возникший иммунитет действует в течение последующих четырех единиц времени,
                а затем клетка оказывается здоровой.
            </p>
        </div>
    </div>
    <!-- интефейс ввода значений -->
<div class="container" style="margin: 20px; display: flex;">
    <div style="flex: 1;">
        <h1 style="color: var(--palette-accent)">Решение модели</h1>
        <p>Белый - Здоровая клетка</p>
        <p style="color:#FF8743">Оранжевый - Инфицированная клетка</p>
        <p style="color:#ADFF00">Зелёный - Клетка с иммунитетом</p>
        <label for="size">Размер NxN:</label>
        <input type="number" id="size" min="1" max="10">
        <br>
        <label for="intervals">Количество интервалов времени:</label>
        <input type="number" id="intervals" min="1" max="10">
        <br>
        <!-- кнопка запуска модели -->
        <button onclick="startSimulation()">Запустить</button>
        <!-- Кнопка сохранения результата -->
        <button id="save">Сохранить</button>
    </div>
    <div id="grid"></div>
</div>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script src="/static/js/lichen.js"> </script>

</body>
<footer>@ Leftbrained, Inc.</footer>
</div>