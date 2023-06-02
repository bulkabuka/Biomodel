        // добавление нужного количества клеток
        // и инициализация поля (берем данные из метода start в модуле на Python)
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

    // обработка нажатия кнопки следующего поколения,
    // изменяет классы клеток, что позволяет видеть динамику
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

    $('#save').click(function () {
        $.post("/save-life")
    })