transactions = []


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
    var price = Number(document.getElementById('price').value);
    var shares = Number(document.getElementById('shares').value);
    var commission = Number(document.getElementById('commission').value);

    var transaction = {
        'price': price,
        'shares': shares,
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
}

function calcProceeds() {
    var shares = document.getElementById('shares').value;
    var price = document.getElementById('price').value;
    var proceeds = document.getElementById('proceeds').value;

    proceeds = shares * price;
    proceeds = proceeds.toFixed(2);
    $('#proceeds').val(proceeds);
}


