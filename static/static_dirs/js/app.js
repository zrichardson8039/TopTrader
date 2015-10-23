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

function buy() {
    var cash = Number(document.getElementById('cash').value);
    var margin = Number(document.getElementById('margin').value);
    var stock = Number(document.getElementById('stock').value);
    var proceeds = Number(document.getElementById('proceeds').value);

    if(cash < proceeds) {
        margin += proceeds - cash;
        cash = 0;
    } else {
        cash -= proceeds;
    }
    stock += proceeds;

    var total = cash + stock - margin;
    var returns = total - 100000.00;

    updateValues(cash, stock, margin, total, returns);
}

function sell() {
    var cash = Number(document.getElementById('cash').value);
    var margin = Number(document.getElementById('margin').value);
    var stock = Number(document.getElementById('stock').value);
    var proceeds = Number(document.getElementById('proceeds').value);

    if(margin > 0) {
        if(margin > proceeds) {
            margin = margin - proceeds;
        } else {
            cash = proceeds - margin;
            margin = 0;
        }
    } else {
        cash += proceeds;
    }
    stock -= proceeds;

    var total = cash + stock - margin;
    var returns = total - 100000.00;

    updateValues(cash, stock, margin, total, returns)
}

function calcProceeds() {
    var shares = document.getElementById('shares').value;
    var price = document.getElementById('price').value;
    var proceeds = document.getElementById('proceeds').value;

    proceeds = shares * price;
    proceeds = proceeds.toFixed(2);
    $('#proceeds').val(proceeds);
}


