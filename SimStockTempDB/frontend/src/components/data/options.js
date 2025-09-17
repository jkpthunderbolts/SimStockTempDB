const candlestickoptions = {
  chart: {
    type: 'candlestick',
    height: 350,
    width: 1000,
  },
  xaxis:{
    type: 'datetime',
    labels: {
      show: false
    }
  }
};

const baroptions = {
    chart: {
        type: 'bar',
        height: 350,
        width: 1000,
    },
    xaxis:{
        type: 'datetime',
        labels: {
            show: false
        }
    },
    dataLabels: {
        enabled: false
    },
    
    
};

export { candlestickoptions,baroptions };
