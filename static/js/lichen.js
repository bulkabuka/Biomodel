function startSimulation() {
        const size = parseInt($("#size").val());
        const intervals = parseInt($("#intervals").val());

        $.post("/simulate", { rows: size, cols: size, intervals: intervals }, function(data) { //с помощью jquery вызов /simulate
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

        for (let j = 0; j < size; j++) { //проверка статуса клетки и присвоение ему нужного цвета
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
                }, i * 500);  // Замена матрицы каждые 0.5 секунды (500 миллисекунд)
            }
        });
    }
    $('#save').click(function (){
        $.post("/save_lichen")
    })