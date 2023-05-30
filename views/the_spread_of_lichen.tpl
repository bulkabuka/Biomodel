<title>Распространение лишая</title>
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
    <style>
        .cell {
            width: 100px;
            height: 100px;
            display: inline-block;
        }
        .infected {
            background-color: red;

        }
        .immune {
            background-color: orange;
        }
        .healthy {
            background-color: green;
        }
    </style>
</head>
    <body>
    <h1>Распространение лишая на кожу</h1>
    <label for="size">Размер NxN:</label>
    <input type="number" id="size" min="1" max="10">
    <br>
    <label for="intervals">Количество интервалов времени:</label>
    <input type="number" id="intervals" min="1" max="10">
    <br>
    <button onclick="startSimulation()">Запустить моделирование</button>
    <br><br>
    <div id="grid"></div>

    <script>
function startSimulation() {
    var size = parseInt(document.getElementById("size").value);
    var intervals = parseInt(document.getElementById("intervals").value);

    if (intervals > 100) {
        intervals = 100; // Ограничение максимального количества интервалов до 100
    }

    var grid = document.getElementById("grid");
    grid.innerHTML = ""; // Очистить сетку перед новой симуляцией

    // Создать начальное состояние сетки
    var initialCell = Math.floor(size / 2);
    var cells = [];
    for (var i = 0; i < size; i++) {
        cells[i] = [];
        for (var j = 0; j < size; j++) {
            if (i === initialCell && j === initialCell) {
                cells[i][j] = { state: "infected", immunity: 4 };
            } else {
                cells[i][j] = { state: "healthy", immunity: 0 };
            }
        }
    }

    var intervalId;

    function updateGrid() {
        if (intervals <= 0) {
            clearInterval(intervalId); // Остановить интервал после выполнения всех интервалов
            return;
        }

        grid.innerHTML = ""; // Очистить сетку перед обновлением

        // Отобразить текущее состояние сетки
        for (var i = 0; i < size; i++) {
            for (var j = 0; j < size; j++) {
                var cell = document.createElement("div");
                var cellState = cells[i][j].state;
                cell.className = "cell " + cellState;
                cell.style.border = "1px solid black"; // Добавить рамку
                grid.appendChild(cell);
            }
            grid.appendChild(document.createElement("br"));
        }
        grid.appendChild(document.createElement("br"));

        // Обновить состояние сетки
        var newCells = JSON.parse(JSON.stringify(cells)); // Создать копию текущего состояния
        for (var i = 0; i < size; i++) {
            for (var j = 0; j < size; j++) {
                var currentCell = cells[i][j];
                if (currentCell.state === "infected") {
                    if (currentCell.immunity === 0) {
                        newCells[i][j] = { state: "immune", immunity: 3 };
                    } else {
                        newCells[i][j] = { state: "infected", immunity: currentCell.immunity - 1 };
                    }
                } else if (currentCell.state === "immune") {
                    if (currentCell.immunity === 0) {
                        newCells[i][j] = { state: "healthy", immunity: 0 };
                    } else {
                        newCells[i][j] = { state: "immune", immunity: currentCell.immunity - 1 };
                    }
                } else if (currentCell.state === "healthy") {
                    // Проверить соседние клетки
                    if (i > 0 && cells[i - 1][j].state === "infected") {
                        newCells[i][j] = Math.random() < 0.5 ? { state: "infected", immunity: 4 } : { state: "healthy", immunity: 0 };
                    } else if (i < size - 1 && cells[i + 1][j].state === "infected") {
                        newCells[i][j] = Math.random() < 0.5 ? { state: "infected", immunity: 4 } : { state: "healthy", immunity: 0 };
                    } else if (j > 0 && cells[i][j - 1].state === "infected") {
                        newCells[i][j] = Math.random() < 0.5 ? { state: "infected", immunity: 4 } : { state: "healthy", immunity: 0 };
                    } else if (j < size - 1 && cells[i][j + 1].state === "infected") {
                        newCells[i][j] = Math.random() < 0.5 ? { state: "infected", immunity: 4 } : { state: "healthy", immunity: 0 };
                    } else {
                        newCells[i][j] = { state: "healthy", immunity: 0 };
                    }
                }
            }
        }
        cells = newCells;

        intervals--;
    }

    function stopSimulation() {
        clearInterval(intervalId); // Остановить интервал
    }

    intervalId = setInterval(updateGrid, 500); // Запуск интервала с обновлением сетки каждые 0.5 секунды

}

    </script>
</body>


</div>