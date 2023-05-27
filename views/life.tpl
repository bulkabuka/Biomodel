<!DOCTYPE html>
<html lang="en">
<head>
    <title>Game of Life</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <style>
        .cell {
            width: 20px;
            height: 20px;
            border: 1px solid #ccc;
            float: left;
            border-radius: 5px;
        }
        .alive {
            background: #000;
        }
    </style>
</head>
<body>
    <h1>Game of Life</h1>
    <p>Rows: <input id="rows" type="number" min="1" value="10"></p>
    <p>Columns: <input id="cols" type="number" min="1" value="10"></p>
    <button id="start">Start Game</button>
    <button id="next">Next Generation</button>
    <div id="grid"></div>

    <script>
    $("#start").click(function() {
        $.post("/start", { rows: $("#rows").val(), cols: $("#cols").val() }, function(data) {
            $("#grid").empty();
            for(let i=0; i<$("#rows").val(); i++) {
                for(let j=0; j<$("#cols").val(); j++) {
                    $("#grid").append('<div class="cell" id="cell_'+i+'_'+j+'"></div>');
                    if(data.grid[i][j] == 1) {
                        $("#cell_"+i+"_"+j).addClass('alive');
                    } else {
                        $("#cell_"+i+"_"+j).removeClass('alive');
                    }
                }
                $("#grid").append('<div style="clear: both;"></div>');
            }
            $("#next").prop("disabled", false);
        });
    });

    $("#next").click(function() {
        $.get("/next", function(data) {
            for(var i=0; i<data.grid.length; i++) {
                for(var j=0; j<data.grid[0].length; j++) {
                    if(data.grid[i][j] == 1) {
                        $("#cell_"+i+"_"+j).addClass('alive');
                    } else {
                        $("#cell_"+i+"_"+j).removeClass('alive');
                    }
                }
            }
        });
    });

    </script>
</body>
</html>
