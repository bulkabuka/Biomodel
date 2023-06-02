<!DOCTYPE html>
<html lang="en">
<head>
    <title>Игра в жизнь</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <link rel="stylesheet" href="/static/css/main.css"/>
</head>
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
        <h1 style="color: var(--palette-accent)">Игра в жизнь</h1>
        <p class="label">Игра "Жизнь" - это клеточный автомат, придуманный британским математиком Джоном Хортоном Конвеем в 1970 году.
            Она моделирует "жизнь" клеток на двумерной сетке, где каждая клетка может быть "живой" или "мертвой".
            Эволюция системы происходит по очень простым правилам, однако, несмотря на их простоту, система способна к сложному поведению,
            включая возникновение различных структур и "живых организмов".

            Главная суть - проверка состояния соседей какой-либо клетки. Например, если у мертвой клетки три живых соседа - она воскресает.
            Так же живая клетка остается живой если у нее есть 2-3 соседа (не больше), иначе она умирает.
        </p>
        </div>

        <div class="container" style="margin: 20px;">
            <h1 style="color: var(--palette-secondary)">Пояснение к задаче</h1>
            <p class="label">Игра по сути является симуляцией простейших форм жизни/клеток.
                С помощью некоторых проверок и системы живой/не живой клетки организуется самостоятельное развитие
                и появление различных структур, угасание и появление жизни. Для работы требуется только выбрать размер
                поля для игры и нажатие кнопки "Следующее поколение" для нового шага работы.
            </p>
        </div>
    </div>

    <div class="container-main" style="padding: 32px;">
        <div class="container" style="margin: 20px; width: 100%;">
            <h1 style="color: var(--palette-accent)">Игровое поле</h1>
            <p>Строки: <input id="rows" type="number" min="4" value="10" max="25"></p>
            <p>Столбцы: <input id="cols" type="number" min="4" value="10" max="25"></p>
            <button id="start">Начать игру</button>
            <button id="next">Следующее поколение</button>
            <button id="save">Сохранить результат</button>
            <div id="grid"></div>
            <label>Белый - Не живая клетка</label>
            <label style="color:#FF8743">Оранжевый - живая клетка </label>
        </div>
    </div>
    <script src="/static/js/life.js"></script>
    <footer>@ Leftbrained, Inc.</footer>
</div>
</html>
