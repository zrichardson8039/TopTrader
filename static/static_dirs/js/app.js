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
            margin = mergin - proceeds;
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

    var data = [],
	    totalPoints = 150;

    function getRandomData() {

        if (data.length > 0)
            data = data.slice(1);

        // Do a random walk

        while (data.length < totalPoints) {
            // Calculate stochastic stock price
            var prev = data.length > 0 ? data[data.length - 1] : 50,
                y = prev + (prev * 0.05 * 0.02) + (prev * 0.10 * (Math.random() - 0.5));
            if (y < 0) {
                y = 0;
            } else if (y > 100) {
                y = 100;
            }
            $('#price').val(y);
            calcReturns();
            calcProceeds();
            data.push(y);
        }

        // Zip the generated y values with the x values

        var res = [];
        for (var i = 0; i < data.length; ++i) {
            res.push([i, data[i]])
        }

        return res;
    }

    // Set up the control widget

    var updateInterval = 1000;

    var plot = $.plot("#placeholder", [ getRandomData() ], {
        series: {
            shadowSize: 0	// Drawing is faster without shadows
        },
        yaxis: {
            min: 0,
            max: 100
        },
        xaxis: {
            show: false
        }
    });

    function update() {

        plot.setData([getRandomData()]);

        // Since the axes don't change, we don't need to call plot.setupGrid()

        plot.draw();
        setTimeout(update, updateInterval);
    }

    update();
});