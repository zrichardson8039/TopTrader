transactions = []

var interestRate = 0.05;
var timeIncrement = 1/52;
var volatility = 0.15;


var data = [];
var totalTicks = 52;
var updateInterval = 1000;
var now = new Date().getTime();

function weinerProcess() {
    return Math.random() - 0.5;
}

function GetPrice() {
    var i = 0;
    while (data.length < totalTicks) {
        var currentPrice = Number(document.getElementById('price').value);
        var newPrice = interestRate * timeIncrement * currentPrice + currentPrice * volatility * weinerProcess();
        var temp = [i, newPrice];
        $('#price').val(newPrice);

        data.push(temp);
    }
}

var options = {
    series: {
        lines: {
            show: true,
            lineWidth: 1.2,
            fill: true
        }
    },

    xaxis: {
        mode: "time",
        tickSize: [2, "second"],
        tickFormatter: function (v, axis) {
            var date = new Date(v);

            if (date.getSeconds() % 20 == 0) {
                var hours = date.getHours() < 10 ? "0" + date.getHours() : date.getHours();
                var minutes = date.getMinutes() < 10 ? "0" + date.getMinutes() : date.getMinutes();
                var seconds = date.getSeconds() < 10 ? "0" + date.getSeconds() : date.getSeconds();

                return hours + ":" + minutes + ":" + seconds;
            } else {
                return "";
            }
        },
        axisLabel: "Week",
        axisLabelUseCanvas: true,
        axisLabelFontSizePixels: 12,
        axisLabelFontFamily: 'Verdana, Arial',
        axisLabelPadding: 10
    },

    yaxis: {
        min: 0,
        max: 100,
        tickFormatter: function (v, axis) {
            if (v % 10 == 0) {
                return v + "%";
            } else {
                return "";
            }
        },
        axisLabel: "Stock Price",
        axisLabelUseCanvas: true,
        axisLabelFontSizePixels: 12,
        axisLabelFontFamily: 'Verdana, Arial',
        axisLabelPadding: 6
    },

    legend: {
        labelBoxBorderColor: "#fff"
    },

    grid: {
        backgroundColor: "#000000",
        tickColor: "#008040"
    },
};


$(document).ready(function () {
    GetPrice();

    dataset = [
        { label: "Stock", data: data, color: "#00FF00" }
    ];

    $.plot("#placeholder1", dataset, options);

    function update() {
        GetPrice();

        $.plot("#placeholder1", dataset, options)
        setTimeout(update, updateInterval);
    }

    update();
});

function updateValues(cash, stock, margin, total, returns) {
    cash = cash.toFixed(2);
    stock = stock.toFixed(2);
    margin = margin.toFixed(2);
    total = total.toFixed(2);
    returns = returns.toFixed(2);

    $('#cash').val(cash);
    $('#stock').val(stock);
    $('#margin').val(margin);
    $('#total').val(total);
    $('#returns').val(returns);
}

function createTransaction(transaction_type) {
    var game = "{{ game_id }}"
    var price = Number(document.getElementById('price').value);
    var shares = Number(document.getElementById('shares').value);
    var commission = Number(document.getElementById('commission').value);

    var transaction = {
        'game': game,
        'price': price,
        'shares': shares,
        'commission': commission,
        'transaction_type': transaction_type,
    };
    return transaction;
}

function buy() {
    transaction = createTransaction('B');
    transactions.push(transaction);
    var cash = Number(document.getElementById('cash').value);
    var margin = Number(document.getElementById('margin').value);
    var stock = Number(document.getElementById('stock').value);
    var proceeds = Number(document.getElementById('proceeds').value);
    var commission = Number(document.getElementById('commission').value);

    if(cash < proceeds) {
        margin += commission + proceeds - cash;
        cash = 0;
    } else {
        cash -= proceeds + commission;
    }
    stock += proceeds;

    var total = cash + stock - margin;
    var returns = total - 100000.00;

    updateValues(cash, stock, margin, total, returns);
    console.log(transactions);

    $.ajax({
            url: 'http://localhost:8000/api/transactions/',
            type: 'post',
            data: transactions,
            dataType: 'JSON',
            success: function(data) {
                updateValues(cash, stock, margin, total, returns)
            }
    });
}

function sell() {
    transaction = createTransaction('S');
    transactions.push(transaction);
    var cash = Number(document.getElementById('cash').value);
    var margin = Number(document.getElementById('margin').value);
    var stock = Number(document.getElementById('stock').value);
    var proceeds = Number(document.getElementById('proceeds').value);
    var commission = Number(document.getElementById('commission').value);

    if(margin > 0) {
        if(margin > (proceeds-commission)) {
            margin = margin - (proceeds-commission);
        } else {
            cash = (proceeds-commission) - margin;
            margin = 0;
        }
    } else {
        cash += (proceeds-commission);
    }
    stock -= proceeds;

    var total = cash + stock - margin;
    var returns = total - 100000.00;

    updateValues(cash, stock, margin, total, returns)
    console.log(transactions);

    $.ajax({
            url: 'http://localhost:8000/api/transactions/',
            type: 'post',
            data: transactions,
            dataType: 'JSON',
            success: function(data) {
                updateValues(cash, stock, margin, total, returns)
            }
    });
}

function calcProceeds() {
    var shares = document.getElementById('shares').value;
    var price = document.getElementById('price').value;
    var proceeds = document.getElementById('proceeds').value;

    proceeds = shares * price;
    proceeds = proceeds.toFixed(2);
    $('#proceeds').val(proceeds);
}

$(document).ready(function() {
    $('#submit-game-button').click(function() {
        var game = "{{ game_id }}"
        var cash = Number(document.getElementById('cash').value);
        var margin = Number(document.getElementById('margin').value);
        var stock = Number(document.getElementById('stock').value);
        var total_value = Number(document.getElementById('total').value);
        var net_income = Number(document.getElementById('returns').value);

        var gameData = {
            'id': game,
            'cash': cash,
            'margin': margin,
            'stock': stock,
            'total_value': total_value,
            'net_income': net_income,
        }

        $.ajax({
            url: 'http://localhost:8000/api/games/',
            type: 'put',
            data: gameData,
            dataType: 'JSON',
            success: function(data) {
                var jsonData = $.parseJSON(data);
                $('#cash').val(jsonData.cash);
                $('#margin').val(jsonData.margin);
                $('#stock').val(jsonData.stock);
                $('#total').val(jsonData.total_value);
                $('#returns').val(jsonData.net_income);
            }
        });
    });
});



