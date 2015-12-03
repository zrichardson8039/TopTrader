function resetPortfolio() {
    $('#id_cash').val(100000);
    $('#id_margin').val(0);
    $('#id_shares').val(0);
    $('#id_stock_value').val(0);
    $('#id_net_income').val(0);
}

function updateValues(cash, margin, totalShares, shareValue, returns) {

    cash = cash.toFixed(2);
    margin = margin.toFixed(2);
    totalShares = totalShares.toFixed(0);
    shareValue = shareValue.toFixed(2);
    returns = returns.toFixed(2);

    $('#id_cash').val(cash);
    $('#id_margin').val(margin);
    $('#id_shares').val(totalShares);
    $('#id_stock_value').val(shareValue);
    $('#id_net_income').val(returns);
}

function buy() {
    var cash = Number(document.getElementById('id_cash').value);
    var margin = Number(document.getElementById('id_margin').value);
    var totalShares = Number(document.getElementById('id_shares').value);
    var shares = Number(document.getElementById('shares').value);
    var price = Number(document.getElementById('price').value);
    var proceeds = Number(document.getElementById('proceeds').value);

    if(cash < proceeds) {
        margin += proceeds - cash;
        cash = 0;
    }
    else {
        cash = cash - proceeds;
    }

    totalShares = totalShares + shares;
    var shareValue = totalShares * price;
    var returns = cash - margin + shareValue - 100000;



    updateValues(cash, margin, totalShares, shareValue, returns);

}

function sell() {
    var cash = Number(document.getElementById('id_cash').value);
    var margin = Number(document.getElementById('id_margin').value);
    var totalShares = Number(document.getElementById('id_shares').value);
    var shares = Number(document.getElementById('shares').value);
    var price = Number(document.getElementById('price').value);
    var proceeds = Number(document.getElementById('proceeds').value);

    if(margin > 0) {
        if(margin > proceeds) {
            margin = margin - proceeds;
        }
        else {
            cash = proceeds - margin;
            margin = 0;
        }
    }
    else {
        cash += proceeds;
    }

    totalShares -= shares;
    var shareValue = totalShares * price;
    var returns = cash - margin + shareValue - 100000;

    updateValues(cash, margin, totalShares, shareValue, returns);
}

function calcProceeds() {
    var shares = document.getElementById('shares').value;
    var price = document.getElementById('price').value;
    var proceeds = document.getElementById('proceeds').value;

    proceeds = shares * price;
    proceeds = proceeds.toFixed(2);
    $('#proceeds').val(proceeds);
}

function calcReturns() {
    var cash = Number(document.getElementById('id_cash').value);
    var margin = Number(document.getElementById('id_margin').value);
    var totalShares = Number(document.getElementById('id_shares').value);
    var price = Number(document.getElementById('price').value);
    var shareValue = totalShares * price;
    var returns = cash - margin + shareValue - 100000;

    shareValue = shareValue.toFixed(2);
    returns = returns.toFixed(2);
    $('#id_stock_value').val(shareValue);
    $('#id_net_income').val(returns);
}

$(document).ready(function() {
    document.getElementById("id_cash").readOnly = true;
    document.getElementById("id_margin").readOnly = true;
    document.getElementById("id_shares").readOnly = true;
    document.getElementById("id_stock_value").readOnly = true;
    document.getElementById("id_net_income").readOnly = true;

    var i = 0;
    var res = [];
    var data = [];
	var totalTicks = 60;

    function generateNextPrice() {
        var prev = data.length > 0 ? data[data.length - 1] : 50,
            y = prev + (prev * 0.10 * (Math.random() - 0.5));
        if (y < 1) {
            y = 1;
        } else if (y > 80) {
            y = 80;
        }
        $('#price').val(y.toFixed(2));
        calcReturns();
        calcProceeds();
        data.push(y);
        res.push([i, data[i]])
        i++;
    }
    generateNextPrice();
    $.plot("#placeholder", [ res ], {
        series: {
            lines: {
                fill: true
            }
        },
        yaxis: {
            min: 0,
            max: 80
        },
        xaxis: {
            show: true
        }
    });
    var updateInterval = 1000;
    function update() {
        generateNextPrice();
        console.log(data.length);
        $.plot("#placeholder", [ res ], {
            series: {
                lines: {
                    fill: true
            }
            },
            yaxis: {
                min: 0,
                max: 80
            },
            xaxis: {
                show: true,
                min: 0,
                max: 59
            }
        });
        if(data.length < totalTicks) {
            setTimeout(update, updateInterval);
        }
    }
    update();
});