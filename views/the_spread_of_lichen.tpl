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
    <div class="container" style="margin: 20px;">
        <h1 style="color: var(--palette-accent)"> Решение модели</h1>
        <p>Белый - Здоровая клетка</p>
        <p style="color:#FF8743">Оранжевый - Инфецированная клетка </p>
        <p style="color:#ADFF00"> Зелёный - Клетка с иммунитетом </p>
        <label for="size">Размер NxN:</label>
        <input type="number" id="size" min="1" max="10">
        <br>
        <label for="intervals">Количество интервалов времени:</label>
        <input type="number" id="intervals" min="1" max="10">
        <br>
        <button onclick="startSimulation()">Запустить</button>
        <br><br>
        <div id="grid"></div>
    </div>

<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
    function startSimulation() {
        const size = parseInt($("#size").val());
        const intervals = parseInt($("#intervals").val());

        $.post("/simulate", { rows: size, cols: size, intervals: intervals }, function(data) {
            console.log(data);
            if (!data || !data.grid || data.grid.length === 0) {
                console.error("Invalid data format");
                return;
            }

            const gridContainer = $("#grid");

            // Функция для отображения текущей матрицы
           function displayGrid(grid) {
    gridContainer.empty();  // Очистка контейнера перед отображением новой матрицы

    for (let i = 0; i < size; i++) {
        const row = $("<div></div>");  // Создание нового элемента div для каждой строки
        row.addClass("row");

        for (let j = 0; j < size; j++) {
            const cell = $("<div></div>");
            cell.addClass("cell");

            if (grid[i][j] === "healthy") {
                cell.addClass("healthy");
            } else if (grid[i][j] === "infected") {
                cell.addClass("infected");
            } else if (grid[i][j] === "immune") {
                cell.addClass("immune");
            }

            row.append(cell);
        }

        gridContainer.append(row);
    }
}
            function displayGrid(grid) {
    gridContainer.empty();  // Очистка контейнера перед отображением новой матрицы

    for (let i = 0; i < size; i++) {
        const row = $("<div></div>");  // Создание нового элемента div для каждой строки
        row.addClass("row");

        for (let j = 0; j < size; j++) {
            const cell = $("<div></div>");
            cell.addClass("cell");

            if (grid[i][j] === "healthy") {
                cell.addClass("healthy");
            } else if (grid[i][j] === "infected") {
                cell.addClass("infected");
            } else if (grid[i][j] === "immune") {
                cell.addClass("immune");
            }

            row.append(cell);
        }

        gridContainer.append(row);
    }
}

            // Перебор всех матриц в результирующих данных
            for (let i = 0; i < data.grid.length; i++) {
                setTimeout(function() {
                    displayGrid(data.grid[i]);
                }, i * 1500);  // Замена матрицы каждые 0.5 секунды (500 миллисекунд)
            }
        });
    }
</script>

</body>
<footer>@ Leftbrained, Inc.</footer>
</div>